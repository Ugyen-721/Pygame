import unittest
import pygame

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

class TestSpaceInvaders(unittest.TestCase):
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
        self.assertTrue(self.explosion_fx.get_busy())
        self.explosion_fx.stop()

        self.explosion2_fx.play()
        self.assertTrue(self.explosion2_fx.get_busy())
        self.explosion2_fx.stop()

        self.laser_fx.play()
        self.assertTrue(self.laser_fx.get_busy())
        self.laser_fx.stop()



if __name__ == '__main__':
    unittest.main()