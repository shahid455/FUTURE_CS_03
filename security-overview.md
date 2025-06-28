# 🔐 Security Overview – AES File Encryption

This system ensures that all uploaded files are encrypted using **AES (Advanced Encryption Standard)** in **CBC (Cipher Block Chaining)** mode. Files are only decrypted during the download phase, never stored in decrypted form.

---

## 🧠 How Encryption Works

| Property         | Description |
|------------------|-------------|
| **Algorithm**    | AES (Advanced Encryption Standard)  
| **Mode**         | CBC (Cipher Block Chaining)  
| **Key Size**     | 128 bits (16 bytes)  
| **Key Used**     | Static key `securefileaes128` (for demo only)  
| **IV (Nonce)**   | Random IV generated per file, stored in first 16 bytes  
| **Padding**      | Manual padding using space characters  
| **Ciphertext**   | Stored in `/uploads/` folder as `.enc` files  

---

## 🔐 Decryption Flow

1. Read first 16 bytes (IV) from the encrypted file  
2. Use the AES key and IV to decrypt the ciphertext  
3. Remove padding  
4. Serve the original file to the user as download

---

## 🔒 Key Management Notes

- For this demo, the key is hardcoded in `encryption.py`  
- In production:
  - Store the key in `.env` or secrets manager
  - Do not commit keys to GitHub
  - Rotate keys periodically if needed

---

## ✅ Security Practices Followed

- No decrypted file is stored on disk  
- Encrypted files only accessible via download route  
- Random IVs used for each encryption session  
- Encryption logic separated from app routes (`encryption.py`)

---

## ⚠️ Future Enhancements

- Add login/authentication for users  
- Implement file integrity checks (hashing)  
- Use .env file or secure vault for real key management  
