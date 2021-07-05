from replit import db

# PAUL server!!1! XDDD

print("Welcome to the Paul Server.")
print(" ")
print("How would you like to modify the DB?")
print(" ")
print("(1) Add value (type 'add')")
print("(2) Delete value (type 'del')")
print("(3) List all keys (type 'list')")
print("(4) get a value from a key (type 'view')")

val = input("Enter: ")

if val == "add":
  print(" ")
  key = input("Key: ")
  value = input("Value: ")
  db[key] = value
elif val == "del":
  print(" ")
  delkey = input("Key: ")
  del db[delkey]
elif val == "list":
  allkeys = db.keys() 
  print(allkeys)
elif val == "view":
  v_keyval = input("Key: ")
  keyvalue = db[v_keyval]
  print(keyvalue)

# Thx for using paul server!!!1 XD