#!/usr/bin/env python
import pyglet
from pyglet import clock
from lib.player import Player
from lib.window import Window

if __name__ == '__main__':
  window = Window(1024, 768, True)
  
  pyglet.clock.schedule_interval(window.update, (1/120.))
  pyglet.app.run()