# importing Library
import pgzrun
from random import randint
TITLE = "GOODshot"
WIDTH = 500
HEIGHT = 500

# to store message 
message = ""

# creating the character
greenguy = Actor("greenguy")

def draw():
    screen.clear()
    screen.fill(color = "#19434F")
    greenguy.draw()
    screen.draw.text(message,center=(250,20),fontsize=25)

def place_gg():
    greenguy.x = randint(50,450)
    greenguy.y = randint(50,450)

def on_mouse_down(pos):
    global message 
    if greenguy.collidepoint(pos):
        message = " Oh hiiiiiiiiiiiiiii, Good Shot!"
        place_gg()
    else:
        message = "Oh hiiiiiiiiiiiiiii, Bad Shot!"

place_gg()
pgzrun.go()
