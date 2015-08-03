
import unittest
#from leHavreGame import Game

class Game:
    def __init__(self):
        self._resources = {'Franc': 0, 'Wood': 0, 'Clay': 0}
        
    @property
    def resources(self):
        return self._resources
    
    @resources.setter
    def resources(self, resources):
        self._resources = resources

        
class leHavreGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        
    def testStartResource(self):
        self.assertEqual(self.game.resources['Franc'], 0)
        self.assertEqual(self.game.resources['Wood'], 0)

    
    def testSetResource(self):
        self.game.resources['Franc'] = 1
        self.assertEqual(self.game.resources['Franc'], 1)
        self.assertEqual(self.game.resources['Wood'], 0)
        

if __name__ == "__main__":
    unittest.main()