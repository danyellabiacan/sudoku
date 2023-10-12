import pygame 				# imports pygame
from values import* 		# imports everything from values
from board import* 			# imports everything from board class
from sudoku_game import*	# imports everything from alex's file

class game():
	def __init__(self):
		self.screen = pygame.display.set_mode([WIDTH, HEIGHT]) 			# initialize the program screen
		self.running = True 											# initialize running to True
		self.board = board() 											# create an instance of the board class
		self.user_input = 0 											# set user_input to 0
		self.pos = False 												# initialize pos to False

	def run(self):
		while self.running: 											# will run until the running flag turns False
			self.board.draw_board() 									# updates the board in the case that the program stalls midway
			self.check_events() 										# will call check_events until the user quits or presses escape

		pygame.quit() 													# will quit pygame
		quit() 															# will exit the program

	def check_events(self):												# will check the event queue and decide the next course of action
		for event in pygame.event.get(): 								# for every event in the event queue
			if event.type == pygame.QUIT: 								# if the user quits (window's x)
				print("Thank you for playing!")
				self.running = False 									# set running to False

			if event.type == pygame.KEYDOWN: 							# if a key is pressed
				if event.key == pygame.K_ESCAPE: 						# if the key is ESCAPE
					print("Thank you for playing!")
					self.running = False 								# set running to False
					pygame.quit() 										# quit pygame
					quit() 												# quit program
				if event.key == pygame.K_c: 							# if the key is 'c'
					print("Can't clear this board; game specific!")		# the board is cleared by calling reset_board()
				if self.pos: 											# if a position has been set
					if event.key == pygame.K_1: 						# if the player pressed 1
						self.user_input = 1 							# stores 1 as the input
						print("Press enter to update the cell to 1.")
					if event.key == pygame.K_2: 						# if the player pressed 2
						self.user_input = 2 							# stores 2 as the input
						print("Press enter to update the cell to 2.")
					if event.key == pygame.K_3: 						# if the player pressed 3
						self.user_input = 3 							# stores 3 as the input
						print("Press enter to update the cell to 3.")
					if event.key == pygame.K_4: 						# if the player pressed 4
						self.user_input = 4 							# store 4 as the input
						print("Press enter to update the cell to 4.")
					if event.key == pygame.K_5: 						# if the player pressed 5
						self.user_input = 5 							# store 5 as the input
						print("Press enter to update the cell to 5.")
					if event.key == pygame.K_6: 						# if the player pressed 6
						self.user_input = 6 							# store 6 as the input
						print("Press enter to update the cell to 6.")
					if event.key == pygame.K_7: 						# if the player pressed 7
						self.user_input = 7 							# store 7 as the input
						print("Press enter to update the cell to 7.")
					if event.key == pygame.K_8: 						# if the player pressed 8
						self.user_input = 8 							# store 8 as the input
						print("Press enter to update the cell to 8.")
					if event.key == pygame.K_9: 						# if the player pressed 9
						self.user_input = 9 							# store 9 as the input
						print("Press enter to update the cell to 9.")
					if event.key == pygame.K_DELETE: 					# if the player pressed delete
						print("Can't delete cells; game specific!")		# Error message.
					if event.key == pygame.K_RETURN: 					# if the player pressed return
						if sudoku_game.full_board[self.pos[0]][self.pos[1]] == self.user_input: # and if the input is valid
							self.board.insert_number(self.user_input) 	# store the input into the grid
							print("Valid input!")
						else: 											# otherwise
							print("Invalid input!") 					# print "Invalid input!" to the terminal

			if event.type == pygame.MOUSEBUTTONDOWN: 					# if a mouse button is pressed
				if pygame.mouse.get_pressed()[0]: 						# if the left mouse button is pressed
					pos = pygame.mouse.get_pos() 						# get the mouse position
					pos = (int((pos[1] - 25) // cell_size), int((pos[0] - 25) // cell_size)) # update the position to be the actual array indicies
					if pos[0] >= 0 and pos[0] < 9 and pos[1] >= 0 and pos[1] < 9: # if the position is 0 - 8 on both x and y axes
						self.pos = pos 									# set position as the pos
						self.board.cell = pos 							# set the board cell as pos
						print(f"You've selected cell {pos[0] + 1}, {pos[1] + 1}") # let the user know what cell they chose on the terminal