import pygame
import globals
import soldier

if __name__ == "__main__": 
    globals.initialize() 

pygame.init()
screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
pygame.display.set_caption('Shooter')


clock = pygame.time.Clock()
player = soldier.Soldier('player', 200, 200, 3, 5, 5)
enemy = soldier.Soldier('enemy', 400, 200, 3, 5, 20)

def draw_bg():
  screen.fill(globals.BACKGROUNDCOLOR)
  pygame.draw.line(screen, globals.RED, (0, 300), (globals.SCREEN_WIDTH, 300))



run = True
while run:
  draw_bg()

  clock.tick(globals.FPS)

  enemies = [enemy]

  player.update(player,enemies)
  player.draw(screen)
  player.move()

  enemy.draw(screen)

  # draw groups
  player.bullet_group.draw(screen)
  
  if player.alive:
    if player.shooting:
      player.shoot()
    elif player.movement.in_air:
      player.sprite.update_action(2) #2: jump
    elif player.movement.moving_left or player.movement.moving_right:
      player.sprite.update_action(1) #1: run
    else:
      player.sprite.update_action(0) #0: idel

  for event in pygame.event.get():
    # keyboard presses
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        player.movement.moving_left = True
      if event.key == pygame.K_d :
        player.movement.moving_right = True
      if event.key == pygame.K_w and player.able_to_jump():
        player.movement.jumping = True
      if event.key == pygame.K_SPACE:
        player.shooting = True
      if event.key == pygame.K_ESCAPE:
        run = False
    
    if event.type == pygame.KEYUP :
      if event.key == pygame.K_a :
        player.movement.moving_left = False
      if event.key == pygame.K_d :
        player.movement.moving_right = False
      if event.key == pygame.K_SPACE:
        player.shooting = False

    # quit game
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()

pygame.quit()