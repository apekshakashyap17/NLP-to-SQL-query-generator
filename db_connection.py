from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
from connections_variable import username, password

DB_USER = username# put your own database username
DB_PASSWORD = quote_plus(password) # input your own password
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = "llm2sql"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # avoids stale connections
)

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            print("✅ Database connected:", result.fetchone())
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_connection()
