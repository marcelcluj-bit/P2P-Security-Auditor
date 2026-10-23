import os
import sys
import re
import json
from datetime import datetime

# Vulnerability signature base (easily extendable by the community)
DEFAULT_RULES = [
    {
        "id": "PHP-01",
        "name": "Potentially dangerous use of eval()",
        "extensions": [".php"],
        "pattern": r"\beval\s*\(",
        "severity": "CRITICAL",
        "advice": "Avoid executing dynamic code with eval(). It can lead to Remote Code Execution (RCE)."
    },
    {
        "id": "PHP-02",
        "name": "Unsafe system command execution",
        "extensions": [".php"],
        "pattern": r"\b(exec|shell_exec|system|passthru)\s*\(",
        "severity": "HIGH",
        "advice": "Strictly validate and sanitize any user input before passing it to system execution functions."
    },
    {
        "id": "GEN-01",
        "name": "Hardcoded API keys, secrets, or plain-text passwords",
        "extensions": [".php", ".py", ".js", ".env", ".json", ".yml"],
        "pattern": r"(api_key|password|secret|passwd)\s*=\s*['\"][a-zA-Z0-9_\-]{8,}['\"]",
        "severity": "HIGH",
        "advice": "Move sensitive credentials and secrets into secure environment variables (.env)."
    }
]

def scan_file(file_path, rules):
    findings = []
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            
        for line_num, line in enumerate(lines, 1):
            for rule in rules:
                if any(file_path.endswith(ext) for ext in rule["extensions"]):
                    if re.search(rule["pattern"], line, re.IGNORECASE):
                        findings.append({
                            "rule_id": rule["id"],
                            "name": rule["name"],
                            "severity": rule["severity"],
                            "file": file_path,
                            "line": line_num,
                            "content": line.strip(),
                            "advice": rule["advice"]
                        })
    except Exception as e:
        print(f"[Error] Could not read file {file_path}: {e}")
    return findings

def audit_directory(target_dir, rules):
    all_findings = []
    print(timestamp_print(f"[*] Starting local audit for directory: {target_dir}"))
    
    for root, _, files in os.walk(target_dir):
        # Exclude common non-source directories
        if any(exc in root for exc in ['.git', 'node_modules', 'vendor', '__pycache__']):
            continue
        for file in files:
            file_path = os.path.join(root, file)
            findings = scan_file(file_path, rules)
            all_findings.extend(findings)
            
    return all_findings

def timestamp_print(text):
    return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}"

def main():
    print("=" * 65)
    print("         P2P-Security-Auditor (Open-Source Tool)         ")
    print("=" * 65)
    
    target = input("Enter target directory path (press Enter for current directory): ").strip()
    if not target:
        target = "."
        
    if not os.path.exists(target):
        print(f"[Error] The specified path '{target}' does not exist!")
        sys.exit(1)
        
    findings = audit_directory(target, DEFAULT_RULES)
    
    print("\n" + "=" * 65)
    print(f" AUDIT RESULTS: Found {len(findings)} potential security issues.")
    print("=" * 65 + "\n")
    
    if not findings:
        print("[+] Success! No matching vulnerable patterns detected based on active rules.")
    else:
        for idx, f in enumerate(findings, 1):
            print(f"{idx}. [{f['severity']}] {f['name']}")
            print(f"   File: {f['file']} (Line {f['line']})")
            print(f"   Snippet: {f['content']}")
            print(f"   Recommendation: {f['advice']}")
            print("-" * 55)
            
    # Save JSON report locally
    report_file = "security_report.json"
    with open(report_file, 'w', encoding='utf-8') as rf:
        json.dump(findings, rf, indent=4, ensure_ascii=False)
    print(f"\n[+] Detailed report successfully saved locally to: {report_file}")

if __name__ == "__main__":
    main()
