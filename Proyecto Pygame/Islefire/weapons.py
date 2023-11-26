import pygame
import globals 


class Bullet(pygame.sprite.Sprite):
  def __init__(self, x, y, direction):
      pygame.sprite.Sprite.__init__(self)
      image = pygame.image.load('img/icons/bullet.png').convert_alpha()
      self.speed = 10
      self.image = image
      self.rect = self.image.get_rect()
      self.rect.center = (x,y)
      self.direction = direction

  def update(self, bullet_group, player, enemies):
    # move bullet 
    self.rect.x += (self.direction * self.speed)
    # if bullet gone of screen
    if self.rect.right < 0 or self.rect.left > globals.SCREEN_WIDTH:
      self.kill()
    # check collision with characters
    if pygame.sprite.spritecollide(player.sprite, bullet_group, False):
      if player.alive:
        self.kill()
    for enemy in enemies:
      if pygame.sprite.spritecollide(enemy.sprite, bullet_group, False):
        if enemy.alive:
          self.kill()
    


