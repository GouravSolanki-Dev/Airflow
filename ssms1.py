import pyodbc

# Connect to the SSMS server
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-I8QHF1P\GOURAV;DATABASE=mitel;UID=sa;Pwd=123')

# Create a cursor object
cursor = conn.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM issues')

# Fetch all results from the cursor
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
