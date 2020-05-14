from src import EZ, sprite
from src import config
from src.sprites.movable_sprite import MovableSprite
from src.sprites.player import Player
from src.sprites.ground import Ground

window = EZ.creation_fenetre(config.WIDTH, config.HEIGHT, config.NAME)
keys = []

players = [Player(300, 200), Player(600, 200)]

EZ.reglage_fps()

#  =========================
#  DEBUG ONLY
Ground(0, 750, 50, config.WIDTH)
#  =========================

while EZ.test_fenetre():
    EZ.trace_rectangle_droit(0, 0, config.WIDTH, config.HEIGHT, *config.WHITE)
    event = EZ.recupere_evenement()

    if event == "TOUCHE_ENFONCEE":
        keys.append(EZ.touche())
    elif event == "TOUCHE_RELACHEE":
        keys.remove(EZ.touche())
    elif event == "EXIT":
        EZ.destruction_fenetre()

    if "q" in keys:
        if players[0].check_speed():
            players[0].apply([-2, 0])
    elif "d" in keys:
        if players[0].check_speed():
            players[0].apply([2, 0])

    for sprites in sprite.sprites:
        if isinstance(sprites, MovableSprite):
            sprites.update()

        sprites.draw_hitbox()  # Debug only

    EZ.mise_a_jour()
    EZ.frame_suivante()
