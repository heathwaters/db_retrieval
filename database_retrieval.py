import psycopg2

# Database connection parameters
db_name = "tournament_data"
db_user = "heathwatersnew"
db_password = "Tenni$777"
db_host = "localhost"
db_port = "5432"

# SQL query to retrieve data (adjust the query to match your actual table and column names)
query = "SELECT * FROM tournament_points;"

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor object
cur = conn.cursor()

# Execute the query
cur.execute(query)

# Fetch all the results
data = cur.fetchall()

# Close the cursor and connection
cur.close()
conn.close()

# Print the data (or process it as needed)
for row in data:
    print(row)