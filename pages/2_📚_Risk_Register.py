
import streamlit as st
import pandas as pd
from sqlalchemy import text
from utils import get_engine, df_to_csv_download, init_db

st.title("📚 Risk Register")
engine = get_engine()
init_db(engine)

with engine.connect() as conn:
    df = pd.read_sql(text("""
    SELECT r.id, a.name as asset, t.name as threat, r.likelihood, r.vulnerability, r.consequence, r.risk_score, r.status, r.owner, r.mitigation, r.review_date
    FROM risks r
    LEFT JOIN assets a ON a.id = r.asset_id
    LEFT JOIN threats t ON t.id = r.threat_id
    ORDER BY r.risk_score DESC
    """), conn)

st.dataframe(df, use_container_width=True)

if len(df) > 0:
    filename, bytes_data = df_to_csv_download(df, "risk_register.csv")
    st.download_button("⬇️ Download CSV", bytes_data, file_name=filename, mime="text/csv")

with st.expander("✏️ Update / Close a Risk"):
    rid = st.number_input("Risk ID", min_value=1, step=1)
    status = st.selectbox("Status", ["Open","In Progress","Mitigated","Accepted","Closed"])
    owner = st.text_input("Risk Owner")
    review_date = st.date_input("Next Review Date")
    mitigation = st.text_area("Mitigation / Notes")

    if st.button("💾 Save Changes"):
        with engine.begin() as conn:
            conn.exec_driver_sql(
                "UPDATE risks SET status=?, owner=?, review_date=?, mitigation=? WHERE id=?",
                (status, owner, str(review_date), mitigation, int(rid))
            )
        st.success("Updated.")
