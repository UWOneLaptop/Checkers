# Unit Tests
# Josh Scotland

import GameState
import unittest

# Class to test the game state
class TestGameState(unittest.TestCase):

    def testGameBegin(self):
        gs = GameState()
        self.assertEqual(gs.get_state(), 0)

    def testBlacksTurn(self):
        gs = GameState()
        gs.set_state(gs.BlacksTurn)
        self.assertEqual(gs.get_state(), 2)

    def testReset(self):
        gs = GameState()
        gs.set_state(gs.BlacksTurn)
        gs.reset()
        self.assertEqual(gs.get_state(), 0)

if __name__ == '__main__':
    unittest.main()
