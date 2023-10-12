from menu import* 						# imports everything from menu
from sudoku_game import* 				# imports everything from sudoku_game
from sudoku_solver import* 				# imports everything from sudoku_solver
from game import*						# imports everything from game

if __name__ == "__main__":
	running = True 						# set running to True
	while running: 						# while program is running
		menu = menu() 					# create an instance of menu
		menu.display_menu() 			# call displlay_menu() from the menu class
		if menu.option == 1:			# if the menu option is 1
			game = game() 				# create an instance of the game class
			game.run() 					# call game.run()
		if menu.option == 2:			# if the menu option is 2
			solver = solver() 			# create an instance of solver from the solver class
			solver.run() 				# call the solver's run function