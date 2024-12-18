# Description: Tic Tac Toe game in 3D
# Author: Melvin Kapferer
# Date: 11.11.2024
# Github: MOD0912

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Game(Entity):
    '''
    Tic Tac Toe game class
    '''
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.HUMAN = 'X'
        self.COMPUTER = 'O'
        self.value_lst = [' ' for _ in range(9)]
        print(self.value_lst)

    def end_turn(self):
        '''
        End the turn of the player
        '''
        #self.turn = 1
        print("computers turn")

    def check_win(self, player):
    # Überprüfen der Reihen
        for i in range(3):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True
        # Überprüfen der Spalten
        for j in range(3):
            if self.board[0][j] == player and self.board[1][j] == player and self.board[2][j] == player:
                return True
        # Überprüfen der Diagonalen
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player) or \
        (self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player):
            return True
        return False

    # Funktion zum Überprüfen auf Unentschieden
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    # Min-Max-Algorithmus
    def minimax(self, depth, is_maximizing):
        if self.check_win(self.COMPUTER):
            return 1
        if self.check_win(self.HUMAN):
            return -1 
        if self.check_draw():
            return 0
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.COMPUTER
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = self.HUMAN
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        best_score = min(score, best_score)
            return best_score

    # Funktion für den Computerzug
    def computer_move(self):
        player.end_of_game()
        best_score = -float('inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = self.COMPUTER
                    score = self.minimax(0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        self.board[best_move[0]][best_move[1]] = self.COMPUTER
        entity = lst[best_move[0]][best_move[1]]
        entity.texture = "/textures/o.png"
        entity.value = self.COMPUTER
        self.value_lst[entity.index] = self.COMPUTER
        


class Player (Entity):
    '''
    Create a player class icluding the weapon
    '''
    def __init__(self, **kwargs):
        self.controller = FirstPersonController (**kwargs)
        super().__init__(parent=self.controller)
        self.lst = []
        self.current_player = game.HUMAN
        self.hand_gun = Entity(
                            parent=camera.ui,
                            model='hand_stl.STL',
                            texture='white_cube',
                            color="#E3BC9A",
                            scale=0.001,
                            position=(0.3, -1),
                            rotation=Vec3(270, 0, 0)
        )
        self.current_player = game.HUMAN
        self.game_over = False

    def input(self, key):
        '''
        Handle the input of the player
        '''
        game_over = False
        if key == 'alt':
            app.destroy()
            exit()
            print("how")
        if key == "left mouse down" and game.turn == 0:
            self.bullet = Bullet (parent=scene,
                    model='hand_stl_v1.stl',
                    texture='white_cube',
                    color="#E3BC9A",
                    scale=0.00005,
                    #collider='sphere',
                    name='bullet',
                    position=self.controller.camera_pivot.world_position,
                    rotation=self.controller.camera_pivot.world_rotation)
            game.end_turn()
            self.lst.append(self.bullet)

    def calc(self, entity):
        rowow = int(entity.index)
        print("rowow: ", rowow) 
        if rowow <= 2:
            row = 0
        elif rowow > 2 and rowow <= 5:
            row = 1
        elif rowow > 5:
            row = 2
        else:
            print("rowow: ", rowow)
        print("row: ", row)
        col = int(entity.index)
        col = col % 3
        print("col: ", col)
        if game.board[row][col] == ' ':
            game.board[row][col] = game.HUMAN
            self.current_player = game.COMPUTER
        player.end_of_game()
        if self.current_player == game.COMPUTER and not self.game_over:
            
            game.computer_move()
            self.current_player = game.HUMAN
        else:
            self.current_player = game.COMPUTER
        print(game.board)
        
    
    def end_of_game(self):
        '''
        Check if the game is over
        '''
        if game.check_draw():
            print("Unentschieden!")
            self.game_over = True
            
        elif game.check_win(game.HUMAN):
            print("Du hast gewonnen!")
            self.game_over = True

        elif game.check_win(game.COMPUTER):
            print("Der Computer hat gewonnen!")
            self.game_over = True        

        
      
app = Ursina()
ground = Entity(model='plane',
                scale=30,
                texture= 'white_cube',
                texture_scale= (15, 15),
                name='ground',
                collider='mesh')

sky = Sky(texture='textures/o.png')

sky = Sky(texture='sky_sunset')

reset = Entity(parent=scene,
                model='hand_stl_v1.STL',
                #texture='texture/hand_stl.STL',
                scale=0.01,
                position=(9, 0.5*1.5, 5),
                color=color.red)

class Bullet(Entity):
    ''' 
    Bullet class
    '''
    def __init__(self, speed=100000, lifetime=10, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
        self.ray = None
        self.current_player = game.HUMAN
        
    def update(self) :
        '''
        Update the position of the bullet
        '''
        self.ray = raycast(self.world_position, self.forward, distance=100*time.dt)
        if not self.ray.hit and time.time() - self.start < self. lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            if self.ray.entity==None or self.ray.entity.name != "self.board":
                destroy(self)
                return
            
            
            #print(self.ray.entity)
            if self.ray.entity.value == " " and player.game_over == False:
                self.ray.entity.texture = "/textures/x.png"
                self.ray.entity.value = game.HUMAN
                game.value_lst[self.ray.entity.index] = game.HUMAN
                player.calc(self.ray.entity)
                player.end_of_game()
            
            
            print()
            print(game.value_lst)
            print()
            destroy(self)
            return
        
        #print(self.get_position())
        

game = Game()       
player = Player(position=(0,10,0))
x=9
y=8
z=2
lst = []
value_lst = []

for i in range(9):
    z-=2
    if i % 3 == 0:
        z=2
        y-=2
    board = Entity(model='cube',
        scale=2,
        texture="textures/cube.png",
        collider='cube',
        color=color.white,
        name="self.board",
        value=" ",
        index=i,
        position=(x,y,z))
    lst.append(board)

a = []
b = []
c = []


for i in range(0, 3):
    a.append(lst[i])
for i in range(3, 6):
    b.append(lst[i])
for i in range(6, 9):
    c.append(lst[i])
lst.clear()
lst.extend([a, b, c])

app.run()




