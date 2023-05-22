import pygame
from main_menu import Menu
from main_menu import Menu


class Blocks:
    """show menu"""
    def __init__(self, screen):
        self._blocks = []
        self._blocks_positions = []
        self._colors = ["", "", "", "", "", ""]
        Menu.draw(screen, "green", (0, 0, 40, 40), 20)

    def append_option(self, option, callback):
        self._option_surfaces.append(self._ARIAL_50.render(option, True, (255, 255, 255)))
        self._callback.append(callback)