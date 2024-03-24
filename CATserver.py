#BYNYOXS
import socket
import threading
from colorama import Fore,Back,Style
import os
import time

time.sleep(2)

isim = ''' 
                               
                               _____________________________________________________
░█████╗░░█████╗░████████╗     | NOT:                                                |
██╔══██╗██╔══██╗╚══██╔══╝     |Anonim mesajlaşırken, mesajlarınız karışabilir.      |           
██║░░╚═╝███████║░░░██║░░░     |Bu durumu önlemek için sırayla mesaj gönderin        |           
██║░░██╗██╔══██║░░░██║░░░     |_____________________________________________________|
╚█████╔╝██║░░██║░░░██║░░░     |BY:NYOXS|v1|
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

                                                
'''

print(Fore.RED+isim)#BYNYOXS
port=int(input(Fore.RED+"Server Hangi Portta Kullanılacak?(1111-9999)=="))
nick=input(Fore.RED+"Arkadaşınızın Nıck'ini Giriniz==")
os.system('clear')
print(Fore.RED+isim)

time.sleep(2)
#BYNYOXS

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(Fore.RED+"HATA:Baglantı Kurulamadı.")
                break
            print(Fore.BLUE+nick+" >",Fore.GREEN+f"{message}")
        except:
            break

          

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", port))
    server.listen()

    print(Fore.RED+f"Server Başalatıldı \nPORT:{port}")

    client, address = server.accept()
    print(Fore.YELLOW+f"Baglantı Kuruldu {address}")

    message_receiver = threading.Thread(target=receive_messages, args=(client,))
    message_receiver.start()
    


    while True:
        time.sleep(2)
        print(Fore.MAGENTA+"CHAT:")
        message = input(Fore.WHITE+"==")
        client.send(message.encode('utf-8'))
        
       

if __name__ == "__main__":
    start_server()


#BYNYOXS
