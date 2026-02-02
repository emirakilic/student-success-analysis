import pyodbc

SERVER = r"localhost\SQLEXPRESS01"
DATABASE = "StudentSuccessDB"

def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

