from Live import load_game, welcome
name = input('Enter Your Name:')
print(welcome(name))
win = False
#initialzing win condition
while win == False:
    win = load_game()
print('Have a Nice Day, come play again...')
