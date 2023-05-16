import pygame

#gun properties
class Stats():
    """statistics"""
    def __init__(self):
        """stat init"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """changes"""
        self.guns_left = 2
        self.score = 0
