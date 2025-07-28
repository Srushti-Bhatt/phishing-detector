import re

# Step 1: Input email text
email_text = input("Paste the email content here:\n")

# Step 2: Phishing keywords
phishing_keywords = [
    "urgent", "verify", "click here", "login", "update", "account suspended", "reset password"
]

found_keywords = [word for word in phishing_keywords if word.lower() in email_text.lower()]

# Step 3: Check for suspicious links
suspicious_links = re.findall(r'http[s]?://[^\s]+', email_text)
shorteners = ['bit.ly', 'tinyurl', 'rb.gy', 't.co']
flagged_links = [link for link in suspicious_links if any(s in link for s in shorteners)]

# Step 4: From address spoof check
from_address = input("\nEnter the FROM email address:\n")
spoof_domains = ["microsoft", "apple", "bank", "paypal"]
spoofed = []

for domain in spoof_domains:
    if domain in from_address.lower() and not from_address.endswith(f"{domain}.com"):
        spoofed.append(from_address)

# Step 5: Final Report
print("\n--- PHISHING SCAN REPORT ---\n")

if found_keywords:
    print(f"⚠️ Found phishing keywords: {', '.join(found_keywords)}")
else:
    print("✅ No phishing keywords found.")

if flagged_links:
    print(f"⚠️ Found suspicious links: {', '.join(flagged_links)}")
else:
    print("✅ No suspicious links found.")

if spoofed:
    print(f"⚠️ Suspected spoofed email address: {from_address}")
else:
    print("✅ Email address appears safe.")

print("\nScan Complete ✅")
