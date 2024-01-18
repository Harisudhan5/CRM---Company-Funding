import mysql.connector
def check_credentials(username, password):
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="your_database"
        )

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Define the query to check the username and password
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        values = (username, password)

        # Execute the query
        cursor.execute(query, values)

        # Fetch the result
        result = cursor.fetchone()

        # Close the cursor and the connection
        cursor.close()
        connection.close()

        # Check if a row with the given username and password was found
        if result:
            return "Login successful"
        else:
            return "Invalid username or password"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Input username and password from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check the credentials and print the result
    result = check_credentials(username, password)
    print(result)