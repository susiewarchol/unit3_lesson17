import time
import random

print()
print('-' * 60)
print('A wild Eevee appears!')
time.sleep(0.2)
print('You have only one Pokémon, Snorlax.')
time.sleep(0.2)
print('I choose you Snorlax!!')
print()
time.sleep(0.2)

#starting HPs
snorlax_hp = 200
eevee_hp = 125

while snorlax_hp > 0 and eevee_hp > 0:
	print('Battle Options:')
	time.sleep(0.2)
	print('- [1] Sleep 💤 ')
	time.sleep(0.2)
	print('- [2] Tackle 👊 ')
	time.sleep(0.2)
	print('- [3] Roundhouse Kick 🏃 ')
	time.sleep(0.2)
	print('- [4] Hyper Beam 💫 ')
	time.sleep(0.2)
	print('- [5] Capture 📸 ')

	your_move = input('Choose a move using the corresponding number:')
	if your_move == '1':
		snorlax_hp = snorlax_hp + 50 
		print('Snorlax uses Sleep Heal, HP increases to ' + str(snorlax_hp))
	time.sleep(0.2)
	if your_move == '2':
		eevee_hp = eevee_hp - 10
		print('Snorlax uses tackle and deals 10 HP damage to Eevee!')
	time.sleep(0.2)
	if your_move == '3':
		eevee_hp = eevee_hp - 30
		print('Snorlax uses roundhouse kick and deals 30 HP damage to Eevee!')
	time.sleep(0.2)
	if your_move == '4':
		eevee_hp = eevee_hp - 40
		print('Snorlax uses hyper beam and deals 40 HP of damage to Eevee!')
	time.sleep(0.2)
	if your_move == '5':
		capture_roll = random.randint(1,2)
		if capture_roll > eevee_hp:
			print('You have tried to capture Eevee!')
		else:
			print('You have tried to capture Eevee, but failed.')
	print()

	#eevee attacks 
	enemy_move = random.randint(1,2)
	enemy_move = str(enemy_move)
	if enemy_move == '1':
		snorlax_hp = snorlax_hp - 30 
		eevee_hp = eevee_hp + 10 
		print('Eevee uses healing potion and deals 30 HP of damage while recovering 10 HP!')
	time.sleep(0.2)
	if enemy_move == '2':
		snorlax_hp = snorlax_hp - 20
		print('Eevee uses breathe fire and deals 20 HP of damage!')
	time.sleep(0.2)
	print()

	if snorlax_hp < 0: 
		snorlax_hp = 0
	if eevee_hp < 0:
		eevee_hp = 0


	print('Updated HP')
	time.sleep(0.2)
	print('- Snorlax HP: ' + str(snorlax_hp))
	time.sleep(0.2)
	print('- Eevee HP: ' + str(eevee_hp))
	time.sleep(0.2)
	print()
	time.sleep(0.2)

	if snorlax_hp == 0:
		print('Snorlax was defeated! Eevee is the winner.')
	if eevee_hp == 0:
		print('Eevee was defeated! Snorlax is the winner.')


