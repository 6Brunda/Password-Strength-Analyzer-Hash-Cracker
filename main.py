import hashlib
import math
import os
import re

WORDLIST_FILE = "passwords.txt"


def evaluate_password_strength(password):
    """Evaluates password strength based on length, complexity, and entropy."""
    score = 0
    feedback = []

    # Check Length
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short (less than 8 characters).")

    # Check Character Diversity
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    character_types = sum([has_upper, has_lower, has_digit, has_special])
    score += character_types

    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_digit:
        feedback.append("Add numbers.")
    if not has_special:
        feedback.append("Add special characters (!@#$).")

    # Calculate Character Set Size for Entropy
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digit:
        pool_size += 10
    if has_special:
        pool_size += 32

    # Calculate Entropy: E = L * log2(R)
    entropy = round(length * math.log2(pool_size), 2) if pool_size > 0 else 0

    # Determine Rating
    if score >= 5 and entropy > 50:
        rating = "STRONG 💪"
    elif score >= 3:
        rating = "MEDIUM ⚠️"
    else:
        rating = "WEAK ❌"

    return {
        "rating": rating,
        "score": f"{score}/6",
        "entropy": f"{entropy} bits",
        "feedback": feedback if feedback else ["Great job! Strong password."],
    }


def generate_hashes(password):
    """Generates MD5, SHA-1, and SHA-256 hashes for a given password."""
    return {
        "md5": hashlib.md5(password.encode()).hexdigest(),
        "sha1": hashlib.sha1(password.encode()).hexdigest(),
        "sha256": hashlib.sha256(password.encode()).hexdigest(),
    }


def crack_hash(target_hash, hash_type="sha256"):
    """Attempts a dictionary attack against a given hash using passwords.txt."""
    if not os.path.exists(WORDLIST_FILE):
        return f"Error: Wordlist '{WORDLIST_FILE}' not found!"

    print(
        f"\n🔍 Starting dictionary attack on target {hash_type.upper()} hash..."
    )

    with open(WORDLIST_FILE, "r", encoding="utf-8", errors="ignore") as file:
        for attempts, line in enumerate(file, start=1):
            word = line.strip()

            # Hash the word from the dictionary
            if hash_type == "md5":
                hashed_word = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha1":
                hashed_word = hashlib.sha1(word.encode()).hexdigest()
            else:  # sha256 default
                hashed_word = hashlib.sha256(word.encode()).hexdigest()

            # Compare target hash with candidate hash
            if hashed_word.lower() == target_hash.lower():
                return f"SUCCESS! Password cracked in {attempts} attempts!\nCracked Password: '{word}'"

    return (
        f"FAILED. Hash not found in wordlist after trying all entries."
    )


# --- MAIN INTERACTIVE PROGRAM ---
if __name__ == "__main__":
    print("=" * 50)
    print(" 🛡️  PASSWORD ANALYZER & HASH CRACKER TOOL  🛡️")
    print("=" * 50)

    user_pwd = input("\nEnter a password to analyze: ")

    # 1. Analyze Strength
    analysis = evaluate_password_strength(user_pwd)
    print("\n--- [1] PASSWORD STRENGTH REPORT ---")
    print(f"Rating:   {analysis['rating']}")
    print(f"Score:    {analysis['score']}")
    print(f"Entropy:  {analysis['entropy']}")
    print("Feedback:")
    for tip in analysis["feedback"]:
        print(f" - {tip}")

    # 2. Generate Hashes
    hashes = generate_hashes(user_pwd)
    print("\n--- [2] GENERATED CRYPTOGRAPHIC HASHES ---")
    print(f"MD5:    {hashes['md5']}")
    print(f"SHA1:   {hashes['sha1']}")
    print(f"SHA256: {hashes['sha256']}")

    # 3. Simulate Dictionary Attack
    print("\n--- [3] DICTIONARY ATTACK SIMULATION ---")
    crack_choice = (
        input("Do you want to test cracking this SHA-256 hash? (y/n): ")
        .strip()
        .lower()
    )

    if crack_choice == "y":
        result = crack_hash(hashes["sha256"], hash_type="sha256")
        print(result)

    print("\nExecution completed successfully!")