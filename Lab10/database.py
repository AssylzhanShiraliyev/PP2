import psycopg2

def connect_to_db(db_name):
    """Establish connection to PostgreSQL database"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user="postgres",
            password="your_password"  # Replace with your password
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def create_phonebook_table(conn):
    """Create phonebook table if it doesn't exist"""
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50),
                phone VARCHAR(20) NOT NULL UNIQUE
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"Table creation error: {e}")
