import socket
import os
import msvcrt
from colorama import Fore, Style
from time import sleep

def host_game():
    """Avvia il server in ascolto, permettendo di annullare premendo ESC."""
    # Creiamo il socket normalmente
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Tentiamo il bind (recuperando l'IP locale automaticamente)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    port = 50007
    
    try:
        server.bind((local_ip, port))
        server.listen(1)
        server.settimeout(1.0) 
    except Exception as e:
        print(f"\n{Fore.RED}Errore durante l'avvio del server: {e}{Style.RESET_ALL}")
        sleep(2)
        return None

    print(f"\n{Fore.CYAN}=== SERVER IN ASCOLTO ==={Style.RESET_ALL}")
    print(f"Comunica questo IP al tuo amico: {Fore.YELLOW}{local_ip}{Style.RESET_ALL}")
    print(f"{Fore.WHITE}In attesa che l'avversario si connetta...{Style.RESET_ALL}")
    print(f"{Fore.RED}Premi ESC per annullare e tornare al menu.{Style.RESET_ALL}\n")

    conn = addr = None


    while True:
        try:
            # Tenta di accettare la connessione per 1 secondo
            conn, addr = server.accept()
            # Se ci riesce, interrompe il ciclo ed entra in partita
            break 
        except socket.timeout:
            # Se scatta il timeout di 1 secondo e nessuno si è connesso, 
            # il programma si sveglia un attimo e controlla la tastiera!
            
            if msvcrt.kbhit():  # Verifica se è stato premuto un tasto
                tasto = msvcrt.getch()
                # 27 è il codice ASCII del tasto ESC, b'\x03' è Ctrl+C
                if tasto == b'\x1b' or tasto == b'\x03': 
                    print(f"\n{Fore.YELLOW}Connessione annullata dall'utente. Chiusura server...{Style.RESET_ALL}")
                    server.close()
                    sleep(1.5)
                    return None
            
            # Se nessun tasto è stato premuto, il ciclo ricomincia e aspetta un altro secondo
            continue
        except (KeyboardInterrupt, SystemExit):
            # Cattura il Ctrl+C se preso nei microsecondi di break
            print(f"\n{Fore.RED}Chiusura server...{Style.RESET_ALL}")
            server.close()
            return None

    print(f"{Fore.GREEN}Giocatore connesso da: {addr[0]}{Style.RESET_ALL}")
    sleep(1.5)
    return conn

def join_game():
    """Logica per il client. Restituisce il socket connesso o None in caso di errore."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Fore.CYAN}{Style.BRIGHT}=== UNISCITI A UNA PARTITA ==={Style.RESET_ALL}")
    ip_host = input(f"Inserisci l'IP dell'Host:\n{Fore.CYAN}>>> {Style.RESET_ALL}").strip()
    porta = 50007
    
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