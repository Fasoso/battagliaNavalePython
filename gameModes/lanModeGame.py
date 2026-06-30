import os
import readchar
from time import sleep
from colorama import Fore, Style
from gameFiles.logicFunctions import *
from gameFiles.classesFile import *
from gameFiles.lanNetlogic import host_game, join_game

def start_lan_match(conn, is_host):
    """Gestisce la partita in LAN unendo la rete al mirino interattivo e alla chat."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{Fore.CYAN}{Style.BRIGHT}=== PREPARAZIONE FLOTTA ==={Style.RESET_ALL}")
    while True:
        playerName = input(f"Inserisci il tuo nome comandante\n{Fore.GREEN}>>> {Style.RESET_ALL}").strip()
        if playerName != "":
            player = Player(playerName)
            break
        print(f"{Fore.RED}Il nome non può essere vuoto.{Style.RESET_ALL}")

    placingShips(player.myboard, player.flotta)
    

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.YELLOW}In attesa che l'avversario finisca di posizionare le navi...{Style.RESET_ALL}")
    
    conn.send(f"READY:{player.nome}".encode('utf-8'))
    risposta = conn.recv(1024).decode('utf-8')
    
    nome_avversario = "Avversario"
    if risposta.startswith("READY:"):
        nome_avversario = risposta.split(":", 1)[1]
        print(f"\n{Fore.GREEN}{Style.BRIGHT}Il comandante {nome_avversario} è pronto! Battaglia imminente!{Style.RESET_ALL}")
        sleep(2)
        loadingAnimation()
        
    playerTurn = True if is_host else False
    game_over = False
            
    avversario_lan = LanOpponent(len(player.flotta))
    
    if hasattr(player, 'navi_rimanenti'):
        player.navi_rimanenti = len(player.flotta)
    
    while True:
        if game_over:
            break
            
        if playerTurn:
            riga = 0
            colonna = 0
            comand = ""
            ha_sparato = False
            
            while not ha_sparato:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.GREEN}{Style.BRIGHT}IL TUO TURNO{Style.RESET_ALL}")
                
                print(f"\n{Fore.YELLOW}{Style.BRIGHT}=== CAMPO AVVERSARIO ==={Style.RESET_ALL}")
                player.enemyBoard.draw(cursor=[(riga, colonna)])
                
                print(f"\n{Fore.GREEN}{Style.BRIGHT}=== TUA FLOTTA ==={Style.RESET_ALL}")
                player.myboard.draw()
                
                print(f"\n{Fore.CYAN}Frecce: Mira | Lettere: Scrivi Comando | INVIO (vuoto): Spara{Style.RESET_ALL}")
                print(f"Digita 'help' o 'h' per la lista dei comandi disponibili.")
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
                        if player.enemyBoard.grid[riga][colonna] in [2, 4]:
                            print(f"\n{Fore.RED}Hai già sparato in queste coordinate! Spostati.{Style.RESET_ALL}")
                            sleep(1.5)
                        else:
                            ha_sparato = True 
                    else:
                        cmd = comand.strip().lower()
                        azione = comandLine(cmd, avversario_lan, conn)
                        
                        if azione == "SURRENDER":
                            os.system('cls' if os.name == 'nt' else 'clear')
                            loseBanner()
                            print(f"{Fore.RED}Ti sei arreso. Il nemico ha vinto la partita.{Style.RESET_ALL}\n")
                            input("Premi INVIO per uscire...")
                            game_over = True
                            break
                            
                        comand = ""
                else:
                    if len(tasto) == 1 and tasto.isprintable():
                        comand += tasto
            
            if game_over:
                break

            player.shotsFired += 1 
            print(f"\n{Fore.CYAN}Missile lanciato verso {chr(65+colonna)}{riga+1}...{Style.RESET_ALL}")
            conn.send(f"{riga},{colonna}".encode('utf-8'))
            
            esito = conn.recv(1024).decode('utf-8')
            
            if esito == "HIT":
                player.shotsHit += 1 
                print(f"{Fore.GREEN}BERSAGLIO COLPITO!{Style.RESET_ALL}")
                player.enemyBoard.grid[riga][colonna] = 4
                sleep(2)
            elif esito == "SUNK":
                player.shotsHit += 1
                avversario_lan.navi_rimanenti -= 1  # Decrementiamo il contatore delle navi nemiche!
                print(f"{Fore.GREEN}{Style.BRIGHT}BERSAGLIO COLPITO E AFFONDATO!{Style.RESET_ALL}")
                player.enemyBoard.grid[riga][colonna] = 4
                sleep(2)
            elif esito == "MISS":
                print(f"{Fore.BLUE}Acqua.{Style.RESET_ALL}")
                player.enemyBoard.grid[riga][colonna] = 2
                sleep(2)
            elif esito == "WIN":
                player.shotsHit += 1 
                player.enemyBoard.grid[riga][colonna] = 4
                
                os.system('cls' if os.name == 'nt' else 'clear')
                winBanner()
                precisione = int((player.shotsHit / player.shotsFired) * 100) if player.shotsFired > 0 else 0
                
                print(f"{Fore.CYAN}Missione compiuta, Comandante {player.nome}! La flotta nemica è distrutta.{Style.RESET_ALL}\n")
                print(f"{Fore.YELLOW}--- RAPPORTO DI FINE BATTAGLIA ---{Style.RESET_ALL}")
                print(f"Colpi sparati: {player.shotsFired}")
                print(f"Colpi a segno: {player.shotsHit}")
                print(f"Precisione:    {precisione}%\n")
                input(f"{Fore.WHITE}Premi INVIO per tornare al menu principale...{Style.RESET_ALL}")
                break
            
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.RED}{Style.BRIGHT}TURNO NEMICO{Style.RESET_ALL}\n")
            
            print(f"{Fore.YELLOW}{Style.BRIGHT}=== CAMPO AVVERSARIO ==={Style.RESET_ALL}")
            player.enemyBoard.draw()
            
            print(f"\n{Fore.GREEN}{Style.BRIGHT}=== TUA FLOTTA ==={Style.RESET_ALL}")
            player.myboard.draw()
            print(f"\n{Fore.YELLOW}In attesa delle mosse di {nome_avversario}...{Style.RESET_ALL}")
            
            while True:
                messaggio_ricevuto = conn.recv(1024).decode('utf-8')
                
                if messaggio_ricevuto.startswith("CHAT:"):
                    testo = messaggio_ricevuto.split(":", 1)[1]
                    print(f"\n{Fore.MAGENTA}[{nome_avversario}]: {testo}{Style.RESET_ALL}")
                elif messaggio_ricevuto == "SURRENDER":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    winBanner()
                    print(f"{Fore.GREEN}Il comandante {nome_avversario} ha alzato bandiera bianca! Vittoria a tavolino!{Style.RESET_ALL}\n")
                    input("Premi INVIO per tornare al menu...")
                    game_over = True
                    break
                else:
                    dati = messaggio_ricevuto.split(",")
                    r_nemico = int(dati[0])
                    c_nemico = int(dati[1])
                    break
            
            if game_over:
                break
                
            if player.myboard.grid[r_nemico][c_nemico] == 1:
                player.myboard.grid[r_nemico][c_nemico] = 4
                nave_affondata = False
                
                for nave in player.flotta:
                    if (r_nemico, c_nemico) in nave.coordinates:
                        nave.vita -= 1
                        if nave.vita == 0:
                            nave_affondata = True
                        break
                        
                if sum(nave.vita for nave in player.flotta) == 0:
                    conn.send("WIN".encode('utf-8'))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    loseBanner()
                    precisione = int((player.shotsHit / player.shotsFired) * 100) if player.shotsFired > 0 else 0
                    
                    print(f"{Fore.RED}La tua intera flotta è stata annientata. Il nemico domina i mari.{Style.RESET_ALL}\n")
                    print(f"{Fore.YELLOW}--- RAPPORTO DI FINE BATTAGLIA ---{Style.RESET_ALL}")
                    print(f"Colpi sparati: {player.shotsFired}")
                    print(f"Colpi a segno: {player.shotsHit}")
                    print(f"Precisione:    {precisione}%\n")
                    input(f"{Fore.WHITE}Premi INVIO per tornare al menu principale...{Style.RESET_ALL}")
                    break
                elif nave_affondata:
                    if hasattr(player, 'navi_rimanenti'):
                        player.navi_rimanenti -= 1
                        
                    print(f"\n{Fore.RED}NAVE COLPITA E AFFONDATA! ({chr(65+c_nemico)}{r_nemico+1}){Style.RESET_ALL}")
                    conn.send("SUNK".encode('utf-8'))
                    sleep(2.5)
                else:
                    print(f"\n{Fore.RED}NAVE COLPITA! ({chr(65+c_nemico)}{r_nemico+1}){Style.RESET_ALL}")
                    conn.send("HIT".encode('utf-8'))
                    sleep(2.5)
            else:
                player.myboard.grid[r_nemico][c_nemico] = 2
                print(f"\n{Fore.BLUE}Mancato. ({chr(65+c_nemico)}{r_nemico+1}){Style.RESET_ALL}")
                conn.send("MISS".encode('utf-8'))
                sleep(2.5)
            
        playerTurn = not playerTurn

def lanMode_main():
    """Menu principale della modalità LAN"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        lanBanner()
        print(f"  [{Fore.CYAN}1{Style.RESET_ALL}] Crea una partita (Fai da Host)")
        print(f"  [{Fore.CYAN}2{Style.RESET_ALL}] Unisciti a una partita (Fai da Client)")
        print(f"  [{Fore.RED}3{Style.RESET_ALL}] Torna indietro")
        
        try:
            choice = int(input(f"{Fore.CYAN}\n>>> {Style.RESET_ALL}"))
            if choice == 1:
                conn = host_game() 
                if conn: 
                    start_lan_match(conn, is_host=True)
                break
            elif choice == 2:
                conn = join_game()
                if conn: 
                    start_lan_match(conn, is_host=False)
                    break
            elif choice == 3:
                return 
            else:
                print(f"{Fore.RED}Scelta non valida. Inserisci 1, 2 o 3.{Style.RESET_ALL}")
                sleep(1.5)
        except ValueError:
            print(f"{Fore.RED}Devi inserire un numero!{Style.RESET_ALL}")
            sleep(1.5)