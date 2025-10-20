
import streamlit as st
import pandas as pd
from sqlalchemy import text
from utils import get_engine, init_db

st.title("🚨 Incident Log")
engine = get_engine()
init_db(engine)

title = st.text_input("Incident Title")
severity = st.slider("Severity (1-5)", 1, 5, 3)
occurred_on = st.date_input("Occurred On")
summary = st.text_area("Summary")
impacted_assets = st.text_input("Impacted Assets (comma-separated)")

if st.button("➕ Add Incident"):
    with engine.begin() as conn:
        conn.exec_driver_sql(
            "INSERT INTO incidents (title, severity, occurred_on, summary, impacted_assets) VALUES (?,?,?,?,?)",
            (title, severity, str(occurred_on), summary, impacted_assets)
        )
    st.success("Incident recorded.")

with engine.connect() as conn:
    df = pd.read_sql(text("SELECT * FROM incidents ORDER BY occurred_on DESC"), conn)
st.dataframe(df, use_container_width=True)
