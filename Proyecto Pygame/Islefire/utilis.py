import globals 
import pygame
import os 

class Movement():
  def __init__(self, speed):
    self.speed = speed

    self.direction = 1
    self.flip = False
    
    self.jumping = False
    self.in_air = False
    self.velocity_y = 0

    self.moving_left = False
    self.moving_right =False

  def move(self):
    dx = 0
    dy = 0 

    speed = self.speed
    #assign movement variables if moving left or right
    if self.moving_left:
      dx = -speed
      self.flip = True
      self.direction = -1
    
    if self.moving_right:
      dx = speed
      self.flip = False
      self.direction = 1  

    if self.jumping == True and self.in_air == False:
      self.velocity_y = -11
      self.jumping = False
      self.in_air = True

    # apply gravity   
    self.velocity_y += globals.GRAVITY
    if self.velocity_y > 10:
      self.velocity_y
    dy += self.velocity_y


    return dx, dy


class Animations():
  def __init__(self, character_type,x, y,  scale):
    self.character_type = character_type
    
    self.animation_list = []
    self.frame_index = 0
    self.update_time = pygame.time.get_ticks()
    self.action = 0
    
    animation_types = ['Idle', 'Run', 'Jump']
    for animation in animation_types:
      # reset temporary list of images
      temp_list = []
      # current number of frames in animation
      number_of_frames = len(os.listdir(f'img/{self.character_type}/{animation}/'))
      for i in range(number_of_frames):
        img = pygame.image.load(f'img/{self.character_type}/{animation}/{i}.png').convert_alpha()
        img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        temp_list.append(img)
      self.animation_list.append(temp_list)

    self.image = self.animation_list[self.action][self.frame_index]
    self.rect = self.image.get_rect()
    self.rect.center = (x,y)	
    
  def update_animation(self):
    # Update animation
    ANIMATION_COOLDOWN = 100
    # update Image depending on current frame
    self.image = self.animation_list[self.action][self.frame_index]
    # check if enough time has passed since last update
    if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
      self.update_time = pygame.time.get_ticks()
      self.frame_index += 1
    # if the animation has ran out reset back to the start    
      if self.frame_index >= len(self.animation_list[self.action]):
        self.frame_index = 0

  def update_action(self, new_action):
    # check if the new action is different to the previous one
    if new_action != self.action:
      self.action = new_action
      # update the animation settings
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()