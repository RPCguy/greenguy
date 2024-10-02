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

pgzrun.go()