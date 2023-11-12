import unittest
import pygame
from Destroyer import Spaceship
from Destroyer import Alien_Bullets
from Destroyer import Explosion


class TestSpaceInvaders(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 650))
        pygame.display.set_caption('Space Invanders')

    def test_window_creation(self):
        self.assertEqual(self.screen.get_width(), 600)
        self.assertEqual(self.screen.get_height(), 650)

    def test_window_caption(self):
        self.assertEqual(pygame.display.get_caption()[0], 'Space Invanders')

class TestSoundLoading(unittest.TestCase):
    def setUp(self):
        pygame.mixer.init()
        self.explosion_fx = pygame.mixer.Sound("explosion.wav")
        self.explosion_fx.set_volume(0.25)
        self.explosion2_fx = pygame.mixer.Sound("explosion2.wav")
        self.explosion2_fx.set_volume(0.25)
        self.laser_fx = pygame.mixer.Sound("laser.wav")
        self.laser_fx.set_volume(0.25)

    def test_sound_loading(self):
        self.assertIsNotNone(self.explosion_fx)
        self.assertIsNotNone(self.explosion2_fx)
        self.assertIsNotNone(self.laser_fx)

    def test_sound_playing(self):
        self.explosion_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)  # Wait for the sound to finish playing

        self.explosion2_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)  # Wait for the sound to finish playing

        self.laser_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)  # Wait for the sound to finish playing

class TestGameInitialization(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.rows = 5
        self.cols = 5
        self.alien_cooldown = 1000
        self.last_alien_shot = pygame.time.get_ticks()
        self.countdown = 3
        self.last_count = pygame.time.get_ticks()
        self.game_over = 0
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.bg = pygame.image.load("bg.png")

    def test_game_variables(self):
        self.assertEqual(self.rows, 5)
        self.assertEqual(self.cols, 5)
        self.assertEqual(self.alien_cooldown, 1000)
        self.assertEqual(self.game_over, 0)

    def test_colors(self):
        self.assertEqual(self.red, (255, 0, 0))
        self.assertEqual(self.green, (0, 255, 0))
        self.assertEqual(self.white, (255, 255, 255))

    def test_bg_loading(self):
        self.assertIsNotNone(self.bg)

class TestSpaceship(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.spaceship = Spaceship(300, 300, 100)

    def test_spaceship_creation(self):
        self.assertIsNotNone(self.spaceship)
        self.assertEqual(self.spaceship.rect.center, (300, 300))
        self.assertEqual(self.spaceship.health_start, 100)
        self.assertEqual(self.spaceship.health_remaining, 100)

class TestAlienBullets(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.alien_bullet = Alien_Bullets(400, 300)

    def test_init(self):
        self.assertIsInstance(self.alien_bullet, pygame.sprite.Sprite)
        self.assertEqual(self.alien_bullet.rect.center, (400, 300))

    def tearDown(self):
        pygame.quit()

class TestExplosion(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.explosion = Explosion(400, 300, 1)

    def test_init(self):
        self.assertIsInstance(self.explosion, pygame.sprite.Sprite)
        self.assertEqual(self.explosion.rect.center, (400, 300))
        self.assertEqual(self.explosion.counter, 0)

    def tearDown(self):
        pygame.quit()

class TestGame(unittest.TestCase):
 def setUp(self):
   pygame.init()
   self.screen = pygame.display.set_mode((800, 600))
   self.countdown = 5
   self.last_count = pygame.time.get_ticks()

 def test_countdown(self):
   self.assertEqual(self.countdown, 5)
   count_timer = pygame.time.get_ticks()
   if count_timer - self.last_count > 1000:
     self.countdown -= 1
     self.last_count = count_timer
   self.assertEqual(self.countdown, 5)

 def tearDown(self):
   pygame.quit()


class TestGame(unittest.TestCase):
 def setUp(self):
   pygame.init()
   self.screen = pygame.display.set_mode((800, 600))
   self.run = True

 def test_event_handling(self):
   event = pygame.event.Event(pygame.QUIT)
   pygame.event.post(event)
   for event in pygame.event.get():
     if event.type == pygame.QUIT:
       self.run = False
   self.assertEqual(self.run, False)

 def tearDown(self):
   pygame.quit()


if __name__ == '__main__':
    unittest.main()