import unittest
import pygame
from Destroyer import Spaceship
from Destroyer import Alien_Bullets
from Destroyer import Explosion

# Test on Screen Display
class TestSpaceInvaders(unittest.TestCase): #This line defines a new test case class named TestSpaceInvaders
    def setUp(self): #This is a special method in unittest that gets called before each test method is executed. 
        pygame.init() #This line initializes all imported Pygame modules. It must be called before any other Pygame functions are used
        self.screen = pygame.display.set_mode((600, 650))
        pygame.display.set_caption('Space Invanders') 

    def test_window_creation(self): ##This is a test method that checks whether the Pygame window was created with the correct dimensions.
        self.assertEqual(self.screen.get_width(), 600)
        self.assertEqual(self.screen.get_height(), 650)

    def test_window_caption(self): #This is another test method that checks whether the Pygame window has the correct title.
        self.assertEqual(pygame.display.get_caption()[0], 'Space Invanders') #This line asserts that the title of the Pygame window is 'Space Invanders'. If the title does not match this value, the test will fail 

# Test on Game Sound
class TestSoundLoading(unittest.TestCase): #This line defines a new test case class named TestSoundLoading that inherits from unittest.TestCase
    def setUp(self): #This is a special method in unittest that gets called before each test method is executed.
        pygame.mixer.init() # This line initializes the Pygame mixer module. 
        self.explosion_fx = pygame.mixer.Sound("explosion.wav")
        self.explosion_fx.set_volume(0.25)
        self.explosion2_fx = pygame.mixer.Sound("explosion2.wav")
        self.explosion2_fx.set_volume(0.25)
        self.laser_fx = pygame.mixer.Sound("laser.wav")
        self.laser_fx.set_volume(0.25)

    def test_sound_loading(self):#This is a test method that checks whether the three sound files were loaded correctly.
        self.assertIsNotNone(self.explosion_fx)
        self.assertIsNotNone(self.explosion2_fx)
        self.assertIsNotNone(self.laser_fx)

    def test_sound_playing(self): # This is another test method that checks whether the three sound files can be played.
        self.explosion_fx.play()
        self.assertTrue(pygame.mixer.get_busy()) #This line asserts that the mixer is busy, i.e., a sound is currently playing. If no sound is playing, the test will fail.
        pygame.time.wait(1000)  # Wait for the sound to finish playing

        self.explosion2_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)  # Wait for the sound to finish playing

        self.laser_fx.play()
        self.assertTrue(pygame.mixer.get_busy())
        pygame.time.wait(1000)  # Wait for the sound to finish playing

class TestGameInitialization(unittest.TestCase): # This line defines a new test case class named TestGameInitialization that inherits from unittest.TestCase
    def setUp(self): #This is a special method in unittest that gets called before each test method is executed.
        pygame.init()#This line initializes all imported Pygame modules. It must be called before any other Pygame functions are used
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

    def test_game_variables(self): #This is a test method that checks whether the game variables were initialized correctly.
        self.assertEqual(self.rows, 5)
        self.assertEqual(self.cols, 5)
        self.assertEqual(self.alien_cooldown, 1000)
        self.assertEqual(self.game_over, 0)

    def test_colors(self): #This is another test method that checks whether the colors were initialized correctly.
        self.assertEqual(self.red, (255, 0, 0))
        self.assertEqual(self.green, (0, 255, 0))
        self.assertEqual(self.white, (255, 255, 255))

    def test_bg_loading(self): # This is a test method that checks whether the background image was loaded correctly.
        self.assertIsNotNone(self.bg)

# Test on Spaceship
class TestSpaceship(unittest.TestCase): #This line defines a new test case class named TestSpaceship that inherits from unittest.TestCase
    def setUp(self): #def setUp(self): This is a special method in unittest that gets called before each test method is executed.
        pygame.init()#This line initializes all imported Pygame modules. It must be called before any other Pygame functions are used
        self.spaceship = Spaceship(300, 300, 100)

    def test_spaceship_creation(self):#This is a test method that checks whether the spaceship was created correctly.
        self.assertIsNotNone(self.spaceship)#This line asserts that the spaceship object is not None. If the spaceship object is None, the test will fail.
        self.assertEqual(self.spaceship.rect.center, (300, 300))
        self.assertEqual(self.spaceship.health_start, 100)
        self.assertEqual(self.spaceship.health_remaining, 100)

