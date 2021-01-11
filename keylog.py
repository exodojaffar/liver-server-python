import keyboard


def callback(event):
	name =  event.name

	with open('keylog_cache', 'w')  as cache:
		if name == 's' and 'ctrl' in event.modifiers:
			cache.write('True')
		else:
			cache.write('False')
	


	pass

keyboard.on_press(callback=callback)
keyboard.wait()