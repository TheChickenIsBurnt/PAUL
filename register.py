# Registration via env

clientid = input("client id: ")
clientsec = input("client secret: ")
useragent = input("user agent: ")
uname = input("uname: ")
password = input("password: ")

f = open(".env", "x")
f.write('CLIENT_ID="' + clientid + '"\n')
f.write('CLIENT_SECRET="' + clientsec + '"\n')
f.write('USER_AGENT="' + useragent + '"\n')
f.write('USER_NAME="' + uname + '"\n')
f.write('PASSWORD="' + password + '"\n')
f.close()

# PLEASE DELETEh THIS FILE AFTER REGISTERED