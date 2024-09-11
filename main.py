import pygame, sys, pygame_widgets
from pygame.locals import QUIT

#Import classes and functions
from ArrayBars import ArrayBars
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown

from display_text import display_text

#Global variables
WIN_HEIGHT = 400
WIN_WIDTH = 500
FPS = 40
BG_COLOR = '#FFFFFF'
PRIMARY_TEXT_COLOR = '#D10000'
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)

#Pygame initializers
pygame.init()
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Algorithm Visualiser')

clock = pygame.time.Clock()


#Function to handle window updates
def update_window(events, ArrayBars):
    win.fill(BG_COLOR)
    apply_settings()
    arrayBars.draw(win)

    #Text displays
    display_text(win, 90, 100, 'Array size:', PRIMARY_TEXT_COLOR, 18)
    display_text(win, 250, 50, 'SORTING VISUALIZER', '#000000', 40)

    display_text(win, 75, 160, 'Passes: ' + str(ArrayBars.num_passes),
                 '#000000', 15)
    display_text(win, 75, 180, 'Comparisons: ' + str(ArrayBars.num_comps),
                 '#000000', 15)
    display_text(win, 75, 200, 'Swaps: ' + str(ArrayBars.num_swaps),
                 '#000000', 15)

    pygame_widgets.update(events)
    pygame.display.update()
    size_slider_display.setText(size_slider.getValue())


#Function to handle windwo updates done by ArrayBars class
def update_window_array_bars():
    global arrayBars
    update_window(pygame.event.get(), arrayBars)


#Function to update settings
def apply_settings():
    arrayBars.set_size(size_slider.getValue())
    arrayBars.algorithm = dropdown.getSelected()


#Initializing classes
#Slider and number display for speed and array size
size_slider = Slider(win, 50, 120, 150, 10, min=90, max=450, step=75)
size_slider_display = TextBox(win,
                              180,
                              90,
                              30,
                              20,
                              fontSize=15,
                              borderThickness=1,
                              radius=2,
                              colour=BG_COLOR)
size_slider_display.disable()

#Button display for shuffle and sort
shuffle_button = Button(win,
                        363,
                        100,
                        50,
                        30,
                        text='Shuffle',
                        radius=2,
                        onClick=lambda: arrayBars.shuffle())
shuffle_button = Button(win,
                        420,
                        100,
                        50,
                        30,
                        text='Sort',
                        radius=2,
                        onClick=lambda: arrayBars.sort())

#Dropdown display
dropdown = Dropdown(
    win,
    240,
    100,
    115,
    30,
    name='Select Algorithm',
    choices=['Bubble Sort', 'Insertion Sort', 'Selection Sort'],
    inactiveColour=PRIMARY_TEXT_COLOR,
    textColour=BG_COLOR,
    borderRadius=4)

arrayBars = ArrayBars(size_slider.getValue(), PRIMARY_TEXT_COLOR,
                      update_window_array_bars)

#Game loop
run = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()

    update_window(events, arrayBars)
    clock.tick(30)
