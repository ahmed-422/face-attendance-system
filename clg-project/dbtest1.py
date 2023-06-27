import mysql.connector
import pickle

# Connect to MySQL server
cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='attendance')

# Create a cursor object
cursor = cnx.cursor()

# Load encodings from pickle file
with open('known_face_encodings.pickle', 'rb') as f:
    encodings = pickle.load(f)

# Insert encodings into the database
query = "INSERT INTO encodings (encoding) VALUES (%s)"
for encoding in encodings:
    values = (encoding.tobytes(),)
    cursor.execute(query, values)

# Commit changes to the database
cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()
