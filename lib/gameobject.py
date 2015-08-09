import pyglet

class GameObject(object):
  x = 0.0
  y = 0.0
  rotation = 0.0
  scale = 0.0
  speed = 0.0
  delta = 0.0
  image_file = None
  game_object = None
  game_sprite = None

  def __init__(self,
    start_x,
    start_y,
    start_rotation,
    start_scale,
    image_file,
    start_delta,
    start_velocity):
  
  self.x = start_x
  self.y = start_y
  self.rotation = start_rotation
  self.scale = start_scale
  self.speed = start_velocity
  self.delta = start_delta
  self.image_file = image_file