# Test on Alien Bullet
class TestAlienBullets(unittest.TestCase): #This line defines a new test case class named TestAlienBullets that inherits from unittest.TestCase
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.alien_bullet = Alien_Bullets(400, 300)

    def test_init(self): # This is a test method that checks whether the alien bullet was created correctly.
        self.assertIsInstance(self.alien_bullet, pygame.sprite.Sprite)#This line asserts that the alien bullet object is an instance of pygame.sprite.Sprite. If the object is not an instance of pygame.sprite.Sprite, the test will fail
        self.assertEqual(self.alien_bullet.rect.center, (400, 300))

    def tearDown(self): #This is a special method in unittest that gets called after each test method is executed. It's typically used to clean up any state that was set up for the tests.
        pygame.quit() #This line quits all Pygame modules that were initialized, freeing up any resources they were using 

# Test on Explosion
class TestExplosion(unittest.TestCase): #This line defines a new test case class named TestExplosion that inherits from unittest.TestCase
    def setUp(self): #This is a special method in unittest that gets called before each test method is executed.
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.explosion = Explosion(400, 300, 1)

    def test_init(self): #This is a test method that checks whether the explosion was created correctly.
        self.assertIsInstance(self.explosion, pygame.sprite.Sprite)#This line asserts that the explosion object is an instance of pygame.sprite.Sprite. If the object is not an instance of pygame.sprite.Sprite, the test will fail
        self.assertEqual(self.explosion.rect.center, (400, 300))#This line asserts that the center of the explosion's rectangle is at the coordinates (400, 300). If the center is not at these coordinates, the test will fail.
        self.assertEqual(self.explosion.counter, 0)#This line asserts that the counter of the explosion is 0. If the counter is not 0, the test will fail.

    def tearDown(self): # #This is a special method in unittest that gets called after each test method is executed. It's typically used to clean up any state that was set up for the tests.
        pygame.quit()

# Test on Countdown timer
class TestGame(unittest.TestCase):#This line defines a new test case class named TestGame that inherits from unittest.TestCase
 def setUp(self):
   pygame.init()
   self.screen = pygame.display.set_mode((800, 600))
   self.countdown = 5
   self.last_count = pygame.time.get_ticks()

 def test_countdown(self): #This is a test method that checks whether the countdown feature works correctly.
   self.assertEqual(self.countdown, 5)#This line asserts that the countdown is initially 5. If the countdown is not 5, the test will fail.
   count_timer = pygame.time.get_ticks()
   if count_timer - self.last_count > 1000:
     self.countdown -= 1
     self.last_count = count_timer
   self.assertEqual(self.countdown, 5)#This line asserts that the countdown is still 5. If the countdown is not 5, the test will fail.

 def tearDown(self):
   pygame.quit()

# Test on Event handler
class TestGame(unittest.TestCase):# This line defines a new test case class named TestGame that inherits from unittest.TestCase
 def setUp(self): #This is a special method in unittest that gets called before each test method is executed.
   pygame.init() #This line initializes all imported Pygame modules. It must be called before any other Pygame functions are used
   self.screen = pygame.display.set_mode((800, 600))
   self.run = True #This line sets up a game loop control variable.

 def test_event_handling(self): #This is a test method that checks whether the event handling feature works correctly.
   event = pygame.event.Event(pygame.QUIT)#These lines create a new Pygame QUIT event and post it to the event queue
   pygame.event.post(event)
   for event in pygame.event.get():
     if event.type == pygame.QUIT: #This line checks if the event is a QUIT event.
       self.run = False #This line sets the game loop control variable to False, indicating that the game should stop running.
   self.assertEqual(self.run, False) # This line asserts that the game loop control variable is False. If the game loop control variable is not False, the test will fail.

 def tearDown(self): #This is a special method in unittest that gets called after each test method is executed.
   pygame.quit() #This line quits all Pygame modules that were initialized, freeing up any resources they were using


if __name__ == '__main__': #This is a common Python idiom. The __name__ variable is a special built-in variable in Python,
#which is automatically set to the name of the module. When a module is run directly, the __name__ variable is set to '__main__'. When a module is imported, the __name__ variable is set to the name of the module. Therefore, the code inside the if __name__ == '__main__': block is only executed when the module is run directly, not when it is imported
    unittest.main() #This line runs the unit test suite.