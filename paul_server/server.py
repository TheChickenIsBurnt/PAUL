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
print("(5) Create a file with data inside (type 'create') ")

val = input("Enter: ")

if val == "add":
  print(" ")
  key = input("Key: ")
  value = input("Value: ")
  db[key] = value
  print("Created key " + key + " with value " + value + ".")
elif val == "del":
  print(" ")
  delkey = input("Key: ")
  del db[delkey]
  print("deleted key " + delkey + ".")
elif val == "list":
  allkeys = db.keys() 
  print(allkeys)
elif val == "view":
  v_keyval = input("Key: ")
  keyvalue = db[v_keyval]
  print(keyvalue)
elif val == "create":
  fname = input("File name: ")
  fexte = input("File Extension: ")
  fcont = input("File Contents: ")
  f = open(fname + "." + fexte, "x")
  f.write(fcont)
  f.close()
  print("Created file " + fname + "." + fexte + " with contents '" + fcont + "'.")

# Thx for using paul server!!!1 XD