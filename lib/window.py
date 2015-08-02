import pyglet
from math import *
from random import randint
from lib.player import Player
from lib.enemy import Enemy

class Window(pyglet.window.Window):
  player = None
  enemy_qty = 10
  enemy = []
  label_mouse_xy = None
  mouse_x = 0
  mouse_y = 0

  # Class initializer
  def __init__(self, size_x, size_y, resize):
    super(Window, self).__init__(resizable = resize, visible = True, vsync = False)
    self.set_size(size_x, size_y)
    self.set_caption('SpaceCow')
    self.maximize()

    self.player = Player((self.width / 2), (self.height / 2), 0, "resources/ship.png")

    for enemies in range(self.enemy_qty):
      self.enemy.append(Enemy((self.width / 2), (self.height / 2), 0, "resources/cow.png"))

    for e in self.enemy:
      e.x_pos = randint(0, self.width)
      e.y_pos = randint(0, self.height)
      e.rotation = randint(0, 360)

    self.player.x_pos = self.width / 2
    self.player.y_pos = self.height / 2
    self.label_mouse_xy = pyglet.text.Label("Mouse Location")

  def follow_mouse(self, player, timer, speed):
    player.c_val = sqrt((self.mouse_x - player.x_pos) ** 2 + \
      (self.mouse_y - player.y_pos) ** 2)
    player.x_pos -= ((player.x_pos - self.mouse_x) / player.c_val * speed * timer)
    player.y_pos -= ((player.y_pos - self.mouse_y) / player.c_val * speed * timer)
    delta_x = player.x_pos - self.mouse_x
    delta_y = player.y_pos - self.mouse_y

    if player.c_val > 1.0:
      player.rotation = atan2(delta_y, delta_x) / pi * 180 * -1

  def follow(self, enemy, timer, speed):
    enemy.c_val = sqrt((enemy.x_pos - self.player.x_pos) ** 2 + \
      (enemy.y_pos - self.player.y_pos) ** 2)
    enemy.x_pos -= ((enemy.x_pos - self.player.x_pos) / enemy.c_val * speed * timer)
    enemy.y_pos -= ((enemy.y_pos - self.player.y_pos) / enemy.c_val * speed * timer)
    delta_x =  enemy.x_pos - self.player.x_pos
    delta_y =  enemy.y_pos - self.player.y_pos

    if enemy.c_val > 1.0:
      enemy.rotation = atan2(delta_y, delta_x) / pi * 180 * -1

  def update(self, dt):
    self.label_mouse_xy.text = \
      "mouse_x: %d mouse_y: %d | player_x: %d player_y: %d | delta: %f | rotation: %f" % \
      (self.mouse_x,
        self.mouse_y,
        self.player.x_pos,
        self.player.y_pos,
        self.player.c_val,
        self.player.rotation)
    self.follow_mouse(self.player, dt, self.player.speed)

    for e in self.enemy:
      self.follow(e, dt, 10)

  def on_draw(self):
    self.clear()
    self.player.draw_player()

    for e in self.enemy:
      e.draw_player()

    self.label_mouse_xy.draw()

  def on_mouse_motion(self, x, y, dx, dy):
    self.label_mouse_xy.x = 10.0
    self.label_mouse_xy.y = 10.0
    self.mouse_x = x
    self.mouse_y = y

