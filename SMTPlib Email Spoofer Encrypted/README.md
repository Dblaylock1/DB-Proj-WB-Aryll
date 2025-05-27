# 📧 Email Spoofing CLI Tool (Educational Use Only)

Welcome to my personal **Email Spoofing CLI** written in Python. This tool is meant **strictly for educational and lab testing purposes** and is not to be used for unethical or illegal activity. If you're experimenting with SMTP services and want to understand how spoofing works under the hood, this project is a clean CLI starter that does exactly that.

---

## 🚨 Disclaimer

> This tool is **not meant to undermine legal authorities** or be used for phishing.  
> Use only in controlled, consented environments (e.g., your lab, CTFs, etc.).  
> Any misuse is entirely your responsibility.

---

## 🔐 Recommended Anonymity

If you *must* test in a public environment, it's strongly encouraged that you use:

- `proxychains4` on **Kali Linux**
- Tor routing or a solid list of **working proxy servers**

**Proxychains** is better if you're dealing with dynamic IP masking and have a strong proxy rotation strategy.

---

## 🛠 Features

- Interactive CLI interface with human-style prompts
- Supports multiple public SMTP services:
  - Yahoo
  - Gmail
  - Hotmail (Live)
  - Brinkster (Port 2525)
- Mimics spoofing by letting you input a custom `From:` address
- Infinite main loop for testing multiple payloads

---

## 💻 How To Use

```bash
python3 spoof.py
