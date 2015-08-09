import pyglet
from math import *
from random import randint
from lib.player import Player
from lib.enemy import Enemy
from lib.settings import Settings

class Window(pyglet.window.Window):
  settings = None
  player = None
  enemy = []
  label_mouse_xy = None
  mouse_x = 0
  mouse_y = 0

  def __init__(self):
    # Load up game settings
    self.settings = Setting()

    # Setup main game window
    super(Window, self).__init__(resizable = self.settings.window_resize,
      vsync = self.settings.window_vsync,
      visible = True)
    self.set_size(self.settings.window_x, self.settings.window_y)
    self.set_caption('SpaceCow')

    if self.settings.window_maximized:
      self.maximize()

    # Setup enemies
    self.enemy in range(self.settings.enemy.qty):
      self.enemy.append(Enemy
        (randint(0, self.width),
          randint(0, self.height),
          randint(0, self.rotation),
          1.0,
          'resources/cow.png',
          0.0,
          randint(0, 25),
          True,
          0.0,
          1.0))

  def __init__(self, size_x, size_y, resize):
    self.player = Player((self.width / 2), (self.height / 2), 0, "resources/ship.png")

    self.player.x_pos = self.width / 2
    self.player.y_pos = self.height / 2
    self.label_mouse_xy = pyglet.text.Label("Mouse Location")

    self.play_bg_music()

  def play_bg_music(self):
    bg_music = pyglet.media.Player()
    music = pyglet.media.load('resources/635964_A-Heros-Destiny.mp3')

    bg_music.queue(music)

    bg_music.eos_action = pyglet.media.Player.EOS_LOOP

    bg_music.play()

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

