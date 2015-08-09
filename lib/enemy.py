import pyglet

from lib.gameobject import GameObject

class Enemy(GameObject):
  alive = None
  shield = 0.0
  life = 0.0

  def __init__(self,
    start_x,
    start_y,
    start_rotation,
    start_scale,
    image_file,
    start_delta,
    start_velocity,
    start_alive,
    start_shield,
    start_life):

    super(self.__class__, self).__init__(start_x,
      start_y,
      start_rotation,
      start_scale,
      image_file,
      start_delta,
      start_velocity)
    
    self.alive = start_alive
    self.shield = start_sheild
    self.life = start_life