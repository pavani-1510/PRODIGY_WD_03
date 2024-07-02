# tictactoe_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game

def index(request):
    return render(request, 'index.html')

def new_game(request):
    game = Game.objects.create()
    return redirect('game_detail', game_id=game.id)

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game.html', {'game': game})

def make_move(request, game_id, position):
    game = get_object_or_404(Game, pk=game_id)
    position = int(position)
    if game.board[position] == Game.EMPTY and game.winner == Game.EMPTY and not game.is_draw:
        board = list(game.board)
        board[position] = game.current_turn
        game.board = ''.join(board)
        game.current_turn = Game.PLAYER_O if game.current_turn == Game.PLAYER_X else Game.PLAYER_X
        game.save()

        winner, is_draw = check_winner(game.board)
        if winner:
            game.winner = winner
        game.is_draw = is_draw
        game.save()

    return redirect('game_detail', game_id=game.id)

def check_winner(board):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for positions in winning_positions:
        if board[positions[0]] == board[positions[1]] == board[positions[2]] != Game.EMPTY:
            return board[positions[0]], False

    if Game.EMPTY not in board:
        return Game.EMPTY, True

    return None, False
