import colorama
from colorama import Fore, Style
import os
import readchar
import random
from time import sleep
import sys

colorama.init(autoreset=True)

def banner():
    print(rf"""{Fore.CYAN}{Style.BRIGHT}
 ________         __    __  .__                 .__   .__        
  \_ |__ _____ ___/  |__/  |_|  |   ____   _____|  |__|  |_____  
   | __ \\__  \\   __\   __\  | _/ __ \ /  ___/  |  \|  \____ \ 
   | \_\ \/ __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >
   |___  (____  /__|  |__| |____/\___  >____  >___|  /__|  ___/ 
       \/     \/                     \/     \/     \/   |__|    
{Style.RESET_ALL}""")
    
def botModeBanner():
    print(rf"""{Fore.GREEN}{Style.BRIGHT}
┏┓ ┏━┓╺┳╸┏━╸┏━┓┏┳┓┏━╸┏┳┓┏━┓╺┳┓┏━╸
┣┻┓┃ ┃ ┃ ┃╺┓┣━┫┃┃┃┣╸ ┃┃┃┃ ┃ ┃┃┣╸ 
┗━┛┗━┛ ╹ ┗━┛╹ ╹╹ ╹┗━╸╹ ╹┗━┛╺┻┛┗━╸                                                                                         
{Style.RESET_ALL}""")
    
def lanBanner():
    print(rf"""{Fore.CYAN}{Style.BRIGHT}
        ╻  ┏━┓┏┓╻┏┳┓┏━┓╺┳┓┏━╸
        ┃  ┣━┫┃┗┫┃┃┃┃ ┃ ┃┃┣╸ 
        ┗━╸╹ ╹╹ ╹╹ ╹┗━┛╺┻┛┗━╸
    {Style.RESET_ALL}""")


def winBanner():
    print(rf"""{Fore.YELLOW}{Style.BRIGHT}
    █████   █████ █████ ███████████ ███████████    ███████    ███████████   █████   █████████  
   ▒▒███   ▒▒███ ▒▒███ ▒█▒▒▒███▒▒▒█▒█▒▒▒███▒▒▒█  ███▒▒▒▒▒███ ▒▒███▒▒▒▒▒███ ▒▒███   ███▒▒▒▒▒███ 
    ▒███    ▒███  ▒███ ▒   ▒███  ▒ ▒   ▒███  ▒  ███     ▒▒███ ▒███    ▒███  ▒███  ▒███    ▒███ 
    ▒███    ▒███  ▒███     ▒███        ▒███    ▒███      ▒███ ▒██████████   ▒███  ▒███████████ 
    ▒▒███   ███   ▒███     ▒███        ▒███    ▒███      ▒███ ▒███▒▒▒▒▒███  ▒███  ▒███▒▒▒▒▒███ 
     ▒▒▒█████▒    ▒███     ▒███        ▒███    ▒▒███     ███  ▒███    ▒███  ▒███  ▒███    ▒███ 
       ▒▒███      █████    █████       █████    ▒▒▒███████▒   █████   █████ █████ █████   █████
        ▒▒▒      ▒▒▒▒▒    ▒▒▒▒▒       ▒▒▒▒▒       ▒▒▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒ 
    {Style.RESET_ALL}""")
    
