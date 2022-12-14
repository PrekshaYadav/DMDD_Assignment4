import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Sh_reyasi03")
mycursor = mydb.cursor()

mycursor.execute("Use assignment3")

#Create table commands
mycursor.execute("Create Table University(University_ID int NOT NULL, University_Name VARCHAR(2555), Country VARCHAR(2555), Chance_of_Admit numeric(9,2), University_Rating int, National_Rank int, PRIMARY KEY (University_ID))")
mycursor.execute("Create Table Standards(University_ID int NOT NULL, Quality_of_Education int NOT NULL, Quality_of_Faculty int, Alumni_Employement int, Patent int, FOREIGN KEY (University_ID) REFERENCES University(University_ID))")
mycursor.execute("Create Table Requirements(University_ID int NOT NULL, Academic_Year int NOT NULL, Score int, GRE int, TOEFL int, SOP numeric(9,2), LOR numeric(9,2), CGPA numeric(9,2), Research int, FOREIGN KEY (University_ID) REFERENCES University(University_ID))")

print("Schema Created")