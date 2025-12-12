from parts import Board

game = Board()
game.display()
game.make_move(1, 1, 'X')
game.make_move(2, 1, '0')
print('Ход сделан!')
game.display()
