import colorama
import os
import sys
from time import sleep
from gameFiles.logicFunctions import banner, menu, showHistory
from gameModes.botModeGame import botMode_main
from gameModes.lanModeGame import lanMode_main

colorama.init(autoreset=True)

if __name__ == "__main__":
    
    isGameRunning = True
    try:
        while isGameRunning:
            os.system('cls' if os.name == 'nt' else 'clear')
            banner()
            choice = menu()
            
            if choice == 1:
                botMode_main()
                
            elif choice == 2:
                lanMode_main()
            
            elif choice == 3:
                showHistory()
                
            elif choice == 4:
                print(colorama.Fore.RED + "GAME CLOSED" + colorama.Style.RESET_ALL)
                break
         
    except KeyboardInterrupt:
        print(colorama.Fore.RED + "\nGAME CLOSED" + colorama.Style.RESET_ALL)
        try:
            sleep(1.5)

        except KeyboardInterrupt:
            pass
        
        sys.exit(0)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        
        