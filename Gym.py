import os , time ,sqlite3



def clear_scr():
    os.system("cls" if os.name=="nt" else "clear")
# تشغيل قاعده البيانات
db = sqlite3.connect("mianData.db")
# عمل المؤشر
cr = db.cursor()

def create_database():
    try:
        #عمل جداول البيانات
        cr.execute("create table if not exists users (user_id integer, first_name text, last_name text,status text,phone text)")
        cr.execute(f"select * from users")
        return cr.fetchall()
    except sqlite3.Error as ee:
        print(f"Error Reading Datat {ee}")
    finally:
        # save data
        db.commit()
        # Close Database Connection
        #db.close()
def display_member(ind):
    print(f"Displaying all members ....\nMembership ID: {ind[0]}\nFirst Name: {ind[1]}\nLast Name: {ind[2]}\nMembership Status: {ind[3]}\nMember phone: {ind[4]}")
    print("-" * 60)
def info_member(id):
    for i,e in enumerate(member_list):
        if e[0]==id:
            print("-" * 60)
            print(f"Membership ID: {e[0]}\nFirst Name: {e[1]}\nLast Name: {e[2]}\nMembership Status: {e[3]}\nMember phone: {e[4]}")
            print("-" * 60)
def create_member():
    member_id = input("Enter membership ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    status = input("Enter membership status, Or click enter: ")
    phone = input("Enter your phone: ")
    print("Member added successfully!")
    try:
        cr.execute(f"insert into users(user_id, first_name, last_name, status,phone ) values({member_id},'{first_name}','{last_name}','{status}','{phone}')")
        # اضافه البيانات الي متغير لست
        cr.execute(f"select * from users")

    except sqlite3.Error as ee:
        print(f"Error Reading Datat {ee}")
    finally:
        # save data
        db.commit()
        # Close Database Connection
        db.close()
member_list = []
def update_data():
    global member_list
    member_list = create_database()
def search():
    print("""Search by:
    1.Membership ID
    2.First Name
    3.Membership Status
    """)
    choice_search = input("Enter your choice: ")
    if choice_search == '1':
        while True:
            enter1 = int(input("Enter the Membership ID to search: "))
            for i,e in enumerate(member_list) :
                if member_list[i][0] == enter1:
                    display_member(e)
            continue_inp = input("if you want to search again press (y/n): ")
            if continue_inp =="y":
                search()
            else:
                break
            # print("not found.....")
            # time.sleep(2)
            # break
    elif choice_search == '2':
        clear_scr()
        while True:
            enter2 = input("Enter the first name to search: ")
            for i,e in enumerate(member_list):
                if member_list[i][1] == enter2:
                    display_member(e)
            continue_inp = input("if you want to search again press (y/n): ")
            if continue_inp == "y":
                search()
            else:
                break
    elif choice_search == '3':
        clear_scr()
        while True:
            enter3 = input("Enter the Membership Status to search: ")
            for i, e in enumerate(member_list):
                if member_list[i][3] == enter3:
                    display_member(e)
            continue_inp = input("if you want to search again press (y/n): ")
            if continue_inp == "y":
                search()
            else:
                break
    else:
        print("WRONG CHOICE!")
        time.sleep(3)
        clear_scr()
        search()
def edite_member():
    clear_scr()
    id_member = int(input("Enter the ID number of the member you want to edite : "))
    print("the information of the member you want to edit is: ")
    info_member(id_member)
    print("""chose the number of element you want to edite:
            1.Membership ID
            2.First Name
            3.Last Name
            4.Membership Status
            5.Phone number
            """)
    choice_edite = input("Enter your choice: ")
    if choice_edite == '1':
        new_value = int(input("Enter the new value: "))
        cr.execute(f"update users set user_id = {new_value} where user_id = {id_member}")
        print("Edite successfully.!")
        time.sleep(2)
    elif choice_edite == '2':
        clear_scr()
        new_value = input("Enter the new value: ")
        cr.execute(f"update users set first_name = '{new_value}' where user_id = {id_member}")
        print("Edite successfully.!")
        time.sleep(2)
    elif choice_edite == '3':
        new_value = input("Enter the new value: ")
        cr.execute(f"update users set last_name = '{new_value}' where user_id = {id_member}")
        print("Edite successfully.!")
        time.sleep(2)
    elif choice_edite == '4':
        new_value = input("Enter the new value: ")
        cr.execute(f"update users set status = '{new_value}' where user_id = {id_member}")
        print("Edite successfully.!")
        time.sleep(2)
    elif choice_edite == '5':
        new_value = input("Enter the new value: ")
        cr.execute(f"update users set phone = '{new_value}' where user_id = {id_member}")
        print("Edite successfully.!")
        time.sleep(2)
    else:
        print("WRONG CHOICE!")
        time.sleep(3)
        clear_scr()
        db.close()
        edite_member()

def delet_member():
    pass
while True:
    update_data()
    #clear_scr()
    print("""Welcome to Gym Membership Management
    Choose an Action:
    1. Add new member
    2. Display all members
    3. Search for a member
    4. Edit a member
    5. Delete a member
    6. Exit
    """)
    enter_choice = input("Enter your choice: ")
    if enter_choice == "1":
        clear_scr()
        create_member()
    elif enter_choice == "2":
        clear_scr()
        for i in member_list:
            display_member(i)
    elif enter_choice == "3":
        clear_scr()
        search()
    elif enter_choice == "4":
        clear_scr()
        edite_member()
    elif enter_choice == "5":
        clear_scr()
        delet_member()
    elif enter_choice == "6":
        break
    else:
        print("Wrong Choice!!")
db.close()
print("this is a new user ")