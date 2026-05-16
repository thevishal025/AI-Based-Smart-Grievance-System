# 🏛️ Citizen Grievance Management System (Aurora Edition)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Machine Learning](https://img.shields.io/badge/AI-Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

A state-of-the-art, AI-powered platform designed to bridge the gap between citizens and municipal authorities. Built with a premium **Aurora Light Glassmorphism** design, this system ensures transparent, rapid, and evidence-backed grievance resolution.

---

## ✨ Key Highlights

*   **🤖 AI-Powered Categorization**: Automatically routes grievances (Water, Electricity, Roads, etc.) using a pre-trained Scikit-Learn NLP model.
*   **📍 Mandatory Live Evidence**: Enforces transparency by requiring live GPS coordinates and real-time camera capture (Photo/Video).
*   **🛡️ Data Integrity**: All evidence is automatically watermarked with GPS coordinates and timestamps to prevent fraudulent submissions.
*   **🗣️ Multilingual & Voice Enabled**: Full support for English and Hindi with built-in Voice-to-Text grievance submission.
*   **⚡ Intelligent Escalation**: Automatically detects repeated complaints in the same area and escalates them to "High Priority."
*   **📧 Secure Authentication**: Email OTP-based verification (via Brevo) for all user accounts.

---

## 🎭 User Personas & Features

### 👤 Citizen Portal
- **Dashboard**: Track all personal grievances with real-time progress bars.
- **Submission**: Smart form with live location detection and camera integration.
- **Communication**: Built-in chatbot for instant query resolution.
- **Transparency**: View detailed resolution proof uploaded by department staff.

### 🏢 Department Staff (Water, Roads, etc.)
- **Workflow Management**: Transition complaints from `Pending` → `In Progress` → `Resolved`.
- **Evidence Management**: View citizen-submitted photos/videos with GPS metadata.
- **Resolution Proof**: Upload completion evidence to notify citizens.

### 🔑 Admin Oversight
- **Global Analytics**: Real-time charts for category distribution and resolution rates.
- **Priority Management**: Monitor escalated issues and department performance.
- **Data Governance**: Reset system data or manage staff access.

---

## 🛠️ Technology Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.9+, Flask |
| **Database** | SQLite3 (WAL Mode for concurrency) |
| **AI/ML** | Scikit-Learn (TF-IDF Vectorization) |
| **UI/UX** | Vanilla CSS (Glassmorphism), JavaScript (ES6+) |
| **Media** | MoviePy (Video processing), Pillow (Image watermarking) |
| **Communication** | Brevo SMTP (Email OTPs) |
| **Maps** | OpenStreetMap (Reverse Geocoding) |

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9 or higher
- A Brevo API Key (for email OTPs)

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/your-username/grievance-system.git
cd grievance-system

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
BREVO_API_KEY=your_api_key_here
BREVO_SENDER_EMAIL=your_verified_email@example.com
```

### 4. Run the Application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure

```text
├── app.py              # Main Flask application logic
├── database/
│   ├── db.py           # Database access layer & schema
│   └── grievance_system.db  # SQLite database
├── static/
│   ├── uploads/        # Citizen evidence & watermarked files
│   └── style.css       # Core design system (Aurora Light)
├── templates/          # Jinja2 HTML templates
├── models/             # Pre-trained ML models & vectorizers
├── requirements.txt    # Project dependencies
└── .env                # Secret configurations
```

---

## 📜 License & Credits
Designed and developed with ❤️ for a smarter, more transparent future.

---
*Note: This project is for demonstration purposes. Ensure `cert.pem` and `key.pem` are properly configured for production HTTPS deployment.*
