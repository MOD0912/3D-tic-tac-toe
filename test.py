from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
class Player (Entity):
    def __init__(self, **kwargs):
        self. controller = FirstPersonController (**kwargs)
        super().__init__(parent=self.controller)


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
        if key == 'left mouse down':
            Schuss(position=self.position, start=self.hand_gun.position)
        if key == 'alt':
            app.destroy()
app = Ursina()

ground = Entity(model='plane',
                scale=20,
                texture= 'white_cube',
                texture_scale= (20,20),
                collider='mesh')

class Schuss(Entity):
    def __init__(self, position, start):
        super().__init__(
            parent=scene,
            model='sphere',
            color=color.yellow,
            position=start,
            scale=0.1
        )
        self.ziel = position

    def update(self):
        richtung = self.ziel - self.position
        self.position += richtung.normalized() * 5 * time.dt
        if distance(self, self.ziel) < 0.1:
            destroy(self)
player = Player(position=(0,10,0))


def input(key):
    if key == 'alt':
        app.destroy()
app.run()