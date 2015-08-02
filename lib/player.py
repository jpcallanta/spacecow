import pyglet

class Player:
  x_pos = 0.0
  y_pos = 0.0
  rotation = 0.0
  scale = 1.0
  speed = 50.0
  c_val = 0.0
  image_file = None
  player = None
  player_sprite = None

  # Class initializer
  def __init__(self, start_x, start_y, start_rot, image_file):
    self.x_pos = start_x
    self.y_pos = start_y
    self.rotation = start_rot
    self.image_file = image_file
    self.player = pyglet.image.load(self.image_file)
    self.player.anchor_x = self.player.width / 2
    self.player.anchor_y = self.player.height / 2
    self.player_sprite = pyglet.sprite.Sprite(self.player,
                                              self.x_pos,
                                              self.y_pos,
                                              subpixel = True)

  def draw_player(self):
    self.player_sprite.x = self.x_pos
    self.player_sprite.y = self.y_pos
    self.player_sprite.scale = self.scale
    self.player_sprite.rotation = self.rotation

    self.player_sprite.draw()