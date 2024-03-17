import re

def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    text = input("Enter the text to extract emails from: ")
    emails = extract_emails(text)
    print("Extracted emails:", emails)
