#!/usr/bin/env python
import pyglet

window = pyglet.window.Window(800,600)

pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_COLOR, pyglet.gl.GL_DST_COLOR)

playfield = pyglet.image.load('images/playfield.png')
rune = pyglet.image.load('images/rune1.png')
@window.event

def on_draw():
	window.clear()

	playfield.blit(0, 0)
	rune.blit(3, 3)

pyglet.app.run()

