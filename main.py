from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Game(Entity):
    '''
    Tic Tac Toe game class
    '''
    def __init__(self):
        super().__init__()
        self.turn = 0

    def end_turn(self):
        '''
        End the turn of the player
        '''
        #self.turn = 1
        print("computers turn")
    
    def start_turn(self):
        '''
        Start the turn of the player
        '''
        self.turn = 0
        print("players turn")
    
    def check_win(self):
        '''
        Check if the player has won
        '''
        pass

    def check_draw(self):
        '''
        Check if the game is a draw
        '''
        pass

    def check_game_over(self):
        '''
        Check if the game is over
        '''
        pass

    def check_move(self):
        '''
        Check if the move is valid
        '''
        pass

    
    

class Player (Entity):
    '''
    Create a player class icluding the weapon
    '''
    def __init__(self, **kwargs):
        self.controller = FirstPersonController (**kwargs)
        super().__init__(parent=self.controller)
        self.lst = []
        self.hand_gun = Entity(
                            parent=camera.ui,
                            model='cube',
                            texture='white_cube',
                            scale=(0.2, 0.2, 1),
                            position=(0.5, -0.4),
                            rotation=Vec3(15, -10, 0),
                            color=color.gray
        )

    def input(self, key):
        '''
        Handle the input of the player
        '''
        if key == 'alt':
            app.destroy()
        if key == "left mouse down" and game.turn == 0:
            x = Bullet (parent=scene,
                    model='sphere',
                    color=color.yellow,
                    scale=0.1,
                    #collider='sphere',
                    name='bullet',
                    position=self.controller.camera_pivot.world_position,
                    rotation=self.controller.camera_pivot.world_rotation)
            game.end_turn()
            self.lst.append(x)

        print(key)
    
    

app = Ursina()
ground = Entity(model='plane',
                scale=30,
                texture= 'white_cube',
                texture_scale= (15, 15),
                name='ground',
                collider='mesh')

class Bullet(Entity):
    '''
    Bullet class
    '''
    def __init__(self, speed=50, lifetime=5, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.lifetime = lifetime
        self.start = time.time()
        
    def update(self) :
        '''
        Update the position of the bullet
        '''
        ray = raycast(self.world_position, self.forward, distance=self.speed*time.dt)
        if not ray.hit and time.time() - self.start < self. lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            if ray.entity==None or ray.entity.name != "Board":
                destroy(self)
                return
            print(ray.entity)
            ray.entity.texture = "/textures/x.png"
            destroy(self)
            return
        print(self.get_position())
        

game = Game()       
player = Player(position=(0,10,0))
x=5
y=8
z=2
for i in range(9):
    z-=2
    if i % 3 == 0:
        z=2
        y-=2
    Entity(model='cube',
        scale=2,
        texture="textures/cube.png",
        collider='cube',
        color=color.white,
        name="Board",
        value=" ",
        position=(x,y,z))
app.run()





# How to upload the code on github 
# '''
# git init
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin

# 