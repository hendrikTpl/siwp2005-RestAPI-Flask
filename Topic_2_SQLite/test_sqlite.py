from sqlite_database import create_table, insert_user, get_users, get_user_by_id, update_user, delete_user

def main():
    create_table()

    while True:
        print("\nSQLite CRUD Operations")
        print("1. Insert User")
        print("2. Display Users")
        print("3. Get User by ID")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            insert_user(name, email, age)
            print("User inserted successfully!")

        elif choice == '2':
            users = get_users()
            print("\nUser List:")
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

        elif choice == '3':
            user_id = int(input("Enter user ID: "))
            user = get_user_by_id(user_id)
            if user:
                print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")
            else:
                print("User not found!")

        elif choice == '4':
            user_id = int(input("Enter user ID: "))
            name = input("Enter new name: ")
            email = input("Enter new email: ")
            age = int(input("Enter new age: "))
            update_user(user_id, name, email, age)
            print("User updated successfully!")

        elif choice == '5':
            user_id = int(input("Enter user ID: "))
            delete_user(user_id)
            print("User deleted successfully!")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
