import sqlite3 as lite


# functionality goes here
class DatabaseManage(object):
    
    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")         
        except Exception:
            print("unable to create a Db !")
            
    #TODO create data          
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data)
                return True
        except Exception:
            return False

    #todo fetch data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    #todo delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM course where id = ?", [id])
                return True
        except Exception:
            return False



#TODO provide interface to user


def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT :: \n")
    print("*"*40)
    
    
    db = DatabaseManage()
    
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("#"*40)
    print("\n")
    
    print("1. Insert a new course")
    print("2. Show all courses")
    print("3. Delete a course (id required)")
    print("#"*40)
    
    choice = input("\n Enter a choice: ")
    
    if choice == "1":
        name = input("\n Enter course name: \n")
        description = input("\n Enter course description: \n")
        price = input("\n Enter price: \n")
        private  = input("\n Is this private(0/1): \n")
    
        if db.insert_data([name, description, price, private]):
            print("Data Successfully Inserted")
        else:
            print("Oops! something went wrong")
    
    
    elif choice == "2":
        print("\n:: Course List ::")
        
        for index, item in enumerate(db.fetch_data()):
            print("\nserial no :", (index+1))
            print("course id : ", item[0]) 
            print("course Name : ", item[1])
            print("course Description : ", item[2])
            print("course Price : ", item[3])
            private = "Yes" if item[4] else "No"
            print("Is private", private)
            print("\n")
            
    elif choice == "3":
        record_id = input("Hey please enter the course id to delete: ")
        
        if db.delete_data(record_id):
            print("Course was deleted with a success")
        else:
            print("Oops ! something went wrong")
        
    else:
        print("\n BAD CHOICE")                 
        
        
if __name__ == '__main__':
    main()