def loseBanner():
    print(rf"""{Fore.RED}{Style.BRIGHT}
         █████████    █████████     ███████    ██████   █████ ███████████ █████ ███████████ ███████████   █████████  
        ███▒▒▒▒▒███  ███▒▒▒▒▒███  ███▒▒▒▒▒███ ▒▒██████ ▒▒███ ▒▒███▒▒▒▒▒▒█▒▒███ ▒█▒▒▒███▒▒▒█▒█▒▒▒███▒▒▒█  ███▒▒▒▒▒███ 
        ███    ▒▒▒  ███     ▒▒▒  ███     ▒▒███ ▒███▒███ ▒███  ▒███   █ ▒  ▒███ ▒   ▒███  ▒ ▒   ▒███  ▒  ▒███    ▒███ 
       ▒▒█████████ ▒███         ▒███      ▒███ ▒███▒▒███▒███  ▒███████    ▒███     ▒███        ▒███     ▒███████████ 
        ▒▒▒▒▒▒▒▒███▒███         ▒███      ▒███ ▒███ ▒▒██████  ▒███▒▒▒█    ▒███     ▒███        ▒███     ▒███▒▒▒▒▒███ 
        ███    ▒███▒▒███     ███▒▒███     ███  ▒███  ▒▒█████  ▒███  ▒     ▒███     ▒███        ▒███     ▒███    ▒███ 
       ▒▒█████████  ▒▒█████████  ▒▒▒███████▒   █████  ▒▒█████ █████       █████    █████       █████    █████   █████
        ▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒▒▒    ▒▒▒▒▒    ▒▒▒▒▒ ▒▒▒▒▒       ▒▒▒▒▒    ▒▒▒▒▒       ▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒ 
    {Style.RESET_ALL}""")
    
def menu():
    print(f"  [{Fore.GREEN}1{Style.RESET_ALL}] Gioca vs BOT")
    print(f"  [{Fore.GREEN}2{Style.RESET_ALL}] Gioca Online (LAN)")
    print(f"  [{Fore.RED}3{Style.RESET_ALL}] Esci dal gioco")
    
    while True:
        try:
            choice = int(input(f"{Fore.GREEN}\n>>> {Style.RESET_ALL}"))
            if 1 <= choice <= 3:
                return choice
            else:
                print(f"{Fore.RED}IL VALORE DEVE ESSERE COMPRESO TRA 1 E 3. REINSERISCI{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}INPUT NON VALIDO. DEVI INSERIRE UN NUMERO. REINSERISCI{Style.RESET_ALL}")
    
def printPlayerBoard(player):
    """Mostra la situazione attuale del giocatore: il radar sopra e la propria griglia sotto"""
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}=== NEMICO ==={Style.RESET_ALL}")
    player.enemyBoard.draw()
    
    print(f"\n{Fore.GREEN}{Style.BRIGHT}=== TU ==={Style.RESET_ALL}")
    player.myboard.draw()
    print(f"{Fore.YELLOW}====================================\n{Style.RESET_ALL}")

def placingShipWithKeys(board, nave):
    """Permette all'utente di muovere e ruotare la nave sulla griglia con le freccette."""
    riga = 0
    colonna = 0
    orizzontale = True 
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.YELLOW}Posiziona: {nave.name} (Lunghezza: {nave.length}){Style.RESET_ALL}")
        print(f"Frecce: Muovi | {Fore.CYAN}'R': Ruota{Style.RESET_ALL} | {Fore.GREEN}INVIO: Conferma{Style.RESET_ALL}\n")
        
        celle_occupate = []
        for i in range(nave.length):
            if orizzontale:
                celle_occupate.append((riga, colonna + i))
            else:
                celle_occupate.append((riga + i, colonna))
                
        board.draw(cursor=celle_occupate)
        
        tasto = readchar.readkey()
        
        if tasto == readchar.key.UP and riga > 0:
            riga -= 1
        elif tasto == readchar.key.DOWN:
            limite = board.size - (nave.length if not orizzontale else 1)
            if riga < limite:
                riga += 1
        elif tasto == readchar.key.LEFT and colonna > 0:
            colonna -= 1
        elif tasto == readchar.key.RIGHT:
            limite = board.size - (nave.length if orizzontale else 1)
            if colonna < limite:
                colonna += 1
                
        elif tasto in ['r', 'R']:
            orizzontale = not orizzontale
            if orizzontale and colonna + nave.length > board.size:
                colonna = board.size - nave.length
            elif not orizzontale and riga + nave.length > board.size:
                riga = board.size - nave.length
                
        elif tasto == readchar.key.ENTER:
            sovrapposizione = False
            for r, c in celle_occupate:
                if board.grid[r][c] == 1:
                    sovrapposizione = True
                    break
            
            if sovrapposizione:
                print(f"\n{Fore.RED}POSIZIONE NON VALIDA! C'è già una nave qui. Premi un tasto per riprovare...{Style.RESET_ALL}")
                readchar.readkey()
            else:
                for r, c in celle_occupate:
                    board.grid[r][c] = 1  
                    nave.coordinates.append((r, c))
                return 

