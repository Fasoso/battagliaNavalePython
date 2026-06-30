import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.vita = length
        self.coordinates = []

class Board:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        
    def draw(self, cursor=None):
        """Stampa la griglia nel terminale convertendo i numeri in simboli colorati.
        Se viene passato un 'cursor' (lista di coordinate), evidenzia quelle celle."""
        
        print("   " + " ".join([chr(65 + i) for i in range(self.size)]))
        
        for r, row in enumerate(self.grid):
            row_num = f"{r + 1:2d} "
            colored_row = []
            
            for c, cell in enumerate(row):
                if cell == 0:
                    simbolo = f"{colorama.Fore.BLUE}~"
                elif cell == 1:
                    simbolo = f"{colorama.Fore.WHITE}{colorama.Style.BRIGHT}■"
                elif cell == 2:
                    simbolo = f"{colorama.Fore.CYAN}O"
                elif cell == 4:
                    simbolo = f"{colorama.Fore.RED}{colorama.Style.BRIGHT}X"
                else:
                    simbolo = str(cell)
                
                if cursor and (r, c) in cursor:
                    simbolo = f"{colorama.Back.WHITE}{colorama.Fore.BLACK}" + ("~" if cell == 0 else "■")
                
                colored_row.append(simbolo + colorama.Style.RESET_ALL)
            
            print(row_num + " ".join(colored_row))

class Player:
    def __init__(self, nome, is_bot=False):
        self.nome = nome            
        self.is_bot = is_bot        
        self.myboard = Board()        
        self.enemyBoard = Board()     
        self.flotta = [
            Ship("Portaerei", 5),
            Ship("Corazzata", 4),
            Ship("Incrociatore", 3),
            Ship("Sottomarino", 3),
            Ship("Cacciatorpediniere", 2)
        ]
        self.navi_rimanenti = len(self.flotta)
        self.shotsFired = 0
        self.shotsHit = 0
        
    def attack(self, row, col, enemy_player):
        """Esegue un attacco alle coordinate specificate contro l'enemy_player."""
        
        if self.enemyBoard.grid[row][col] in [2, 4]:
            return "ALREADY_FIRED"
        
        self.shotsFired += 1
        
        if enemy_player.myboard.grid[row][col] == 1:
            self.shotsHit += 1
            self.enemyBoard.grid[row][col] = 4       
            enemy_player.myboard.grid[row][col] = 4  
            
            for nave in enemy_player.flotta:
                if (row, col) in nave.coordinates:
                    nave.vita -= 1
                    break
                    
            return "HIT"
            
        elif enemy_player.myboard.grid[row][col] == 0:
            self.enemyBoard.grid[row][col] = 2       
            enemy_player.myboard.grid[row][col] = 2  
            
            return "MISS"

class LanOpponent:
    def __init__(self, navi_iniziali):
        self.is_bot = False
        self.navi_rimanenti = navi_iniziali