from pico2d import *
import game_framework


def init():
    pass


def finish():
    pass


def update():
    pass


def render():
    clear_canvas()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()


def pause():
    pass


def resume():
    pass
