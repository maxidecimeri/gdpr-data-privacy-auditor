import pandas as pd

def scan_for_pii(data):
    patterns = {
        'Email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'Phone Number': r'\b\d{10}\b',
        'Credit Card': r'\b\d{4} \d{4} \d{4} \d{4}\b',
    }
    findings = {}
    for column in data.columns:
        for key, pattern in patterns.items():
            matches = data[column].str.contains(pattern, regex=True)
            if matches.any():
                findings[column] = key
    return findings

def evaluate_gdpr_compliance(findings):
    if findings:
        compliance_score = 50
        status = "Non-compliant"
    else:
        compliance_score = 100
        status = "Compliant"
    return compliance_score, status

if __name__ == "__main__":
    file_path = input("Enter the dataset file path: ")
    data = pd.read_csv(file_path)
    findings = scan_for_pii(data)
    score, status = evaluate_gdpr_compliance(findings)
    print(f"Compliance Score: {score}")
    print(f"Status: {status}")
    if findings:
        print("Non-compliant fields detected:")
        for column, data_type in findings.items():
            print(f"{column}: {data_type}")
