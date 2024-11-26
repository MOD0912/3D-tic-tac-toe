'''
ursina 3d with ground and first person controller
'''
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ground = Entity(model='plane',
                scale=30,
                texture= 'white_cube',
                texture_scale= (15, 15),
                collider='mesh')

player = FirstPersonController()
cube = Entity(model='cube', 
              texture="arrow_right",
              #color=color.red, 
              scale=(1, 2, 1), 
              position=(2, 0, 0)
              )

def input(key):
    if key == 'alt' or key == 'q':
        exit()
app.run()







