import time
import random

print('-'*65)
print('I am a Magic Eight Ball!')
print()
question = input('What is your question? ')
time.sleep(0.7)
print('Shaking!')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)
print('...thinking...')
time.sleep(0.7)

choice = random.randint(1,4)

if choice == 1:
	print('Happy Trails, Hans')
elif choice == 2:
		print ('Yippee-Ki-Yay')
elif choice == 3:
	print('I Must Break You')
elif choice == 4:
	print('My Name Is Inigo Montoya')