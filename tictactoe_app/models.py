# tictactoe_app/models.py
from django.db import models

class Game(models.Model):
    PLAYER_X = 'X'
    PLAYER_O = 'O'
    EMPTY = ' '
    STATUS_CHOICES = [
        (PLAYER_X, 'Player X'),
        (PLAYER_O, 'Player O'),
        (EMPTY, 'Empty'),
    ]

    board = models.CharField(max_length=9, default=EMPTY*9)
    current_turn = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PLAYER_X)
    winner = models.CharField(max_length=1, choices=STATUS_CHOICES, default=EMPTY)
    is_draw = models.BooleanField(default=False)

    def __str__(self):
        return self.board
