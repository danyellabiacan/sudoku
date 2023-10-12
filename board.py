import pygame
import sudoku_game
from values import*
from buttons import*

class board():
	# basically a python constructor
	def __init__(self):
		pygame.init() 											# initialize pygame
		self.screen = pygame.display.set_mode([WIDTH, HEIGHT])	# initialize the screen
		self.screen.fill(DARK_GREY)                             # fill the screen with dark grey
		self.grid = sudoku_game.hidden_board
		self.cell = (0, 0) 										# initialize cell coordinates
		self.draw_board() 										# call draw_board()

	# prints the grid contents to the terminal
	def print_board(self):
		for row in range(9):										# for row #'s' 0 - 8
			if row % 3 == 0: 										# if the row # is divisible by 3
				print("+-------+-------+-------+") 					# print top border
			for column in range(9): 								# for column #'s 0 - 9
				if column % 3 == 0: 								# if the column # is divisible by 3
					print("| ", end = '') 							# print a 3x3 divider
				print(self.grid[row][column], end = ' ') 			# otherwise, print the next column as usual
				if column == 8: 									# if the column # is 8
					print("|", end = '') 							# print righthand border
			if row == 8: 											# if the row # is 8
				print("\n+-------+-------+-------+") 				# print the bottom border
			print('\n', end = '') 									# new line

	# checks if the input is valid
	def valid_input(self, row, column, number):
		for value in range((row // 3) * 3, (row // 3) * 3 + 3):					# will check if the user input already
			for num in range((column // 3) * 3, (column // 3) * 3 + 3): 		# exists in the grid array
				if self.grid[value][num] == number: 							# if it does
					return False 												# return False

		for value in range(9): 													# will check if the user input already exists
			if self.grid[row][value] == number: 								# within it's row and column
				return False
			if self.grid[value][column] == number: 								# if so, return False
				return False

		return True 															# otherwise, return True

	# resets the board to be empty
	def reset_board(self):
		self.grid = [[0] * 9 for numbers in range(9)] 							# creates 9 lists containing 9 values that are all 0
		self.draw_board() 														# will update the window

	# will insert the user input into the grid array
	def insert_number(self, number):
		self.grid[self.cell[0]][self.cell[1]] = number 							# will change the index in the grid array into the user input
		self.draw_board() 														# will update the window

	# will set the selected cell coordinates to the mouse click position
	def choose_cell(self, position):
		self.cell = position 													# will set cell to the selected position

	# prints the grid contents onto the window and draws the grid lines
	def draw_board(self):
		for row in range(9):
			for column in range(9): 											# prints the contents of grid onto the window
				pygame.draw.rect(self.screen, MED_GREY, ((column * cell_size) + 25, (row * cell_size) + 25, cell_size + 1, cell_size + 1)) # draws the grid background
				if self.grid[row][column]: 										# if the grid index has a value (not 0)
					font = pygame.font.SysFont('arial', 40) 					# will render the index contents into a string and print it to the board
					number = font.render(str(self.grid[row][column]), 1, BRIGHT_WHITE)
					self.screen.blit(number, (column * cell_size + 40, row * cell_size + 28))

		pygame.draw.rect(self.screen, WHITE, (board_pos[0], board_pos[1], WIDTH - 50, HEIGHT - 50), 3) # draws the grid border
		for position in range(9):                               # while position < 9
			if position % 3 != 0:                               # if the position is not divisible by 3
				pygame.draw.line(self.screen, WHITE, (board_pos[0] + (position * cell_size), board_pos[1]), (board_pos[0] + (position * cell_size), board_pos[1] + (HEIGHT - 50))) # create vertical line
				pygame.draw.line(self.screen, WHITE, (board_pos[0], board_pos[1] + (position * cell_size)), (board_pos[0] + (WIDTH - 50), board_pos[1] + (position * cell_size))) # create horizontal line
			else:                                               # otherwise
				pygame.draw.line(self.screen, WHITE, (board_pos[0] + (position * cell_size), board_pos[1]), (board_pos[0] + (position * cell_size), board_pos[1] + (HEIGHT - 50)), 3) # create a thicker vertical line
				pygame.draw.line(self.screen, WHITE, (board_pos[0], board_pos[1] + (position * cell_size)), (board_pos[0] + (WIDTH - 50), board_pos[1] + (position * cell_size)), 3) # create a thicker horizontal line
				
		pygame.display.update() 								# updates the display