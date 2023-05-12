import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gmail_db"
)

# Create the table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE emails (id INT AUTO_INCREMENT PRIMARY KEY, thread_id VARCHAR(255), subject VARCHAR(255), sender VARCHAR(255), recipient VARCHAR(255), message VARCHAR(1000), received_date DATETIME)")

# Insert some data
sql = "INSERT INTO emails (thread_id, subject, sender, recipient, message, received_date) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("thread_id_1", "Subject 1", "sender1@example.com", "recipient1@example.com", "This is the message body", "2022-05-12 00:00:00")
mycursor.execute(sql, val)

val = ("thread_id_2", "Subject 2", "sender2@example.com", "recipient2@example.com", "This is another message body", "2022-05-13 00:00:00")
mycursor.execute(sql, val)

mydb.commit()

# Retrieve the data
mycursor.execute("SELECT * FROM emails")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

