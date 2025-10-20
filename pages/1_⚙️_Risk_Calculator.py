
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import text
from utils import get_engine, load_config, init_db

st.title("⚙️ Risk Calculator")
cfg = load_config()
engine = get_engine()
init_db(engine)

levels = cfg.get("risk_matrix_levels", [1,2,3,4,5])

with engine.connect() as conn:
    assets = pd.read_sql(text("SELECT id, name, criticality FROM assets"), conn)
    threats = pd.read_sql(text("SELECT id, name FROM threats"), conn)

col = st.columns(2)
with col[0]:
    asset = st.selectbox("Asset", assets["name"].tolist() if len(assets)>0 else [])
with col[1]:
    threat = st.selectbox("Threat", threats["name"].tolist() if len(threats)>0 else [])

l,v,c = st.columns(3)
with l: likelihood = st.slider("Likelihood (T)", min_value=min(levels), max_value=max(levels), value=3)
with v: vulnerability = st.slider("Vulnerability (V)", min_value=min(levels), max_value=max(levels), value=3)
with c: consequence = st.slider("Consequence (C)", min_value=min(levels), max_value=max(levels), value=3)

risk = likelihood * vulnerability * consequence
st.metric("Risk score (T×V×C)", f"{risk}")

# Heatmap (matplotlib, single plot, no specific colors)
fig, ax = plt.subplots()
matrix = np.outer(levels, levels)
ax.imshow(matrix)
ax.set_title("5×5 Risk Heatmap (V vs T)")
ax.set_xlabel("Vulnerability (V)")
ax.set_ylabel("Likelihood (T)")
ax.set_xticks(range(len(levels)))
ax.set_xticklabels(levels)
ax.set_yticks(range(len(levels)))
ax.set_yticklabels(levels)
st.pyplot(fig)

notes = st.text_area("Mitigation / Notes", placeholder="Add proposed controls or plan…")

if st.button("➕ Add to Risk Register"):
    if len(assets)==0 or len(threats)==0 or asset=="" or threat=="":
        st.warning("Please add at least one asset and one threat first.")
    else:
        asset_id = int(assets.loc[assets['name']==asset, 'id'].iloc[0])
        threat_id = int(threats.loc[threats['name']==threat, 'id'].iloc[0])
        with engine.begin() as conn:
            conn.exec_driver_sql(
                "INSERT INTO risks (asset_id, threat_id, likelihood, vulnerability, consequence, risk_score, mitigation) VALUES (?,?,?,?,?,?,?)",
                (asset_id, threat_id, likelihood, vulnerability, consequence, risk, notes or "")
            )
        st.success("Saved to Risk Register!")
