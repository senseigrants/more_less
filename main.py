class More_less:
    '''A game where the user will think of a integer within a certain range and the program will try to guess.
    The user will each time tell if the guess is correct, or if it's less or more.'''

    def invert(self, a, b):
        '''Returns two integers inverted.'''

        return (b, a)

    def get_int(self, question):
        '''Asks the user a question, and makes sure the answer is an integer.'''

        user_input = ''
        while not isinstance(user_input, int):
            user_input = input(question)
            try:
                user_input = int(user_input)
            except ValueError:
                print('Wrong input. The value should be an integer only !')
        return user_input
        
    def get_range(self):
        '''Asks the user the range of integers to guess.'''

        self.min = self.get_int('\nEnter the value of X: ')
        self.max = self.get_int('\nEnter the value of Y: ')

        if self.min > self.max:
            print('You inputed X as greater than Y, I will invert them.')
            self.min, self.max = self.invert(self.min, self.max)


    def start_menu(self):
        '''Shows the start menu of the game.'''
        
        print('Hello and welcome to the More/Less game !')
        print('In this game, you will enter two integers X and Y,')
        print('and then think about an integer between X and Y.')
        print('I will try to guess it, and you tell me if it\'s your')
        print('number is higher, lower, or equal to mine !')


    def start_guess(self):
        '''Starts to guess the number.'''

        answer = previous = ''

        while answer != '=':
            next = int(self.min + (self.max-self.min) // 2)

            if previous == next:
                print('\nHey ! You scammed me !')
                return False
            
            print(f'\nAre you thinking of {next}?')
            answer = input('Answer \'+\' or \'-\' or \'=\' : ')
            
            if answer == '+':
                self.min = next
            elif answer == '-':
                self.max = next
            elif answer != '=':
                print('Wrong input.')
            previous = next
        
        print('\nYay !')
        return True


    def play(self):
        '''Launches the game'''

        self.start_menu()        
        self.get_range()
        print(f'\nThink about an integer from {self.min} to {self.max}. I will try to guess it !')
        answer = ''

        while answer not in ['0', '1']:
            answer = input('\nEnter 1 to start, 0 to quit: ')

            if answer == '1':
                endgame = self.start_guess()

                if endgame:
                    print('\nThanks for the fun !')
                else:
                    print('\nThanks tho, is was still fun !')

            elif answer == '0':
                print('\nHope to see you soon !')

            else:
                print('Wrong input.')

game = More_less()
game.play()