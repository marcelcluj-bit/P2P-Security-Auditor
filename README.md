# P2P-Security-Auditor 🛡️

An open-source, lightweight, local-first Python tool designed to help developers, sysadmins, and small organizations locally audit their codebase for potential security vulnerabilities and risky functions before deployment.

---

## 🔓 Unlicense / Zero Restrictions

This project is released into the **Public Domain** under **The Unlicense**. 

* **No Legal Barriers:** Anyone is free to copy, modify, publish, use, compile, sell, or distribute this software, either in source code form or as a compiled binary, for any purpose, commercial or non-commercial, and by any means.
* **No Attribution Required:** You do not need permission, license agreements, or legal approval from compliance departments to run this code in government agencies, hospitals, schools, or private enterprises.
* **Pure Public Good:** Cybersecurity is a shared public responsibility. This tool belongs to everyone.

---

## 🚀 Why this project?

Millions of websites and servers run on open-source or legacy codebases. Security audits are often too expensive or time-consuming for small teams, local administrations, and independent developers. This tool provides a free, privacy-first, peer-to-peer approach to proactive cybersecurity.

---

## 💡 3 Essential Tips for Effective Usage

1. **Run Locally Before Deployment:** Always execute the auditor locally in your development or staging environment before pushing code to production servers. This catches hardcoded secrets or risky functions early without exposing your code to external third parties.
2. **Customize Rules for Your Stack:** The `DEFAULT_RULES` array can be easily extended. If your project uses specific frameworks or custom patterns, add regular expressions tailored to your technology stack.
3. **Combine Automation with Code Review:** While the tool automates the detection of common patterns (like `eval()` or hardcoded keys), always perform a manual code review for critical business logic and authentication modules.

---

## ⚙️ Quick Start (Python)

1. Ensure you have Python 3 installed.
2. Save the script as `auditor.py`.
3. Run the script from your terminal:

```bash
python auditor.py

```




## Proiectul in limba romana

Proiectul complet — intitulat Securitate-P2P-Auditor — este structurat mai jos sub formă de cadru de management, diagrame analitice și codul sursă Python deschis și gratuit.

## 1. Analiza Stakeholderilor (Părți Implicate)CategoriaRol / InteresImpact / InfluențăDezvoltatori & SysadminiUtilizează scriptul Python pentru a-și verifica local serverele și aplicațiile.Ridicat (Sunt primii care aplică corecțiile).Comunitatea Open-SourceContribuie cu semnături de vulnerabilități, reguli de căutare și optimizări.Ridicat (Asigură actualizarea continuă a instrumentului).Instituțiile Publice & SpitaleleBeneficiază de audit gratuit pentru infrastructura critică legacy.Mediu (Protejează serviciile esențiale pentru cetățeni).Atacatorii CiberneticiÎncearcă să inverseze ingineria scriptului pentru a găsi sisteme neactualizate.Ridicat (Reprezintă amenințarea activă din exterior).

## 2. Arborele de ProblemeProblema Centrală: Infrastructura digitală globală și locală este vulnerabilă din cauza codului vechi neverificat și a lipsei de resurse financiare pentru audituri de securitate profesionale.Cauze (Rădăcini):Costurile ridicate ale companiilor de securitate privată.Lipsa timpului și a personalului specializat în instituțiile mici și medii.Dependența masivă de biblioteci legacy open-source întreținute de voluntari.Efecte (Fructe/Consecințe):Compromiterea în masă a serverelor guvernamentale și comerciale.Întreruperea serviciilor publice (spitale, utilități, administrație).Pierderi economice uriașe și erodarea încrederii în mediul digital.
## 3. Arborele de Riscuri și Managementul RisculuiRisc 1: Armarea instrumentului de către atacatori (Hackerii folosesc logica scriptului pentru a scana rapid internetul după ținte vulnerabile).Mitigare: Scriptul este conceput strict pentru rulare locală (offline-first) pe folderele proprii ale deținătorului, fără funcții de scanare externă agresivă.Risc 2: Alarme false (False Positives) care blochează activitatea dezvoltatorilor.Mitigare: Sistem modular de reguli bazat pe expresii regulate validate și niveluri clare de severitate (Info, Warning, Critical).Risc 3: Uzura morală rapidă a semnăturilor de vulnerabilități în fața unor noi tipuri de atacuri.Mitigare: Arhitectură modulară unde fișierul de semnături (rules.json) poate fi actualizat instantaneu de comunitate.

## 4. Analiza SWOTPuncte Tari (Strengths):Accesibilitate totală (gratuit, cod sursă deschis, rulare simplă în Python).Fără dependență de cloud extern; datele utilizatorului rămân pe propria mașină (confidențialitate 100%).Distribuție virală prin simplul parteneriat P2P / GitHub.Puncte Slabe (Weaknesses):Nu poate detecta vulnerabilități logice extrem de complexe fără modele AI avansate.Depinde de disciplina utilizatorului de a rula frecvent scriptul și de a aplica patch-urile.Oportunități (Opportunities):Crearea unei rețele globale de solidaritate cibernetică open-source.Adoptarea instrumentului de către școli, primării și IMM-uri care nu au bugete de securitate.Amenințări (Threats):Încercări de discreditare a instrumentului de către actori interesați de menținerea monopolului pe serviciile de securitate scumpe.

## 5. Diagrama Ishikawa (Cauză-Efect) pentru VulnerabilitățiPlaintext[Oameni / Resurse]                 [Procese / Cod]
- Lipsă specialiști securitate  -->  - Cod vechi (legacy) neactualizat
- Bugete insuficiente           -->  - Lipsă audituri preventive regulate
        \                             /
          [ VULNERABILITATE CIBERNETICĂ ]
        /                             \
