
import streamlit as st
import pandas as pd
from sqlalchemy import text
from utils import get_engine, init_db

st.title("🛡️ Controls Library")
engine = get_engine()
init_db(engine)

framework = st.selectbox("Framework", ["ISO 27001 Annex A", "NIST CSF 1.1/2.0", "NIST 800-53 rev5"])
control_id = st.text_input("Control ID (e.g., A.5.1, PR.AC-1)")
title = st.text_input("Title")
desc = st.text_area("Description")

if st.button("➕ Add Control"):
    with engine.begin() as conn:
        conn.exec_driver_sql(
            "INSERT INTO controls (framework, control_id, title, description) VALUES (?,?,?,?)",
            (framework, control_id, title, desc)
        )
    st.success("Control added.")

with engine.connect() as conn:
    df = pd.read_sql(text("SELECT * FROM controls ORDER BY framework, control_id"), conn)

st.dataframe(df, use_container_width=True)
