import os
from colorama import Fore, Style
from gameFiles.logicFunctions import *
from gameFiles.classesFile import *
from time import sleep
import random

def botMode_main():            
    os.system('cls' if os.name == 'nt' else 'clear')
    botModeBanner()
    playerName = ""
    
    while True:
        playerName = input(f"Inserisci il tuo nome giocatore\n{Fore.GREEN}{Style.BRIGHT}>>> {colorama.Style.RESET_ALL}").strip()
        
        if playerName != "":
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            botModeBanner()
            print(f"{Fore.RED}{Style.BRIGHT}IL NOME NON PUO' ESSERE VUOTO. REINSERISCI{colorama.Style.RESET_ALL}")

    player = Player(playerName)
    bot = Player("Bender The Bot", is_bot=True)
    
    # 1. Posizionamento del giocatore
    placingShips(player.myboard, player.flotta)
    
    # 2. Posizionamento del bot
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\n{Fore.YELLOW}{bot.nome} sta posizionando le sue navi...{Style.RESET_ALL}")
    sleep(1.5)
    placingShipsRandom(bot.myboard, bot.flotta)
    
    # 3. Transizione
    loadingAnimation()
    
    # --- INIZIO LOOP DI GIOCO ---
    playerTurn = True
    
    while True:
        
        if playerTurn:
            # Turno del Player
            playerGame(player, bot)
            
            # TODO: Qui potrai inserire il controllo della vittoria (es. se bot.navi_rimanenti == 0: break)
            
        else:
            # Turno del Bot (Logica temporanea: spara a caso)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\n{Fore.RED}{Style.BRIGHT}Turno di {bot.nome}...{Style.RESET_ALL}")
            sleep(1.5)
            
            while True:
                r = random.randint(0, player.myboard.size - 1)
                c = random.randint(0, player.myboard.size - 1)
                
                esito = bot.attack(r, c, player)
                
                if esito != "ALREADY_FIRED":
                    if esito == "HIT":
                        print(f"{Fore.RED}ATTENZIONE! {bot.nome} ha colpito una tua nave in {chr(65+c)}{r+1}!{Style.RESET_ALL}")
                    elif esito == "MISS":
                        print(f"{Fore.BLUE}{bot.nome} ha mancato il bersaglio sparando in {chr(65+c)}{r+1}.{Style.RESET_ALL}")
                    sleep(2.5)
                    break # Esce dal ciclo del bot perché ha effettuato un attacco valido
            
        if sum(nave.vita for nave in bot.flotta) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                winBanner()
                
                precisione = int((player.shotsHit / player.shotsFired) * 100) if player.shotsFired > 0 else 0
                print(f"{Fore.YELLOW}--- RAPPORTO DI FINE BATTAGLIA ---{Style.RESET_ALL}")
                print(f"Colpi sparati: {player.shotsFired}")
                print(f"Colpi a segno: {player.shotsHit}")
                print(f"Precisione:    {precisione}%\n")
                
                input(f"{Fore.WHITE}Premi INVIO per tornare al menu principale...{Style.RESET_ALL}")
                break
        
        if sum(nave.vita for nave in player.flotta) == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                
                loseBanner()
                precisione = int((player.shotsHit / player.shotsFired) * 100) if player.shotsFired > 0 else 0
                print(f"{Fore.YELLOW}--- RAPPORTO DI FINE BATTAGLIA ---{Style.RESET_ALL}")
                print(f"Colpi sparati: {player.shotsFired}")
                print(f"Colpi a segno: {player.shotsHit}")
                print(f"Precisione:    {precisione}%\n")
                
                input(f"{Fore.WHITE}Premi INVIO per tornare al menu principale...{Style.RESET_ALL}")
                break
            
            
            
        # Inversione dei ruoli alla fine di ogni turno
        playerTurn = not playerTurn