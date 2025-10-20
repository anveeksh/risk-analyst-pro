
import streamlit as st
import json
from utils import load_config

st.title("🔧 Settings")

cfg = load_config()
st.write("Update footer/contact info and matrix levels. These changes save to **config.json** in your project folder.")

with st.form("cfg"):
    app_name = st.text_input("App Name", cfg.get("app_name","Risk Analyst Pro"))
    owner_name = st.text_input("Owner/Creator Name", cfg.get("owner_name",""))
    owner_email = st.text_input("Owner Email", cfg.get("owner_email",""))
    owner_website = st.text_input("Owner Website", cfg.get("owner_website",""))
    levels_str = st.text_input("Risk Matrix Levels (comma-separated)", ",".join(map(str, cfg.get("risk_matrix_levels",[1,2,3,4,5]))))
    min_sim = st.number_input("Minimum similarity threshold (for future matching features)", 0.0, 1.0, cfg.get("min_similarity_threshold",0.65), 0.01)
    submitted = st.form_submit_button("💾 Save")
    if submitted:
        try:
            levels = [int(x.strip()) for x in levels_str.split(",") if x.strip().isdigit()]
            cfg.update({
                "app_name": app_name,
                "owner_name": owner_name,
                "owner_email": owner_email,
                "owner_website": owner_website,
                "risk_matrix_levels": levels,
                "min_similarity_threshold": float(min_sim)
            })
            with open("config.json","w") as f:
                json.dump(cfg, f, indent=2)
            st.success("Saved. Reload the page to see changes.")
        except Exception as e:
            st.error(f"Failed to save: {e}")
