import pygame
import utilis
import weapons


# create Sprite groups

class Soldier(pygame.sprite.Sprite):
  def __init__(self, character_type, x, y, scale, speed, ammo):
    pygame.sprite.Sprite.__init__(self)
    self.alive = True
    self.shooting = False
    self.shoot_cooldown = 0
    self.ammo  = ammo
    self.start_ammo = ammo
    self.bullet_group = pygame.sprite.Group()

    # image and rect 
    self.sprite = utilis.Animations(character_type, x, y, scale)
    
    # movement 
    self.movement =utilis.Movement(speed)

  def update(self,player, enemies):
    self.update_animation()
    self.bullet_group.update(self.bullet_group, player, enemies)
    # update cooldown
    if self.shoot_cooldown > 0 :
      self.shoot_cooldown -= 1

  def able_to_jump(self):
    return self.alive and self.movement.in_air == False

  def move(self):
    #reset movement variables
    dx, dy = self.movement.move()
    
    # check for collision with floor
    if self.sprite.rect.bottom + dy > 300:
      self.movement.in_air = False
      dy = 300 - self.sprite.rect.bottom
    
    # update rectangle position
    self.sprite.rect.x += dx
    self.sprite.rect.y += dy

  def update_animation(self):
    self.sprite.update_animation()
 
  def shoot(self):
    if self.shoot_cooldown == 0 and self.ammo > 0: 
      self.shoot_cooldown = 20
      bullet = weapons.Bullet(self.sprite.rect.centerx + (0.6 * self.sprite.rect.size[0] * self.movement.direction), self.sprite.rect.centery, self.movement.direction)
      self.bullet_group.add(bullet)
      # reduce ammo
      self.ammo -= 1

  def draw(self, screen):
   img = pygame.transform.flip(self.sprite.image, self.movement.flip,False)
   screen.blit(img, self.sprite.rect) 

