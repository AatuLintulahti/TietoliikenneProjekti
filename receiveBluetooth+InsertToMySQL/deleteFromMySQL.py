import mysql.connector


mydb = mysql.connector.connect(
  host="172.20.241.9",
  user="dbaccess_rw",
  password="fasdjkf2389vw2c3k234vk2f3",
  database="measurements"
)
mycursor = mydb.cursor()

print(mydb) 

sql = "DELETE FROM rawdata WHERE groupid = '12'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
