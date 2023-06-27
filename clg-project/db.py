import mysql.connector
import pickle
import numpy as np

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="attendance"
)

# Read the encodings from a file
with open("class_names.pickle", "rb") as f:
    encodings = pickle.load(f)


# Convert the face encodings to bytes
encodings_bytes = [pickle.dumps(encoding) for encoding in encodings]

# Insert the encodings into the database
mycursor = mydb.cursor()
sql = "INSERT INTO encodings VALUES (%s)"
mycursor.execute(sql)
mydb.commit()



# Retrieve the encodings from the database
# mycursor.execute("SELECT name, encoding FROM encodings")
# results = mycursor.fetchall()

# Convert the encodings back to face encodings
# encodings = {}
# for name, result in results:
#     encoding = pickle.loads(result)
#     encodings[name] = encoding
