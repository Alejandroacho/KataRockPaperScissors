import unittest
from PaperRockScissors import *
from mock import patch

class MyTestCase(unittest.TestCase):
"""    
    @patch('PaperRockScissors.inputComprover')
    def test_called(self, mock):
        game=PaperRockScissors()
        game.start()
        self.assertTrue(mock.called)
"""    
    def test_dont__admit_letters(self):
        game = PaperRockScissors()
        result = game.inputComprover('a')
        self.assertEqual(False, result)
    
    def test_dont__admit_numbers_out_of_rules(self):
        game = PaperRockScissors()
        result = game.inputComprover(0)
        self.assertEqual(False, result)

    def test_dont__admit_numbers_out_of_rules_2(self):
        game = PaperRockScissors()
        result = game.inputComprover(4)
        self.assertEqual(False, result)
    
    def test_admit_valid_numbers(self):
        game = PaperRockScissors()
        result = game.inputComprover(2)
        self.assertEqual(True, result)
    
    def test_admit_valid_numbers_2(self):
        game = PaperRockScissors()
        result = game.inputComprover(1)
        self.assertEqual(True, result)
    
    def test_draw(self):
        game = PaperRockScissors()
        result = game.winnerComprover(1,1)
        self.assertEqual("Empate", result)
    
    def test_draw_2(self):
        game = PaperRockScissors()
        result = game.winnerComprover(2,2)
        self.assertEqual("Empate", result)

    def test_draw_3(self):
        game = PaperRockScissors()
        result = game.winnerComprover(3,3)
        self.assertEqual("Empate", result)
    
    def test_paper_wins_over_rock(self):
        game = PaperRockScissors()
        result = game.winnerComprover(1,2)
        self.assertEqual("Player 1 wins", result)

    def test_paper_wins_over_rock_2(self):
        game = PaperRockScissors()
        result = game.winnerComprover(2,1)
        self.assertEqual("Player 2 wins", result)
    
    def test_rock_wins_over_scissors(self):
        game = PaperRockScissors()
        result = game.winnerComprover(2,3)
        self.assertEqual("Player 1 wins", result)
    
    def test_rock_wins_over_scissors_2(self):
        game = PaperRockScissors()
        result = game.winnerComprover(3,2)
        self.assertEqual("Player 2 wins", result)
    
    def test_scissors_wins_over_paper(self):
        game = PaperRockScissors()
        result = game.winnerComprover(3,1)
        self.assertEqual("Player 1 wins", result)
    
    def test_scissors_wins_over_paper_2(self):
        game = PaperRockScissors()
        result = game.winnerComprover(1, 3)
        self.assertEqual("Player 2 wins", result)
    