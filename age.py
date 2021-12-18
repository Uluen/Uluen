# Goal: Learn stuff
# ToDo: check input


from datetime import date
today = date.today()


print("Hullo!")

fname = input("Firstname: ")
lname = input("Lastname: ")
bdate = int(input("Born (YYYY): "))


age = int(today.year - bdate)

print(fname + ", you're", age, "years old!")

# is this synced?