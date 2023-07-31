# BruteSSH
Simple Python tool used for brute force ssh login using list of usernames and passwords.

## Usage:
  * BruteSSH.py -t 192.168.1.1 --pnum 22 -u "msfadmin" -p "msfadmin"
  
  * BruteSSH.py -t 192.168.1.1 --pnum 22 -U Users.txt -P Passwords.txt


  ## Requriments:

    > python -m pip install paramiko
