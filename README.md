#  Risk Analyst Pro  
### A Professional Cyber Risk Management and Analysis Tool

**Developer:** [Anveeksh Mahesh Rao](https://www.anveekshmrao.com)  
**Email:** [raoanveeksh@gmail.com](mailto:raoanveeksh@gmail.com)  
**LinkedIn:** [linkedin.com/in/anveekshmrao](https://www.linkedin.com/in/anveekshmrao)

---

##  Overview

**Risk Analyst Pro** is a browser-based cyber risk management application built with **Python + Streamlit**.  
It provides an interactive environment for risk analysts, cybersecurity consultants, and students to:

- Identify & register **assets** and **threats**
- Calculate **risk scores (T × V × C)** using a visual heatmap
- Maintain a **Risk Register**, **Control Library**, and **Incident Log**
- Manage **Vendor Risks**
- Perform **Monte Carlo Simulations** for financial loss estimation
- Export structured **reports** for audits or ISO/NIST compliance

---

##  Key Features

| Feature | Description |
|----------|-------------|
| **Risk Calculator** | Compute risks using Threat × Vulnerability × Consequence scoring, visualize in a 5×5 heatmap |
| **Risk Register** | Track, update, and export all identified risks |
| **Assets & Threats** | Build your inventory of assets and threat scenarios |
| **Controls Library** | Add controls from ISO 27001 / NIST CSF / NIST 800-53 |
| **Vendor Risk** | Assess third-party and supplier exposure |
| **Reports & Exports** | Export CSV reports for all modules |
| **Monte Carlo Simulation** | Quantify financial losses and 95th-percentile Probable Maximum Loss |
| **Incident Log** | Record real events and their impact |
| **Settings & Branding** | Customize app name, email, and footer details |

---

##  Architecture
```bash
risk-analyst-pro/
│
├── Home.py                 # Main dashboard
├── utils.py                # Database + config helpers
├── risk_db.sqlite          # Auto-created SQLite DB
├── config.json             # App configuration
├── pages/
│   ├── 0 About_the_Creator.py
│   ├── 1 Risk_Calculator.py
│   ├── 2 Risk_Register.py
│   ├── 3 Assets_&_Threats.py
│   ├── 4 Controls_Library.py
│   ├── 5 Vendor_Risk.py
│   ├── 6 Reports.py
│   ├── 7 Monte_Carlo.py
│   ├── 8 Incident_Log.py
│   └── 9 Settings.py
└── requirements.txt
```
---

##  Installation & Setup

###  Clone or Download the Repository
```bash
git clone https://github.com/yourusername/risk-analyst-pro.git
cd risk-analyst-pro
```
###  Create and Activate Virtual Environment
```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```
###  Install Dependencies
```bash
pip install -r requirements.txt
```
###  Launch the App
```bash
streamlit run Home.py
```
###  Access the Tool
```bash
Open your browser and go to  http://localhost:8501
```
----
## How to Use (Step-by-Step with Example)

### Step 1 — Add Assets
1.	Open   **Assets & Threats** 
2.	Under Assets, click “Add Asset”
   
   •	Name: Customer Database
  	
	•	Owner: IT Security Team

	•	Category: Data

	•	Criticality: 5

	•	Notes: “Stores all customer PII data.”

4.	 Asset added to database.

## Step 2 — Add Threats
1.	Still in  **Assets & Threats → Threats**
2.	Click “Add Threat”
   
	•	Threat Name: Ransomware

	•	Vector: Malware via phishing emails

	•	Description: “Encrypts system files and demands ransom.”

4.	 Threat recorded.

## Step 3 — Calculate Risk
1.	Go to  Risk Calculator
2.	Choose:
   
	•	Asset: Customer Database

	•	Threat: Ransomware

4.	Set sliders:
   
	•	Likelihood (T): 4

	•	Vulnerability (V): 3

	•	Consequence (C): 5

5.	The Risk Score = 4 × 3 × 5 = 60
6.	Add mitigation note:
“Implement offline backups and MFA for admin access.”
7.	Click Add to Risk Register

## Step 4 — Manage the Register
1.	Open  **Risk Register**
2.	View all saved risks.
3.	Update fields:
   
	•	Status → Mitigated
   
	•	Owner → SOC Manager
   
	•	Review Date → 2025-12-01
   
5.	Click Save Changes

## Step 5 — Add Controls
1.	Open  Controls Library
2.	Add:
   
	•	Framework: ISO 27001 Annex A

	•	Control ID: A.12.3.1

	•	Title: Backup Procedures

	•	Description: “Ensure backups are performed and tested regularly.”

## Step 6 — Vendor Risk
Add cloud or SaaS providers and assess their risk level (criticality 1-5).

## Step 7 — Run Monte Carlo Simulation
1.	Go to  **Monte Carlo**
2.	Example:
   
	•	Simulations: 10,000

	•	Probability: 0.25

	•	Loss Range: $10,000 – $200,000
4.	Click Run
5.	Tool displays:
   
	•	Expected Annual Loss

	•	95th Percentile Loss (PML)

	•	Histogram distribution

## Step 8 — Export Reports
1. Go to  **Reports**
2. Download CSVs of:
   
	•	Risk Register

	•	Assets

	•	Vendors

	•	Controls

## Step 9 — Record Incidents

1. Document any real events in ** Incident Log with**:

	•	Title
   
	•	Date
   
	•	Severity
   
	•	Impacted Assets

## Step 10 — Customize Footer & Branding

•	Go to ** Settings**

•	Edit app name, your contact info, or matrix levels

•	Changes saved in config.json

##  Example Risk Output

| **Asset**            | **Threat**      | **Likelihood (T)** | **Vulnerability (V)** | **Consequence (C)** | **Risk Score (T×V×C)** | **Status**   | **Mitigation / Notes**                           |
|----------------------|----------------|--------------------|-----------------------|---------------------|------------------------|--------------|--------------------------------------------------|
| Customer Database    | Ransomware     | 4                  | 3                     | 5                   | **60 (High)**          | Open         | Implement offline backups and MFA for admin access |
| Payment Gateway API  | SQL Injection  | 3                  | 4                     | 4                   | **48 (Medium-High)**   | Mitigated    | Validate user input and enable WAF protection    |
| Employee Email Server| Phishing       | 5                  | 2                     | 3                   | **30 (Medium)**        | In Progress  | Conduct awareness training and enable DKIM/SPF   |
| HR Portal            | Insider Threat | 2                  | 3                     | 5                   | **30 (Medium)**        | Accepted     | Segregate duties and enable monitoring logs      |
| Backup Server        | Hardware Failure | 2                | 2                     | 4                   | **16 (Low)**           | Closed       | Maintain redundant systems and test DR plans     |

> **Interpretation:**
> - Scores below 20 = *Low risk*
> - 20–40 = *Medium risk*
> - 40–60 = *High risk*
> - Above 60 = *Critical risk*

##  Database

•	SQLite database auto-creates on first run (risk_db.sqlite)
	
•	Tables: assets, threats, risks, controls, vendors, incidents

## 📊 Technologies Used

•	Python 3.10+

•	Streamlit

•	SQLAlchemy

•	Pandas / NumPy

•	Matplotlib

##  Author & Credits
**Developed by:**
** Anveeksh Mahesh Rao**
**Cybersecurity Engineer | Founder of Cyber Tech Associates | Researcher | Educator**
### Who is Anveeksh Mahesh Rao
Anveeksh Mahesh Rao is a passionate Cybersecurity Professional, Cyber Crime Investigator, and Entrepreneur with expertise spanning digital forensics, vulnerability assessment, penetration testing, and cybersecurity education.

He is the Founder and Managing Director of Cyber Tech Associates, a firm providing end-to-end cybersecurity consulting, training, and digital investigation services. Under his leadership, Cyber Tech Associates has trained and empowered over 10,000 students, professionals, and institutions across India through workshops, seminars, and awareness programs on Cyber Crime Investigation and Cyber Forensics.

Anveeksh holds a B.Tech in Cyber Security and Cyber Forensics from Srinivas University and professional certifications including CISCO CCST. His career reflects a balance between technical expertise and strategic leadership, making him a driving force in cybersecurity innovation and education.

He has served as Guest Faculty and Keynote Speaker at numerous universities and organizations, inspiring the next generation of cybersecurity professionals through real-world insights and practical skill development.

Beyond technology, Anveeksh is also a motivational speaker and mentor, using his platform to share stories of career growth, entrepreneurship, and digital safety awareness.

 LinkedIn: www.linkedin.com/in/anveekshmrao

 Email: raoanveeksh@gmail.com

 Website: www.anveekshmrao.com

## 🏁 License
This project is released under the MIT License — free for research, academic, and authorized commercial use.
```bash
MIT License © 2025 Anveeksh Mahesh Rao
Permission is granted to use, copy, modify, and distribute this software for lawful, authorized purposes only.
```

---

##  If You Like This Project

If you find **Risk Analyst Pro** helpful or inspiring:

-  **Fork** the repository  
-  **Star** it on GitHub  
-  **Share** it with cybersecurity and risk management communities  
-  **Contribute** by improving features, fixing bugs, or adding new modules  

> Every star and contribution motivates continuous innovation in open cybersecurity education!













