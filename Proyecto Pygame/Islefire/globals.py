import pygame

def initialize(): 
    global SCREEN_WIDTH 
    SCREEN_WIDTH = 800
    global SCREEN_HEIGHT
    SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
    global GRAVITY 
    GRAVITY = 0.75
    global BACKGROUNDCOLOR
    BACKGROUNDCOLOR = (144, 201, 130)
    global FPS
    FPS = 60
    global RED
    RED = (255,0,0)
