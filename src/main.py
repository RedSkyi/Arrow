from src import EZ
from src import config
from src.sprite import sprite

window = EZ.creation_fenetre(config.WIDTH, config.HEIGHT, config.NAME)
keys = []

players = [sprite.Sprite(300, 200, 100, 100), sprite.Sprite(600, 200, 100, 100)]

EZ.reglage_fps()

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
        players[0].direction = [-1, 0]

        if players[0].speed[0] <= config.MAX_SPEED:
            players[0].apply([2, 0])
    elif "d" in keys:
        players[0].direction = [1, 0]

        if players[0].speed[0] <= config.MAX_SPEED:
            players[0].apply([2, 0])

    for sprites in sprite.sprites:
        sprites.update()
        sprites.draw_hitbox()  # Debug only

    EZ.mise_a_jour()
    EZ.frame_suivante()
