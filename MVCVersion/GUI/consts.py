#Intelligent Systems Project Assignment
#Authors: Daniel Nelson, Tyler Beaumont
#Statics.py
"""This file contains only colour related definitions required for gui"""

StartupMessage = "Intelligent Systems Assignment 1.\nAuthors: Daniel N & Tyler B.\n"

def rgb_to_hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


GREY = rgb_to_hex(  54,  54,  54)
BLACK= rgb_to_hex(   0,   0,   0)
WHITE= rgb_to_hex( 255, 255, 255)
LGREY= rgb_to_hex( 212, 212, 212)

BLUE = rgb_to_hex(  84, 131, 179)
MINT = rgb_to_hex( 130, 255, 193)
GREEN= rgb_to_hex(  57, 143,  57)
YELLOW=rgb_to_hex( 255, 241, 120)
ORANGE=rgb_to_hex( 255, 200, 138)
PINK  =rgb_to_hex( 252, 157, 157)
RED   =rgb_to_hex( 235,  63,  63)
NIGHT =rgb_to_hex( 140, 136, 181)
PURPLE=rgb_to_hex(  68,  57, 184)
SKY   =rgb_to_hex( 168, 245, 255)
CYAN  =rgb_to_hex(   7, 186, 186)
MAGENTA=rgb_to_hex(177,  18, 201)


COLOURS = {
    'l':BLUE, #location
    'd':BLACK,#Depot
    's':MINT,  #Selected
    'np':LGREY #No package
}

COL_LIST = [MINT,GREEN,YELLOW,ORANGE,PINK,RED,NIGHT,SKY,CYAN,MAGENTA]

#node radius
R = 8