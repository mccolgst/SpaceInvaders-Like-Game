import pyglet
from classes import player
from classes.enemy import *

game_window = pyglet.window.Window(*WINDOW_SIZE)

main_batch = pyglet.graphics.Batch()

# Initialize the player sprite
player_ship = player.Player(x=400, y=300, batch=main_batch)

eg = EnemyGroup(NUM_ENEMIES, main_batch)
#en1 = Enemy(x=500, y=700, batch=main_batch)
game_objects = [player_ship, eg]


# Tell the main window that the player object responds to events
game_window.push_handlers(player_ship.key_handler)


@game_window.event
def on_draw():
	game_window.clear()

	main_batch.draw()


def update(dt):
	# collision detection
	all_enemies = eg.enemies
	for en in eg.enemies:
		obj_1 = player_ship
		obj_2 = en

		if not obj_1.dead and not obj_2.dead:
			if obj_1.collides_with(obj_2):
				obj_1.handle_collision_with(obj_2)
				obj_2.handle_collision_with(obj_1)

	# remove objects from game_objects and delete them
	if player_ship.dead:
		player_ship.delete()
		game_objects.remove(player_ship)
	for obj in eg.enemies:
		if obj.dead:
			eg.remove(obj)

	# update all game objects
	for obj in game_objects:
		obj.update(dt)

if __name__ == "__main__":
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()