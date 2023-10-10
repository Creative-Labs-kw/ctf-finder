import psycopg2
from psycopg2 import extras
import pyperclip

def connect_to_postgresql(host, port, username, password, database):
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=username,
            database=database,
            password=password
        )
        return connection
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def fetch_table_data(connection, table_name):
    try:
        # Create a cursor object with RealDictCursor
        cursor = connection.cursor(cursor_factory=extras.RealDictCursor)

        # Execute an SQL query to retrieve all data from the specified table
        cursor.execute(f"SELECT * FROM {table_name};")

        # Fetch all the results as dictionaries
        data = cursor.fetchall()

        # Get column names
        column_names = data[0].keys() if data else []

        # Close the cursor
        cursor.close()

        return data, column_names
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return None, None

def fetch_all_tables(connection):
    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Execute an SQL query to retrieve a list of all tables in the public schema
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)

        # Fetch all the table names
        table_names = [row[0] for row in cursor.fetchall()]

        # Close the cursor
        cursor.close()

        return table_names
    except Exception as e:
        print(f"Error executing SQL query: {e}")
        return []

def display_table(data, column_names):
    if data:
        print("Data in the specified table:")
        if column_names:
            print("\t".join(column_names))
        for row in data:
            values = [str(row[column_name]) for column_name in column_names]
            print("\t".join(values))
    else:
        print("No data found in the specified table.")

def search_for_ctf_in_table(data, column_names, table_name):
    found_ctf = False
    if data:
        for row in data:
            for column_name in column_names:
                cell_data = str(row[column_name])
                if "CTF" in cell_data:
                    print_and_copy_flag(cell_data)
                    found_ctf = True
    if not found_ctf:
        print(f"NOT Found 'CTF' in table: {table_name}, column: {', '.join(column_names)}")

def print_and_copy_flag(flag):
    formatted_flag = f"\033[1;33;1m{flag}\033[0m"
    print("-------------")
    print(formatted_flag)
    print("-------------")
    pyperclip.copy(formatted_flag)
    print("Flag copied to clipboard.")

if __name__ == "__main__":
    host = input("Enter the PostgreSQL host: ")
    port = input("Enter the PostgreSQL port: ")
    username = input("Enter the PostgreSQL username: ")
    database = input("Enter the PostgreSQL database name: ")
    password = input("Enter the PostgreSQL password: ")

    connection = connect_to_postgresql(host, port, username, password, database)
    
    if connection:
        table_names = fetch_all_tables(connection)
        for table_name in table_names:
            data, column_names = fetch_table_data(connection, table_name)
            print(f"Table: {table_name}")
            display_table(data, column_names)
            search_for_ctf_in_table(data, column_names, table_name)  # Search for 'CTF' in this table's data
    else:
        print("Failed to connect to the PostgreSQL server.")
