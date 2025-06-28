# 🔐 Secure File Sharing System (AES Encrypted)

This is a secure file upload and download system built using **Python Flask** and **AES encryption (CBC mode)**. Files are encrypted during upload and decrypted only during download, simulating real-world secure file transfer workflows.

---

## 📦 Features

- ✅ AES (CBC mode) encryption for file storage
- ✅ Encrypted file upload and download system
- ✅ Secure key handling (static demo key)
- ✅ Simple frontend (HTML + Flask)
- ✅ Handles any file type (.pdf, .jpg, .txt, etc.)

---

## 🔧 Technologies Used

- Python 3.10  
- Flask (Web Framework)  
- PyCryptodome (AES Encryption)  
- HTML/CSS (Frontend)  

---

## 📁 Folder Structure

<pre> ```bash secure-file-sharing/ ├── app.py ├── encryption.py ├── requirements.txt ├── uploads/ # Encrypted files (.enc) ├── templates/ │ └── index.html ``` </pre>


---

## 🔐 How Encryption Works

- AES in CBC mode with a 16-byte key (`securefileaes128`)
- Random IV (initialization vector) prepended to each ciphertext
- Padding used for non-16-byte-aligned file content
- Key is static for demo; in production use `.env` or vaults

---

## 🚀 How to Run

```bash
git clone https://github.com/shahid455/FUTURE_CS_03.git
cd secure-file-sharing
python -m venv venv
venv\Scripts\activate   # (or source venv/bin/activate on Linux)
pip install -r requirements.txt
python app.py

Visit: http://127.0.0.1:5000/

## 📄 Security Overview

See [`security-overview.md`](./security-overview.md) for encryption flow and key handling details.


🧠 Author
Shahidul Hasan

📜 License
MIT License

