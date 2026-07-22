# Password-Strength-Analyzer-Hash-Cracker
Markdown
# 🔑 Password Strength Analyzer & Hash Cracker

A hybrid cybersecurity tool written in Python that provides both defensive capabilities (evaluating password policies and calculating entropy) and offensive concepts (generating cryptographic hashes and performing dictionary attacks).

---

## 🎯 Features

* **Password Entropy & Complexity Analysis:** Calculates information entropy in bits and checks against standard password policy guidelines (length, casing, digits, special characters).
* **Multi-Hash Generation:** Converts plaintext inputs into `MD5`, `SHA-1`, and `SHA-256` digest outputs using standard Python libraries.
* **Dictionary Attack Engine:** Demonstrates hash-cracking mechanisms by testing hashed strings against wordlists line-by-line.

---

## 📁 Repository Structure

```text
password-analyzer-cracker/
├── main.py            # Core logic for analysis, hashing, and cracking
├── passwords.txt      # Sample dictionary wordlist
├── README.md          # Project documentation
🚀 How to Run
Clone the repository:

Bash
git clone [https://github.com/your-username/password-analyzer-cracker.git](https://github.com/your-username/password-analyzer-cracker.git)
cd password-analyzer-cracker
Run the script:

Bash
python main.py
🛠️ Technologies Used
Language: Python 3

Libraries: hashlib (Cryptographic hashing), math (Entropy math), re (Regex pattern matching), os
