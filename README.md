# 🔍 Identity Reconciliation Backend API (Zamazon.com)

This Flask-based microservice handles identity resolution for Zamazon.com by intelligently linking multiple email and phone number combinations to a single customer identity.

---

## 🚀 Features

- Accepts contact info via `/identify` endpoint.
- Automatically links records using email or phone overlap.
- Creates primary and secondary contact entries.
- Returns consolidated contact info in the response.

---

## 🛠 Tech Stack

- Python 3.10+
- Flask
- SQLite (default for local testing)
- SQLAlchemy ORM

---

## 📦 Project Structure

# identity-reconciliation