def placingShips(board, flotta):
    for nave in flotta:
        placingShipWithKeys(board, nave)
        
def placingShipsRandom(board, flotta):
    """Posiziona l'intera flotta del BOT in modo completamente automatico e casuale."""
    for nave in flotta:
        posizionata = False
        while not posizionata:
            orizzontale = random.choice([True, False])
            if orizzontale:
                riga = random.randint(0, board.size - 1)
                colonna = random.randint(0, board.size - nave.length)
            else:
                riga = random.randint(0, board.size - nave.length)
                colonna = random.randint(0, board.size - 1)
                
            celle_occupate = []
            for i in range(nave.length):
                if orizzontale:
                    celle_occupate.append((riga, colonna + i))
                else:
                    celle_occupate.append((riga + i, colonna))
            
            sovrapposizione = False
            for r, c in celle_occupate:
                if board.grid[r][c] == 1:
                    sovrapposizione = True
                    break
            
            if not sovrapposizione:
                for r, c in celle_occupate:
                    board.grid[r][c] = 1
                    nave.coordinates.append((r, c))
                posizionata = True 
                
def loadingAnimation():
    print(f"{Fore.CYAN}Caricamento partita{Style.RESET_ALL}", end="")
    for _ in range(3):
        print(f"{Fore.CYAN}.{Style.RESET_ALL}", end="", flush=True)
        sleep(0.6)
    print()
    os.system('cls' if os.name == 'nt' else 'clear')
        
def playerGame(player, bot):
    """Gestisce il turno del giocatore umano: radar interattivo e riga di comando."""
    riga = 0
    colonna = 0
    comand = ""
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"{Fore.YELLOW}{Style.BRIGHT}===  ATTACCA IL NEMICO   ==={Style.RESET_ALL}")
        
        # Disegna il radar per la mira
        player.enemyBoard.draw(cursor=[(riga, colonna)])
        
        print(f"\n{Fore.GREEN}=== TUA FLOTTA ==={Style.RESET_ALL}")
        # Mostra anche la propria griglia per tenere d'occhio la situazione
        player.myboard.draw()
        
        print(f"\n{Fore.CYAN}Frecce: Mira | Lettere: Comando | INVIO: Conferma/Spara{Style.RESET_ALL}")
        print(f"{Fore.GREEN}>>>{Style.RESET_ALL} {comand}", end="", flush=True)
        
        tasto = readchar.readkey()
        if tasto == readchar.key.UP and riga > 0:
            riga -= 1
        elif tasto == readchar.key.DOWN and riga < player.enemyBoard.size - 1:
            riga += 1
        elif tasto == readchar.key.LEFT and colonna > 0:
            colonna -= 1
        elif tasto == readchar.key.RIGHT and colonna < player.enemyBoard.size - 1:
            colonna += 1
            
        elif tasto == readchar.key.BACKSPACE:
            comand = comand[:-1]
            
        elif tasto == readchar.key.ENTER:
            if comand.strip() == "":

                esito = player.attack(riga, colonna, bot)
                
                if esito == "ALREADY_FIRED":
                    print(f"\n{Fore.RED}Hai già sparato in queste coordinate! Spostati.{Style.RESET_ALL}")
                    sleep(1.5)
                else:
                    if esito == "HIT":
                        # Controlla quale nave del bot è stata colpita e se è affondata
                        nave_affondata = False
                        for nave in bot.flotta:
                            if (riga, colonna) in nave.coordinates:
                                if nave.vita == 0:
                                    nave_affondata = True
                                break
                        if nave_affondata:
                            bot.navi_rimanenti -= 1
                            print(f"\n{Fore.GREEN}{Style.BRIGHT}BOOM! Bersaglio colpito e AFFONDATO!{Style.RESET_ALL}")
                        else:
                            print(f"\n{Fore.GREEN}{Style.BRIGHT}BOOM! Bersaglio colpito!{Style.RESET_ALL}")
                    elif esito == "MISS":
                        print(f"\n{Fore.BLUE}Splash... Hai mancato.{Style.RESET_ALL}")
                    sleep(2)
                    return 
            else:
                # Esegue il comando inserito
                comandLine(comand.strip().lower(), bot)
                comand = "" 
                
        else:
            if len(tasto) == 1 and tasto.isprintable():
                comand += tasto
    
