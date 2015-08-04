
import unittest
#from leHavreGame import Game

class Game:
    def __init__(self):
        self._resources = Resource()
        
    @property
    def resources(self):
        return self._resources
    
    @resources.setter
    def resources(self, resources):
        self._resources = resources

        
class Player:
    def score(self):
        pass

    
class Resource:
    def __init__(self):
        self.franc = 0
        self.wood = 0
        self.clay = 0

        
class leHavreGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        
    def testStartResource(self):
        self.assertEqual(self.game.resources.franc, 0)
        self.assertEqual(self.game.resources.wood, 0)
    
    def testSetResource(self):
        self.game.resources.franc = 1
        self.assertEqual(self.game.resources.franc, 1)
        self.assertEqual(self.game.resources.wood, 0)
        

if __name__ == "__main__":
    unittest.main()