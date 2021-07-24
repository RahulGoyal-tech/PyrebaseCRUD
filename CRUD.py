import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDIMxV2cqA26DuDb8smqPo2LVgiLyupRnc",
    'authDomain': "pyrebase-e83fb.firebaseapp.com",
    'databaseURL':"https://pyrebase-e83fb-default-rtdb.firebaseio.com/",
    'projectId': "pyrebase-e83fb",
    'storageBucket': "pyrebase-e83fb.appspot.com",
    'messagingSenderId': "854606615501",
    'appId': "1:854606615501:web:ef3fe85797246f25de2a84"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Database consist of information of name, age and address

# Create
# Creating dummy data
print("########## Creating Data ##########")
inp = input("Enter no. of entries ")
for i in range(int(inp)):
    name = input("Enter Your Name ")
    age = input("Enter Your Age ")
    address = input("Enter the state you live in ")
    data={'name':name,'age':age, 'address':address}
    try:
        db.child("People").child("ID"+str(i+1)).set(data)
        print("Database addition successful")
    except:
        print("Databse creation not successful")

# Read
# Reading in all data
print("########## Reading Data ##########")
People = db.child("People").get()
for person in People.each():
    print(person.val())
    print(person.key())

# Update
# Updating selected data
print("########## Updating Data ##########")
uid = input("Enter Unique ID of data to be updated ")
fld = input("Enter data field to be updated ")
value = input("Enter new value of data field ")
try:    
    db.child("People").child(str(uid)).update({str(fld):str(value)})
    print('Update Successful')
except:
    print("Update not successful")

#Reading Updated Data filtered by Unique ID
print("########## Reading Data ##########")
uid = input("Enter UID to print ")
People = db.child("People").get()
for person in People.each():
    if person.key()==uid:
        print(person.val())

# Delete
# Deleting selected data
print("########## Deleting Data ##########")
uid = input("Enter id from which you want to delete data ")
fld = input("Enter field which you want to delete ")
try:
    db.child("People").child(str(uid)).child(str(fld)).remove()
    print("Deletion Successful")
except:
    print("Field Does Not Exist")

# Reading the data
print("########## Reading Data ##########")
People = db.child("People").get()
for person in People.each():
    print(person.val())
    print(person.key())
