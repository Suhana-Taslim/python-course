import sqlite3

def create_and_list_tables(db_path):
    conn = sqlite3.connect(db_path)
    try:
        cursor = conn.cursor()
        # Create a sample table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                country TEXT
            )
        """)
        conn.commit()
        # List all user-defined tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;")
        tables = [row[0] for row in cursor.fetchall()]
        return tables
    finally:
        conn.close()

if __name__ == "__main__":
    db_file = "sample.db"
    tables = create_and_list_tables(db_file)
    if tables:
        print("Tables present in database:")
        for t in tables:
            print(f" • {t}")
    else:
        print("No tables found.")
