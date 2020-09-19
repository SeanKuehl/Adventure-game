from cx_Freeze import setup, Executable
import pygame
pygame.init()
pygame.event.get()
setup(name='Adventure', version='0.0.1',description='go on an adventure',executables = [Executable("Main.py")])
pygame.event.get()