def comandLine(comand, player, conn=None):
    """Gestisce i comandi speciali digitati durante il turno."""
    
    # Comandi base sempre validi
    commandList = ['help', 'h', 'enemyhealth', 'showenemybattlefield']
    
    # FILTRO: Se l'avversario non è un bot (siamo in LAN), sblocchiamo i comandi aggiuntivi
    if player.is_bot == False:
        commandList.extend(['clear', 'surrender', 'ff'])
    
    # Gestione del comando chat che ha argomenti (es. "chat ciao")
    is_chat = comand.startswith("chat ") and player.is_bot == False
    
    # Se non è un comando valido e non è una chat valida, dà errore
    if comand not in commandList and not is_chat:
        print(f"\n{Fore.RED}{Style.BRIGHT}COMANDO SCONOSCIUTO: '{comand}'{Style.RESET_ALL}")
        input("Premi INVIO per continuare...")
        return None
        
    # --- COINVOLGIMENTO DEI COMANDI ---
    elif comand in ["help", "h"]:
        print(f"\n{Fore.CYAN}--- GUIDA AI COMANDI DI GIOCO ---{Style.RESET_ALL}")
        print("  [INVIO vuoto]    : Lancia un missile alle coordinate attuali del mirino.")
        print("  enemyhealth      : Mostra le navi rimanenti del nemico.")
        if player.is_bot == False:
            print("  chat <testo>     : Invia un messaggio radio in tempo reale all'avversario.")
            print("  clear            : Pulisce la schermata del terminale e la ridisegna.")
            print("  surrender / ff   : Alza bandiera bianca decretando la tua sconfitta immediata.")
        input(f"\n{Fore.YELLOW}Premi INVIO per tornare alla battaglia...{Style.RESET_ALL}")
        
    elif comand == "enemyhealth":
        print(f"\n{Fore.RED}Navi nemiche rimanenti: {player.navi_rimanenti}{Style.RESET_ALL}")
        input(f"\n{Fore.YELLOW}Premi INVIO per tornare alla battaglia...{Style.RESET_ALL}")
        
    elif comand == "showenemybattlefield" and player.is_bot == True:
        print(f"\n{Fore.MAGENTA}{Style.BRIGHT}  [DEV MODE] GRIGLIA REALE DEL NEMICO {Style.RESET_ALL}")
        player.myboard.draw()
        input(f"\n{Fore.YELLOW}Premi INVIO per nascondere e tornare alla battaglia...{Style.RESET_ALL}")
        
    elif comand == "clear" and player.is_bot == False:
        return "CLEAR"
        
    elif comand in ["surrender", "ff"] and player.is_bot == False:
        if conn:
            conn.send("SURRENDER".encode('utf-8'))
        return "SURRENDER"
        
    elif is_chat:
        messaggio = comand[5:]
        if conn:
            conn.send(f"CHAT:{messaggio}".encode('utf-8'))
        print(f"\n{Fore.MAGENTA}[TU]: {messaggio}{Style.RESET_ALL}")
        sleep(1.5)
        return "CHAT"
        
    return None