import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        
        direction = player.status
        print(direction)
        
        # graphic
        full_path = f'graphics/weapons/{player.weapon}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        
        # placement
        if direction == 'right':
            self.rect = self.image.get_rect(center = player.rect.midright + pygame.math.Vector2(16,0))
        elif direction == 'left':
            self.rect = self.image.get_rect(center = player.rect.midleft - pygame.math.Vector2(16,0))
        elif direction == 'up':
            self.rect = self.image.get_rect(center = player.rect.midtop + pygame.math.Vector2(16,0))
        else:
            self.rect = self.image.get_rect(center = player.rect.midbottom - pygame.math.Vector2(16,0))