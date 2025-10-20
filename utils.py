
import os
import json
import pandas as pd
from typing import Tuple
from sqlalchemy import create_engine

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), "risk_db.sqlite")

def get_engine(db_path: str = DEFAULT_DB_PATH):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    engine = create_engine(f"sqlite:///{db_path}", echo=False, future=True)
    return engine

def load_config() -> dict:
    cfg_path = os.path.join(os.getcwd(), "config.json")
    if not os.path.exists(cfg_path):
        cfg = {
            "app_name": "Risk Analyst Pro",
            "owner_name": "Anveeksh Mahesh Rao",
            "owner_email": "your-email@example.com",
            "owner_website": "https://www.anveekshmrao.com",
            "risk_matrix_levels": [1,2,3,4,5],
            "min_similarity_threshold": 0.65
        }
        with open(cfg_path, "w") as f:
            json.dump(cfg, f, indent=2)
        return cfg
    with open(cfg_path, "r") as f:
        return json.load(f)

def init_db(engine):
    with engine.connect() as conn:
        conn.exec_driver_sql("""
        CREATE TABLE IF NOT EXISTS assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            owner TEXT,
            category TEXT,
            criticality INTEGER DEFAULT 3,
            notes TEXT
        );
        """)
        conn.exec_driver_sql("""
        CREATE TABLE IF NOT EXISTS threats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            vector TEXT,
            description TEXT
        );
        """)
        conn.exec_driver_sql("""
        CREATE TABLE IF NOT EXISTS risks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_id INTEGER,
            threat_id INTEGER,
            likelihood INTEGER,
            vulnerability INTEGER,
            consequence INTEGER,
            risk_score REAL,
            status TEXT DEFAULT 'Open',
            owner TEXT,
            mitigation TEXT,
            review_date TEXT,
            FOREIGN KEY(asset_id) REFERENCES assets(id),
            FOREIGN KEY(threat_id) REFERENCES threats(id)
        );
        """ )
        conn.exec_driver_sql("""
        CREATE TABLE IF NOT EXISTS controls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            framework TEXT,
            control_id TEXT,
            title TEXT,
            description TEXT
        );
        """ )
        conn.exec_driver_sql("""
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            service TEXT,
            criticality INTEGER DEFAULT 3,
            risk_notes TEXT
        );
        """ )
        conn.exec_driver_sql("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            severity INTEGER DEFAULT 3,
            occurred_on TEXT,
            summary TEXT,
            impacted_assets TEXT
        );
        """ )

def df_to_csv_download(df: pd.DataFrame, filename: str) -> Tuple[str, bytes]:
    csv_bytes = df.to_csv(index=False).encode('utf-8')
    return filename, csv_bytes
