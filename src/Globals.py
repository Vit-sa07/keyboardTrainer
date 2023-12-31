import pygame
import os
bg_img = 'bg.png'  # background image
start_img = 'start.png'  # start button image

bg = pygame.image.load(os.path.join('images', bg_img))   # loading bg image into "bg" parameter
start = pygame.image.load(os.path.join('images', start_img))  # loading start button img into "start" param.


class Gl:
    """
    This class for global parameters
    Globals saves the value of global parameters,
     it will be imported into "play.py"
    """
    results = None
    results2 = None
    results3 = None
    pygame.init()
    width, height = 900, 600  # width and height of screen.
    user_text = ''  # text entry option.
    user_joke = ''  # joke (random sentence) output option.
    time_start = 0  # will fix the start of time after the start.
    total_time = 0  # total time during after typing.
    res = 'Time:0   Accuracy:0 %    WpM:0'  # result of typing.
    game_over = True  # will fix end of game.
    len_rect = 10  # the length of the rectangle where the text is inputted.
    rect_color = 'red'  # color of this rectangle.
    start_color = 'red'  # color of start button.
    color_text = 'white'
    count = 0

    text_size = 20  # the size of text, which inputting.
    header_size = 60  # the size of header text (Keyboard Trainer)
    finish_size = 15  # the size of finish text
    result_size = 30  # the size of finish text
    last_result_size = 20  # the size of finish text
    start_w, start_h = 200, 64  # width and height start button.

    pygame.display.set_caption('Keyboard Trainer')  # show in screen caption
    screen = pygame.display.set_mode((width, height))  # display screen (900x600)
    bg = pygame.transform.scale(bg, (width, height))  # scale background image to fit screen
    start = pygame.transform.scale(start, (start_w, start_h))  # scale start image (200, 64)

    joke_font = pygame.font.SysFont('georgia', text_size, False, False)  # font and size of output text(joke)
    joke_text = 'Are you ready?'  # output text before start
    joke = joke_font.render(joke_text, True, 'yellow')  # output text character
    joke2 = joke_font.render(joke_text, True, 'black')  # output text tint character
    result_font = pygame.font.SysFont('georgia', result_size)  # font and size result text
    last_result_font = pygame.font.SysFont('georgia', last_result_size)  # font and size result text