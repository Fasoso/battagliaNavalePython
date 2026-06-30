import socket
import os
from colorama import Fore, Style
from time import sleep

def host_game():
    """Logica per il server. Restituisce il socket connesso."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nome_host = socket.gethostname()
    ip_locale = socket.gethostbyname(nome_host)
    porta = 5555 
    
    server_socket.bind(('0.0.0.0', porta)) 
    server_socket.listen(1) 
    
    print(f"{Fore.GREEN}{Style.BRIGHT}=== SERVER AVVIATO ==={Style.RESET_ALL}")
    print(f"In attesa di uno sfidante...")
    print(f"Di' al tuo amico di connettersi a questo IP: {Fore.YELLOW}{ip_locale}{Style.RESET_ALL}")

    conn, addr = server_socket.accept()
    
    print(f"\n{Fore.GREEN}Sfida accettata! Giocatore connesso da: {addr[0]}{Style.RESET_ALL}")
    sleep(2)
    
    return conn

def join_game():
    """Logica per il client. Restituisce il socket connesso o None in caso di errore."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Fore.CYAN}{Style.BRIGHT}=== UNISCITI A UNA PARTITA ==={Style.RESET_ALL}")
    ip_host = input(f"Inserisci l'IP dell'Host:\n{Fore.CYAN}>>> {Style.RESET_ALL}").strip()
    porta = 5555
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"\nTentativo di connessione a {ip_host}...")
    
    try:
        client_socket.connect((ip_host, porta))
        print(f"{Fore.GREEN}{Style.BRIGHT}Connessione stabilita con successo!{Style.RESET_ALL}")
        sleep(2)
        
        return client_socket
        
    except Exception as e:
        print(f"\n{Fore.RED}Impossibile connettersi. Assicurati che l'Host sia pronto e l'IP sia corretto.{Style.RESET_ALL}")
        input("Premi INVIO per tornare indietro...")
   
        return None