- Unelte comerciale prea scumpe -->  - Lipsă instrumente automate gratuite
- Accesibilitate redusă a tool-urilor - Distribuție lentă a corecțiilor
[Tehnologie / Unelte]              [Mediu / Distribuție]
6. Planificarea Proiectului (Diagrama Gantt / Etape)Săptămâna 1 (Faza de Arhitectură): Definirea motorului de scanare statică în Python și crearea structurii de reguli (rules.json).Săptămâna 2 (Dezvoltare & Testare): Implementarea funcțiilor de căutare a pattern-urilor periculoase și generarea rapoartelor în format text/HTML.Săptămâna 3 (Lansare Open-Source): Publicarea pe GitHub sub licență liberă (MIT/Unlicense) și crearea pachetului ușor de descărcat.Săptămâna 4 (Adâncirea Comunității): Preluarea feedback-ului de la primii utilizatori, adăugarea de noi semnături pentru vulnerabilități recent descoperite.7. Codul Sursă Python: Securitate-P2P-AuditorMai jos este un cod sursă complet, curat și gratuit în Python. El scanează recursiv un director de proiect (cum ar fi un site PHP sau o aplicație web) căutând funcții potențial periculoase (de ex. eval, system, shell_exec neprotejate) și generează un raport clar.Python#!/usr/bin/env python3
"""
Nume Proiect: Securitate-P2P-Auditor
Descriere: Instrument open-source, local, pentru auditul preventiv al codului sursă 
           și detectarea rapidă a potențialelor breșe sau funcții nesigure.
Licență: Unlicense / Public Domain (Liber pentru oricine, oriunde).
"""

import os
import sys
import re
import json
from datetime import datetime

# Bază de semnături pentru vulnerabilități comune (se poate extinde nelimitat)
DEFAULT_RULES = [
    {
        "id": "PHP-01",
        "name": "Utilizare potențial periculoasă a funcției eval()",
        "extensions": [".php"],
        "pattern": r"\beval\s*\(",
        "severity": "CRITICAL",
        "advice": "Evitați rularea de cod dinamic cu eval(). Poate duce la RCE (Remote Code Execution)."
    },
    {
        "id": "PHP-02",
        "name": "Execuție de comenzi de sistem nesigară",
        "extensions": [".php"],
        "pattern": r"\b(exec|shell_exec|system|passthru)\s*\(",
        "severity": "HIGH",
        "advice": "Verificați riguros parametrii introduși de utilizator înainte de a rula comenzi de sistem."
    },
    {
        "id": "GEN-01",
        "name": "Prezența cheilor API hardcodate sau parolelor în clar",
        "extensions": [".php", ".py", ".js", ".env", ".json", ".yml"],
        "pattern": r"(api_key|password|secret|passwd)\s*=\s*['\"][a-zA-Z0-9_\-]{8,}['\"]",
        "severity": "HIGH",
        "advice": "Mutați secretele și parolele în variabile de mediu (.env)."
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
        print(f"[Erore] Nu s-a putut citi fișierul {file_path}: {e}")
    return findings

def audit_directory(target_dir, rules):
    all_findings = []
    print(v_print(f"[*] Începere audit local pentru directorul: {target_dir}"))
    
    for root, _, files in os.walk(target_dir):
        # Excludem folderele inutile (ex: .git, node_modules, vendor)
        if any(exc in root for exc in ['.git', 'node_modules', 'vendor', '__pycache__']):
            continue
        for file in files:
            file_path = os.path.join(root, file)
            findings = scan_file(file_path, rules)
            all_findings.extend(findings)
            
    return all_findings

def v_print(text):
    return f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {text}"

def main():
    print("=" * 60)
    print("         Securitate-P2P-Auditor (Open Source Tool)       ")
    print("=" * 60)
    
    target = input("Introduceți calea către folderul de verificat (lăsați gol pentru directorul curent): ").strip()
    if not target:
        target = "."
        
    if not os.path.exists(target):
        print(f"[Erore] Calea specificată '{target'}' nu există!")
        sys.exit(1)
        
    findings = audit_directory(target, DEFAULT_RULES)
    
    print("\n" + "=" * 60)
    print(f" REZULTATE AUDIT: S-au găsit {len(findings)0 if False else len(findings)} potențiale probleme.")
    print("=" * 60 + "\n")
    
    if not findings:
        print("[+] Felicitări! Nu s-au detectat tipare vulnerabile cunoscute conform regulilor active.")
    else:
        for idx, f in enumerate(findings, 1):
            print(f"{idx}. [{f['severity']}] {f['name']}")
            print(f"   Fișier: {f['file']} (Linia {f['line']})")
            print(f"   Cod detectat: {f['content']}")
            print(f"   Recomandare: {f['advice']}")
            print("-" * 50)
            
    # Salvare raport opțională
    report_file = "raport_securitate.json"
    with open(report_file, 'w', encoding='utf-8') as rf:
        json.dump(findings, rf, indent=4, ensure_ascii=False)
    print(f"\n[+] Raportul detaliat a fost salvat local în: {report_file}")

if __name__ == "__main__":
    main()
Cum se distribuie și se folosește?Copiere simplă: Oricine poate salva codul de mai sus într-un fișier numit auditor.py.Rulare instantanee: Cu Python instalat pe sistem, se rulează simplu din terminal: python auditor.py.P2P / Din mână în mână: Scriptul poate fi trimis prin email, distribuit pe un grup de discuții sau urcat pe un repository public, permițând oricărui administrator de sistem să își verifice imediat aplicațiile web și să corecteze liniile semnalate înainte ca cineva să le exploateze.
