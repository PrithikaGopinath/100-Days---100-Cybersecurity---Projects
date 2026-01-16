import math
import re
import string

def calculate_entropy(password):
    charset = 0
    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_password_strength(password):
    length = len(password)
    entropy = calculate_entropy(password)

    common_patterns = ["password", "123", "qwerty", "admin", "letmein"]

    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, entropy

def main():
    password = input("Enter a password to check: ")

    strength, entropy = check_password_strength(password)

    print(f"\n🔍 Password Strength: {strength}")
    print(f"🔢 Entropy Score: {entropy} bits")

    if strength == "Weak":
        print("⚠️ Consider adding length, numbers, symbols, and avoiding common patterns.")
    elif strength == "Moderate":
        print("🟡 Not bad, but could be stronger.")
    elif strength == "Strong":
        print("🟢 Good password!")
    else:
        print("💪 Excellent! Very strong password.")

if __name__ == "__main__":
    main()
