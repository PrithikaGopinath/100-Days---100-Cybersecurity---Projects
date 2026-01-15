import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def save_baseline(hash_value):
    with open("baseline.txt", "w") as f:
        f.write(hash_value)

def load_baseline():
    if not os.path.exists("baseline.txt"):
        return None
    with open("baseline.txt", "r") as f:
        return f.read().strip()

def main():
    file_path = input("Enter file path to check: ")

    current_hash = calculate_hash(file_path)
    if current_hash is None:
        print("❌ File not found.")
        return

    baseline_hash = load_baseline()

    if baseline_hash is None:
        print("📌 No baseline found. Creating one now...")
        save_baseline(current_hash)
        print("✅ Baseline saved.")
    else:
        print(f"🔍 Current Hash:   {current_hash}")
        print(f"📁 Baseline Hash:  {baseline_hash}")

        if current_hash == baseline_hash:
            print("🟢 File is intact. No changes detected.")
        else:
            print("🔴 WARNING: File has been modified!")

if __name__ == "__main__":
    main()
