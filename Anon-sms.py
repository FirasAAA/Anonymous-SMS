import os
import requests
import sys

if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetConsoleOutputCP(65001)
    sys.stdout.reconfigure(encoding='utf-8')

def sms():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('''
    █████╗ ███╗   ██╗ ██████╗  ███╗   ██╗     ███████╗███╗   ███╗███████╗
   ██╔══██╗████╗  ██║██╔═══██╗ ████╗  ██║     ██╔════╝████╗ ████║██╔════╝
   ███████║██╔██╗ ██║██║   ██║ ██╔██╗ ██║     █████╗  ██╔████╔██║█████╗  
   ██╔══██║██║╚██╗██║██║   ██║ ██║╚██╗██║          ██╔██║╚██╔╝██║     ██╔ 
   ██║  ██║██║ ╚████║╚██████╔╝ ██║ ╚████║     ███████╗██║ ╚═╝ ██║███████╗
   ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═╝  ╚═══╝     ╚══════╝╚═╝     ╚═╝╚══════╝

    ''')
    print('''\n
    [1] Send SMS
    [2] Exit
    ''')
    choice = input("Choose an option: ")
    if choice == '1':
        send_sms()
    elif choice == '2':
        exit()
    else:
        print("Invalid option. Please try again.")
        sms()
def send_sms():
    phone = input("phone number with prefix, exemple +3355555555 :")
    message = input("message :")

    resp = requests.post("https://textbelt.com/text",{'phone': phone,'message':message,'key':'textbelt'})
    print('\n',resp.json())
    if resp.json()['success'] == True:
        print("SMS sent successfully!")
    else:
        print("Failed to send SMS. Please check the number and try again.")

sms()
    
