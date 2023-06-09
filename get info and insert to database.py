import mysql.connector #library for connect mysql to python

print('connecting to database...')

cnx = mysql.connector.connect(user='name_server', password='password',  #enter information of database
                              host='ip_server',
                              database='name_database')
print('connected to database')
cursor = cnx.cursor()

information_user = input('please type your name : ') # to get information from users
information_user2 = input('please type your lastname : ')
information_user3 = int(input('please type your weight : '))
information_user4 = int(input('please type your high : '))

data_user = (information_user , information_user2 , information_user3 , information_user4)

#insert information users to the database
add_user = """INSERT INTO information_table(  
   firstname ,lastname ,weight ,high )
   VALUES (%s,%s,%s,%s)"""

cursor.execute(add_user , data_user)
cnx.commit()

print('user information increase database\ninformation: %s , %s , %s , %s' %(information_user , information_user2 , information_user3 , information_user4))
 #sort entered information by some data example high   
sql = "SELECT * FROM information_table ORDER BY high"
cursor.execute(sql)
myresult = cursor.fetchall()
#print all of the data of database sorted
for x in myresult:
    print(x)

#disconected from database 
cnx.close()
