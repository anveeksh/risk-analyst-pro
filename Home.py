
import os
import streamlit as st
from utils import load_config, get_engine, init_db

st.set_page_config(page_title="Risk Analyst Pro", layout="wide")

cfg = load_config()
engine = get_engine()
init_db(engine)

with st.sidebar:
    st.title(cfg.get("app_name", "Risk Analyst Pro"))
    st.page_link("pages/0_👤_About_the_Creator.py", label="👤 About the Creator", icon="👤")
    st.caption("A modern, analyst‑friendly risk platform for T×V×C scoring, registers, and reporting.")
    st.page_link("Home.py", label="🏠 Dashboard", icon="🏠")
    st.page_link("pages/1_⚙️_Risk_Calculator.py", label="⚙️ Risk Calculator", icon="⚙️")
    st.page_link("pages/2_📚_Risk_Register.py", label="📚 Risk Register", icon="📚")
    st.page_link("pages/3_🧱_Assets_&_Threats.py", label="🧱 Assets & Threats", icon="🧱")
    st.page_link("pages/4_🛡️_Controls_Library.py", label="🛡️ Controls Library", icon="🛡️")
    st.page_link("pages/5_📦_Vendor_Risk.py", label="📦 Vendor Risk", icon="📦")
    st.page_link("pages/6_📄_Reports.py", label="📄 Reports", icon="📄")
    st.page_link("pages/7_🧪_Monte_Carlo.py", label="🧪 Monte Carlo", icon="🧪")
    st.page_link("pages/8_🚨_Incident_Log.py", label="🚨 Incident Log", icon="🚨")
    st.page_link("pages/9_🔧_Settings.py", label="🔧 Settings", icon="🔧")
    st.markdown("---")
    st.caption("Built to run locally (localhost) in your browser via Streamlit.")

st.title("🏠 Dashboard")
st.write("Welcome to **Risk Analyst Pro** — a practical, advanced, and easy‑to‑use tool for analysts.")

col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Open Risks", "—")
with col2: st.metric("High Risks", "—")
with col3: st.metric("Assets", "—")
with col4: st.metric("Vendors", "—")

st.markdown("""
### What you can do here
- Record assets, threats, controls, vendors, and incidents
- Calculate risk with T×V×C (likelihood, vulnerability, consequence)
- Visualize a 5×5 heatmap and export reports
- Run Monte Carlo to estimate Probable Maximum Loss (basic)
- Map risks to frameworks (ISO 27001, NIST CSF, etc.)
""")

st.info("Use the sidebar to open each workspace. Add some assets and threats first, then calculate risks!")

# Footer
st.markdown("""
<hr/>
<div style='font-size:14px; opacity:0.8'>
<b>Created by:</b> {owner} | <b>Email:</b> {email} | <b>Website:</b> <a href='{site}' target='_blank'>{site}</a>
</div>
""".format(owner=cfg.get("owner_name",""), email=cfg.get("owner_email",""), site=cfg.get("owner_website","")), unsafe_allow_html=True)


st.markdown("""
<hr/>
<div style='font-size:14px; line-height:1.6'>
  <b>Let's Connect</b><br/>
  Email: <a href='mailto:raoanveeksh@gmail.com'>raoanveeksh@gmail.com</a><br/>
  Phone: +1 (617) 840-8538<br/>
  LinkedIn: <a href='https://www.linkedin.com/in/anveekshmrao' target='_blank'>linkedin.com/in/anveekshmrao</a><br/>
  <br/>
  <b>Privacy &amp; Policy</b><br/>
  &copy;2022 by Cyber Tech Associates. Proudly created with Cyber Tech Associates.
</div>
""", unsafe_allow_html=True)
