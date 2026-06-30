import colorama
import os
from time import sleep
from gameFiles.logicFunctions import banner, menu
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
                print(colorama.Fore.RED + "GAME CLOSED" + colorama.Style.RESET_ALL)
                break
         
    except KeyboardInterrupt:
        print(colorama.Fore.RED + "\nGAME CLOSED" + colorama.Style.RESET_ALL)
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        
        