import pygame 				# import pygame module
from buttons import* 		# import all of the buttons class
from values import* 		# import all of the values class

class menu():
	# like a constructor, will initialize all variable when an instance of the class is created
	def __init__(self):
		pygame.init() 											# initialize pygame
		self.screen = pygame.display.set_mode([WIDTH, HEIGHT]) 	# initialize the window dimensions
		pygame.display.set_caption("SUDOKU SOLVER (DB)")        # set program caption
		self.screen.fill(DARK_GREY) 							# fill the screen as dark grey
		self.option = False 									# initialize option as False
		self.running = True 									# initialize option as True
		self.how_to_play() 										# call how_to_play() to display instructions on the terminal
		self.start_button = buttons(LIGHT_GREY, WIDTH / 3.6, HEIGHT / 3, 230, 40, "START GAME") # create the start button
		self.solve_button = buttons(LIGHT_GREY, WIDTH / 3.6, HEIGHT / 3 + 50, 230, 40, "SOLVE A PUZZLE") # create the solve button 
		self.quit_button = buttons(LIGHT_GREY, WIDTH / 3.6, HEIGHT / 3 + 100, 230, 40, "QUIT") # create the quit button

	# will redraw the window
	def redraw_window(self):
		self.screen.fill(DARK_GREY) 							# fills they screen to dark grey
		self.start_button.draw_button(self.screen) 				# draws the start button
		self.solve_button.draw_button(self.screen) 				# draws the solve button
		self.quit_button.draw_button(self.screen) 				# draws the draw button

	# will display the menu until an option has been selected
	def display_menu(self):
		while self.running: 									# while running is True
			self.redraw_window() 								# call redraw_window() to draw the menu
			pygame.display.update() 							# update the display
			self.check_events() 								# call check_events() to check for events in the queue

	# will print out the program instructions
	def how_to_play(self): 
		with open('how_to_play.txt', 'r') as instructions: 		# opens the how_to_play.txt file as instructions
			how_to_play = instructions.read() 					# reads the contents of how_to_play.txt into how_to_play
		print(how_to_play) 										# prints the contents of the text file

	# will check the event queue to see the next course of action based on user input
	def check_events(self):
		for event in pygame.event.get(): 						# for every event in the event queue
			pos = pygame.mouse.get_pos() 						# get the position of the mouse

			if event.type == pygame.QUIT: 						# if the user exits the program using the window's x
				print("\nSee you next time!")
				self.running = False 							# set running to False
				pygame.quit() 									# quit pygame
				quit() 											# quit program

			if event.type == pygame.KEYDOWN: 					# if the user presses a key down
				if event.key == pygame.K_ESCAPE: 				# if the key is ESC
					print("\nSee you next time!")
					self.unning = False 						# set running to False
					pygame.quit() 								# quit pygame
					quit() 										# quit program

			if event.type == pygame.MOUSEBUTTONDOWN: 			# if the user presses a mouse button
				if self.start_button.is_hovering(pos):			# check if the mouse is over the button
					print("\nBoard is generated.\n") 			# let the user know that the board is generated
					self.option = 1 							# set option to 2
					self.running = False						# self running to False

				if self.solve_button.is_hovering(pos): 			# check if the mouse is over the button by calling the button class' function is_hovering
					print("\nPress 's' to solve or press 'c' to clear the board")
					print("and insert your generated Sudoku puzzle.\n") # prompt to insert the generated puzzle
					self.option = 2 							# set option to 2
					self.running = False 						# set running to False

				if self.quit_button.is_hovering(pos): 			# check if the mouse is over the button by calling the button class' function is_hovering
					print("\nSee you next time!") 				# print thank you for playing to the terminal
					pygame.quit() 								# quit pygame
					quit() 										# quit the program

			if event.type == pygame.MOUSEMOTION:				# if the mouse is moving
				if self.start_button.is_hovering(pos):			# check if the mouse is hovering over the button
					self.start_button.color = MED_GREY 			# if True, make the button darker
				else: 											# otherwise
					self.start_button.color = LIGHT_GREY 		# keep it the same color

				if self.solve_button.is_hovering(pos):			# check if the mouse is hovering over the button
					self.solve_button.color = MED_GREY			# if True, make the button darker
				else:											# otherwise
					self.solve_button.color = LIGHT_GREY 		# keep it the same color

				if self.quit_button.is_hovering(pos): 			# check if the mouse is hovering over the button
					self.quit_button.color = MED_GREY 			# if True, make the button darker
				else: 											# otherwise
					self.quit_button.color = LIGHT_GREY 		# keep it the same color
