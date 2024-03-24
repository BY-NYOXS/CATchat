#BYNYOXS
import socket
import threading
from colorama import Fore,Back,Style
import time

time.sleep(2)#BYNYOXS

isim = ''' 
                               
                               _____________________________________________________
░█████╗░░█████╗░████████╗     | NOT:                                                |
██╔══██╗██╔══██╗╚══██╔══╝     |Anonim mesajlaşırken, mesajlarınız karışabilir.      |           
██║░░╚═╝███████║░░░██║░░░     |Bu durumu önlemek için sırayla mesaj gönderin        |           
██║░░██╗██╔══██║░░░██║░░░     |_____________________________________________________|
╚█████╔╝██║░░██║░░░██║░░░     |BY:NYOXS|v1|
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░


                                                
'''


print(Fore.RED+isim)

ip=input(Fore.RED+"Server İp Adresini Giriniz==")
port=int(input(Fore.RED+"Server Portunuzu Giriniz=="))
nick=input(Fore.RED+"Arkadaşınızın Nıck'ini Giriniz==")#BYNYOXS

time.sleep(2)


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')#BYNYOXS
            if not message:
                print(Fore.RED+"HATA:Baglantı Kurulamadı.")
                break
            print(Fore.YELLOW+nick+" >",Fore.GREEN+f"{message}")
        except:
            break
            

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

message_receiver = threading.Thread(target=receive_messages, args=(client,))#BYNYOXS
message_receiver.start()


while True:
    time.sleep(1)
    print(Fore.MAGENTA+"CHAT:")
    message = input(Fore.WHITE+"==")
    client.send(message.encode('utf-8'))#BYNYOXS

