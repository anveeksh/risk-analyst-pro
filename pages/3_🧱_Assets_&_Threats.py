
import streamlit as st
import pandas as pd
from sqlalchemy import text
from utils import get_engine, init_db

st.title("🧱 Assets & Threats")
engine = get_engine()
init_db(engine)

tab1, tab2 = st.tabs(["Assets", "Threats"])

with tab1:
    st.subheader("Assets")
    name = st.text_input("Asset Name")
    owner = st.text_input("Owner / Custodian")
    category = st.selectbox("Category", ["Application","Data","Device","Facility","Network","People","Process"])
    criticality = st.slider("Business Criticality", 1, 5, 3)
    notes = st.text_area("Notes")
    if st.button("➕ Add Asset"):
        with engine.begin() as conn:
            conn.exec_driver_sql(
                "INSERT INTO assets (name, owner, category, criticality, notes) VALUES (?,?,?,?,?)",
                (name, owner, category, criticality, notes)
            )
        st.success("Asset added.")

    with engine.connect() as conn:
        a_df = pd.read_sql(text("SELECT * FROM assets ORDER BY criticality DESC"), conn)
    st.dataframe(a_df, use_container_width=True)

with tab2:
    st.subheader("Threats")
    t_name = st.text_input("Threat Name")
    vector = st.text_input("Vector (e.g., Phishing, Ransomware, DDoS)")
    desc = st.text_area("Description")
    if st.button("➕ Add Threat"):
        with engine.begin() as conn:
            conn.exec_driver_sql(
                "INSERT INTO threats (name, vector, description) VALUES (?,?,?)",
                (t_name, vector, desc)
            )
        st.success("Threat added.")

    with engine.connect() as conn:
        t_df = pd.read_sql(text("SELECT * FROM threats ORDER BY id DESC"), conn)
    st.dataframe(t_df, use_container_width=True)
