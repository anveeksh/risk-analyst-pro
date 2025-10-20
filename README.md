
# Risk Analyst Pro

A local, analyst-friendly **Risk Analysis** web app you can run in your browser (localhost) using **Streamlit**.

## Features
- T×V×C **Risk Calculator** with 5×5 heatmap
- **Risk Register** (SQLite) with status, owner, review dates
- **Assets & Threats** management
- **Controls Library** (ISO 27001, NIST CSF, NIST 800-53) — add your own
- **Vendor Risk** workspace
- **Incident Log**
- **Reports & Exports** (download CSVs)
- **Monte Carlo** simulation for expected loss & PML
- **Settings** page to customize footer/name/email/website and matrix levels

## Quick Start
1. Install Python 3.10+
2. In a terminal:
   ```bash
   cd risk-analyst-pro
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   streamlit run Home.py
   ```
3. Your browser will open to `http://localhost:8501`

## Customization
- Footer & contact info are in **config.json** (auto-created on first run), or use the **🔧 Settings** page.
- Data is stored in **risk_db.sqlite** in the project folder.
- Add more pages in `pages/` to extend the app.

## Creator
By **Anveeksh Mahesh Rao** — website: https://www.anveekshmrao.com
