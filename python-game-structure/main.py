import game.chapter_one.main
import game.chapter_two.main
from game.engine import Engine, SceneMap

print("Starting the engine...")
a_map = SceneMap()
a_game = Engine(a_map)
a_game.play()
