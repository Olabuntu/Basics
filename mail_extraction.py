import re

def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    matche = re.findall(email_pattern, text, re.IGNORECASE)
    matches = list(set(matche))
    return matches


with open ('.txt', 'r') as file:
    files =file.read()


# Extract email addresses
email_addresses = extract_emails(files)

# writing  extracted email addresses into a text file
with open('mail_address.txt', 'a') as c:
    for email in email_addresses:
        c.write(f'{email}\n')