#using a python program read the table present in mysql database and save the content into the file on desktop
import mysql.connector
import csv
import os

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_restaurant"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM tb_menu") 
rows = cursor.fetchall()

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "C:\\Users\\91885\\OneDrive\\Desktop\\menu_data.csv")
with open(desktop_path, 'w', newline='',encoding='utf-8') as w:
    writer = csv.writer(w)
    writer.writerows(rows)
    w.flush()

print(f"Data has been saved to: {desktop_path}")
# print(rows)
cursor.close()
db.close()

