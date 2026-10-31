#!/usr/bin/env python3
"""
Spider Weaver - Autonomous Agents Simulation
Spinning simulated spiders that navigate the digital canvas...
"""

import pygame
import random
import math

# Initialize pygame
pygame.init()

# Canvas settings
WIDTH, HEIGHT = 800, 600
FPS = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SPIDER_COLOR = (100, 50, 200)  # Purple for spiders
WEB_COLOR = (200, 180, 255)    # Light purple for web patterns

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spider Weaver - Autonomous Agents")
clock = pygame.time.Clock()

class Spider:
    """An autonomous spider agent navigating the weave"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 8
        # Random velocity
        vx = random.uniform(-2, 2)
        vy = random.uniform(-2, 2)
        self.vx = vx
        self.vy = vy
        
        # Movement behavior
        self.wander_angle = 0
        self.wander_radius = random.uniform(50, 100)
        
    def update(self):
        """Update spider position with gentle wandering"""
        self.x += self.vx
        self.y += self.vy
        
        # Add slight wandering motion
        self.wander_angle += 0.02
        wander_x = math.sin(self.wander_angle) * self.wander_radius * 0.1
        wander_y = math.cos(self.wander_angle) * self.wander_radius * 0.1
        
        self.x += wander_x
        self.y += wander_y
        
        # Keep within canvas bounds (soft bounce)
        if self.x < self.size:
            self.x = self.size
        if self.x > WIDTH - self.size:
            self.x = WIDTH - self.size
        if self.y < self.size:
            self.y = self.size
        if self.y > HEIGHT - self.size:
            self.y = HEIGHT - self.size
            
    def draw(self, surface):
        """Draw the spider"""
        # Draw circular body
        pygame.draw.circle(surface, SPIDER_COLOR, (int(self.x), int(self.y)), self.size)
        
        # Draw simple legs
        leg_positions = [(-15, 10), (-5, -10), (5, -10), (15, 10)]
        for offset_x, offset_y in leg_positions:
            leg_tip_x = self.x + offset_x * math.cos(self.wander_angle)
            leg_tip_y = self.y + offset_y * math.sin(-self.wander_angle)
            pygame.draw.line(surface, WEB_COLOR, 
                           (int(self.x), int(self.y)), 
                           (int(leg_tip_x), int(leg_tip_y)), 2)

def main():
    # Create a swarm of spiders
    spider_count = 15
    spiders = [Spider(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)) 
               for _ in range(spider_count)]
    
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear screen
        screen.fill(BLACK)
        
        # Update and draw each spider
        for spider in spiders:
            spider.update()
            spider.draw(screen)
        
        # Draw web pattern background (random dots connecting to form weave)
        pygame.draw.rect(screen, WEB_COLOR, 
                        (0, 0, WIDTH, HEIGHT), 2)  # Border
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == '__main__':
    main()
