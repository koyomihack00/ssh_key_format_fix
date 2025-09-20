
# fix_ssh_key.py

## 🔐 SSH Private Key Format Repair Tool

A Python 3 script to **fix broken SSH private key files** (bad line breaks, header/footer issues, copy-paste errors) and convert them to a format that works with OpenSSH, ssh-keygen, and all major CTF/pentest platforms.

**Supports:**
- OpenSSH format (`-----BEGIN OPENSSH PRIVATE KEY-----`)
- Traditional PEM RSA (`-----BEGIN RSA PRIVATE KEY-----`)

---

## 🚀 Usage

1. Save your broken key file as `id_rsa_broken` (or any name you like).
2. Run the script:

   ```bash
   python3 fix_ssh_key.py id_rsa_broken -o id_rsa_fixed
   ```

3. Secure the output file:

   ```bash
   chmod 600 id_rsa_fixed
   ```

4. Verify the key is valid:

   ```bash
   ssh-keygen -l -f id_rsa_fixed
   ```

5. Use it with SSH:

   ```bash
   ssh -i id_rsa_fixed user@target
   ```

---

## 📦 Example of Correct Output

**OpenSSH format:**
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAE...
...base64 data...
QIDBA==
-----END OPENSSH PRIVATE KEY-----
```

**PEM RSA format:**
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQE...
...base64 data...
AgMBAAEC
-----END RSA PRIVATE KEY-----
```

---

## 💡 Notes & Tips

- Designed for red teamers, OSCP/CTF candidates, and anyone who regularly recovers broken keys from pentest or training platforms.
- Automatically detects and fixes both OpenSSH and PEM (RSA) key formats.
- No dependencies except standard Python 3.

---

## 🧑‍💻 Author

Created by Sn1p3r-Scou7

---
