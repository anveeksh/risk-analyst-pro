
import streamlit as st
import pandas as pd
from sqlalchemy import text
from utils import get_engine, init_db

st.title("📦 Vendor Risk")
engine = get_engine()
init_db(engine)

name = st.text_input("Vendor Name")
service = st.text_input("Service / Product")
criticality = st.slider("Vendor Criticality", 1, 5, 3)
risk_notes = st.text_area("Risk Notes")

if st.button("➕ Add Vendor"):
    with engine.begin() as conn:
        conn.exec_driver_sql(
            "INSERT INTO vendors (name, service, criticality, risk_notes) VALUES (?,?,?,?)",
            (name, service, criticality, risk_notes)
        )
    st.success("Vendor added.")

with engine.connect() as conn:
    df = pd.read_sql(text("SELECT * FROM vendors ORDER BY criticality DESC"), conn)
st.dataframe(df, use_container_width=True)
