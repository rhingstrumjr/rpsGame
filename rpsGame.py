#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random
moves = ['rock', 'paper', 'scissors', 'lizard', 'Spock']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

# This is a random Player


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

# This is a Human Player


class HumanPlayer(Player):
    def move(self):
        self.h_move = input("Choose rock, paper, scissors, lizard or Spock: ")
        while self.h_move not in moves:
            self.h_move = input("Sorry.  I don't recognize that move.  Please "
                                + "choose 'rock', 'paper', 'scissors', "
                                + "'lizard', or 'Spock'. ")
        return self.h_move


"""This player starts with a random move,
then copies the last move of the other player."""


class ReflectPlayer(Player):
    def __init__(self):
        self.move_choice = random.choice(moves)

    def move(self):
        return self.move_choice

    def learn(self, my_move, their_move):
        self.move_choice = their_move


"""This player plays a continous sequence of rock, paper, scissors,
lizard and Spock."""


class CyclePlayer(Player):
    def __init__(self):
        self.c_count = 0

    def move(self):
        if self.c_count < 4:
            self.c_count += 1
            return moves[self.c_count - 1]
        else:
            self.c_count = 0
            return moves[4]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'lizard') or
            (one == 'paper' and two == 'Spock') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'Spock' and two == 'rock') or
            (one == 'Spock' and two == 'scissors') or
            (one == 'lizard' and two == 'Spock') or
            (one == 'lizard' and two == 'paper'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1_score += 1
            print("Player 1 won the round!")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print("Player 2 won the round!")
        else:
            print("The round was a tie.")
        print(f"P1\'s score: {self.p1_score} P2\'s score: {self.p2_score}\n")

    def play_game(self):
        print("Game start!\nBest of 3 game!\n")
        round = 1
        while self.p1_score < 2 and self.p2_score < 2:
            print(f"Round {round}:")
            round += 1
            if round == 101:
                print("The two players are an even match!")
                return
            self.play_round()
        if self.p1_score == 2:
            print(f"Game over! Player 1 wins {self.p1_score} " +
                  f"to {self.p2_score}!")
        else:
            print(f"Game over! Player 2 wins {self.p2_score} " +
                  f"to {self.p1_score}!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
