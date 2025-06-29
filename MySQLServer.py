import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',    # Replace with your MySQL username
            password=''     # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database without checking if it exists first (no SELECT/SHOW needed)
            try:
                cursor.execute("CREATE DATABASE alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as e:
                if e.errno == 1007:  # Database already exists error code
                    print("Database 'alx_book_store' already exists.")
                else:
                    raise
            
    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()