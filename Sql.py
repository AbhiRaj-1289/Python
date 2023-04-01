import pymysql
operations = {
    "1" : viewRecord,
    "2" : addRecord,
    "3" : updateRecord,
    "4" : deleteRecord
}
def dbconnection():
    global conn, cursor, result, rows
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Abhi@161891",
        database = "lnm_bca")
    cursor = conn.cursor()
def viewRecord():
    count = 0
    cursor.execute("SELECT * from Students")
    rows = cursor.fetchall()
    print("******____Student's Record----******\n")
def addRecord():
    fname = input("Enter Student's Name: ")
    while True:
        uname = input("Enter Username")
        search_qurey = f"SELECT * from Students where user_name = {uname}"
        cursor.execute(search_qurey)
        result = cursor.fetchall()
        if result:
            print("Username already taken, Please choose another!")
        else:
            count = 0
            sql = f'INSERT into students(name,user_name) values(\
                "{fname}","{uname}")'
            cursor.execute(sql)
            conn.commit()
            cursor.execute("SELECT * from students")
            rows = cursor.fetchall()
            print("\nRecord Added Successfully")
            for row in rows: 
                print(row)
                count += 1
                print("Total Record = ",count)
                break
def updateRecord():
    uname = input("Enter Username: ")
    query = f'SELECT * from students where user_name = {uname}'
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        fname = input("Enter Student's Name to Update: ")
        query = f'UPDATE students SET name = "{fname}"\
        WHERE user_name = "{uname}"'
        cursor.execute(query)
        conn.commit()
        print(f"\nRecord for {uname} Updated!")
    else:
        print("\nUsername not Found...!")
def deleteRecord():
    uname = input("Enter Username: ")
    query = f'DELETE FROM students WHERE user_name = {uname}'
    cursor.execute(query)
    conn.commit()
    if cursor.rowcount > 0:
        print(f"\n{cursor.rowcount} deleted")
    else:
        print(f"{uname} not found...!")
dbconnection()
while True:
    print("Select a CRUD Operations")
    print("1. View Records")
    print("2. Update Reord")
    print("3. Delete Record")
    print("4. Exit..!")
    print("\n")
    choice = input("Enter Your Choice (1/2/3/4):")
    if choice == 4:
        cursor.close()
        conn.close()
        break
    elif choice == 1:
        viewRecord()
    elif choice == 2:
        updateRecord()
    elif choice == 3:
        deleteRecord()
    elif choice == 5:
        break
