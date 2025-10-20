
import streamlit as st
import pandas as pd
from sqlalchemy import text
from utils import get_engine, df_to_csv_download, init_db

st.title("📄 Reports & Exports")
engine = get_engine()
init_db(engine)

with engine.connect() as conn:
    risks = pd.read_sql(text("""
    SELECT r.id, a.name as asset, t.name as threat, r.likelihood, r.vulnerability, r.consequence, r.risk_score, r.status, r.owner, r.mitigation, r.review_date
    FROM risks r
    LEFT JOIN assets a ON a.id = r.asset_id
    LEFT JOIN threats t ON t.id = r.threat_id
    ORDER BY r.risk_score DESC
    """), conn)
    assets = pd.read_sql(text("SELECT * FROM assets"), conn)
    vendors = pd.read_sql(text("SELECT * FROM vendors"), conn)
    controls = pd.read_sql(text("SELECT * FROM controls"), conn)

st.subheader("Quick summaries")
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Total Risks", len(risks))
with col2: st.metric("High (≥50)", int((risks['risk_score']>=50).sum()) if len(risks)>0 else 0)
with col3: st.metric("Assets", len(assets))
with col4: st.metric("Vendors", len(vendors))

st.markdown("---")
st.subheader("Export tables")
for label, df in [("Risk Register", risks), ("Assets", assets), ("Vendors", vendors), ("Controls", controls)]:
    st.write(f"**{label}**")
    st.dataframe(df, use_container_width=True)
    if len(df) > 0:
        fname, bytes_data = df_to_csv_download(df, f"{label.lower().replace(' ','_')}.csv")
        st.download_button(f"⬇️ Download {label}", bytes_data, file_name=fname, mime="text/csv")
