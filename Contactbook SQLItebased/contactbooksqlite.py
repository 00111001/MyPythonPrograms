# Working with Database

# cur.execute('''CREATE TABLE contacts(Name text, Lastname text, Number text)''')
import sqlite3

try:
    # Connect / Create (If not exists) Database
    con = sqlite3.connect("contacts.db")
    # create a Cursor  object and call its execute() method to perform SQL commands
    cur = con.cursor()
except sqlite3.Error as e:
    # Display Msg + Error
    print("An error occurred:", e.args[0])


# Shows us all Users in our Server
def kontakte_anzeigen():
    # iterate through DB to print every Row (Every User)
    for row in cur.execute('SELECT * FROM contacts ORDER BY Name'):
        print(row)


def kontakte_hinzufuegen():
    Name_to_add = input("Enter Name of Friend: ")
    Lastname_to_add = input("Enter Lastname of Friend: ")
    Number = input('Enter Number of your Contact')
    params = (Name_to_add, Lastname_to_add, Number)
    cur.execute(f"INSERT INTO contacts VALUES (?,?,?)", params)
    # Save (commit) the changes
    con.commit()
    con.close
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed, or they will be lost.


def kontakt_loeschen():
    Name_to_del = str(input("Enter Name of your Friend  "))
    con.execute(f"delete from contacts where Name = (?)", (Name_to_del,))
    con.commit()

def main_menu():
    while True:
        print("""(1) Show Users
            2) Add User
            (3) Delete User
            (0) Exit""")

        menu_auswahl = input("Was willst du tun? ")

        if menu_auswahl == '1':
            kontakte_anzeigen()
        elif menu_auswahl == '2':
            kontakte_hinzufuegen()
        elif menu_auswahl == '3':
            kontakt_loeschen()
        elif menu_auswahl == '0':
            exit()


if __name__ == '__main__':
    main_menu()
