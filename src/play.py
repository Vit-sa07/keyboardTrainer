import pygame
import pyjokes
import time
from src.Globals import Gl as self

pygame.init()
clock = pygame.time.Clock()


class Training:

    # Функция для получения шутки с помощью библиотеки pyjokes
    @staticmethod
    def get_joke():
        self.joke_text = pyjokes.get_joke(language='en', category='all')
        self.joke_text = self.joke_text[:90]
        print(self.joke_text)
        self.joke = self.joke_font.render(self.joke_text, True, 'yellow')
        self.joke2 = self.joke_font.render(self.joke_text, True, 'black')

    @staticmethod
    def result(cost):
        accuracy = 0  # Точность
        wpm = 0  # Кол-во знаков в минуту
        percent = 100  # Процент
        minute = 60
        count = 0
        average_word = 5  # Кол-во слов
        if not self.game_over:
            self.total_time = time.time() - self.time_start
            for i in range(len(self.joke_text)):
                try:
                    if self.user_text[i] != self.joke_text[i]:
                        cost += 1
                        self.user_text = self.user_text[:-1]
                    if self.user_text[i] == self.joke_text[i]:
                        count += 1
                except:
                    print('Ошибка')
            try:
                accuracy = (count / ((len(self.user_text)) + cost)) * percent
                wpm = len(self.user_text) * minute / (average_word * self.total_time)
            except:
                print('Ошибка')
            self.res = 'Время: ' + str(round(self.total_time)) + \
                       ' Ошибки: ' + str(round(accuracy)) + '%' + \
                       ' Кол.Сим.Мин: ' + str(round(wpm))

        self.results = self.result_font.render(self.res, True, 'green')
        self.results2 = self.result_font.render(self.res, True, 'black')
        f = open('./static.txt')
        self.results3 = self.last_result_font.render('Твой последний результат ' + str(f.readlines()[-1]), True, 'Yellow')


    @staticmethod
    def testing():
        play = True
        active = False
        start_x1, start_x2, start_y1, start_y2 = 350, 550, 400, 464
        max_len_rect, change_len_rect, max_len_text = 440, 5, 90
        time_tick = 80
        help_text = ''
        count = 0
        while play:
            f = open('./static.txt', 'a')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if start_x1 <= x <= start_x2 and start_y1 <= y <= start_y2:
                        Training.get_joke()
                        self.user_text = ''
                        active = True
                        self.game_over = False
                        self.time_start = time.time()
                        self.rect_color = 'green'
                        self.start_color = 'green'
                        self.len_rect = 10
                        count = 0
                elif event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        f.write('\n' + '\n' + 'Основной текст: ' + self.joke_text + '\n')
                        f.write('Твой текст: ' + self.user_text + '\n')
                        f.write('Результат: ' + self.res)
                        active = False
                        self.game_over = True
                        count = 0
                        print(' ' + self.user_text)
                        print(self.res + '\n')
                        self.rect_color = 'red'
                        self.start_color = 'red'
                    if event.key == pygame.K_BACKSPACE:
                        count += 1
                        self.user_text = self.user_text[:-1]
                        if len(help_text) > 0:
                            self.user_text = help_text[len(help_text) - 1] + self.user_text
                            help_text = help_text[:-1]
                        if len(self.user_text) < max_len_text - 10:
                            self.len_rect -= change_len_rect
                    else:
                        if self.len_rect < max_len_rect:
                            self.len_rect += change_len_rect
                        self.user_text += event.unicode
                        for i in range(len(self.joke_text)):
                            try:
                                if self.user_text[i] != self.joke_text[i]:
                                    count += 1
                            except:
                                pass
                        if len(self.user_text) > max_len_text:
                            help_text = help_text + self.user_text[0]
                            self.user_text = self.user_text.replace(self.user_text[0], '', 1)
                    if len(self.user_text) == len(self.joke_text):
                        f.write('\n' + '\n' + 'Основной текст: ' + self.joke_text + '\n')
                        f.write('Твой текст: ' + self.user_text + '\n')
                        f.write('Результат: ' + self.res)
                        Training.get_joke()
                        self.user_text = ''
                        self.len_rect = 10
                        count = 0
                        self.time_start = time.time()

            Training.result(count)
            Training.fonts()
            pygame.display.update()
            clock.tick(time_tick)

    @staticmethod
    def display(header_text, header_text_2, text, finish_key, rect_size,
                header2_xy, header_xy, joke2_xy, joke_xy, results2_xy,
                results_xy, results3_xy, finish_xy, text_xy):
        """
            This function displays widgets in a screen.
        """
        start_x = 350
        start_y = 400
        start_size = (345, 395, 210, 74)  # coord x, y, length, wight
        # background
        self.screen.blit(self.bg, (0, 0))

        # rect for input text
        pygame.draw.rect(self.screen, 'black', rect_size)
        pygame.draw.rect(self.screen, self.rect_color, rect_size, 3)

        # start button
        pygame.draw.rect(self.screen, self.start_color, start_size)
        self.screen.blit(self.start, (start_x, start_y))

        # header text
        self.screen.blit(header_text_2, header2_xy)
        self.screen.blit(header_text, header_xy)
        # output text (random text, joke)
        self.screen.blit(self.joke2, joke2_xy)
        self.screen.blit(self.joke, joke_xy)
        # input text
        self.screen.blit(text, text_xy)
        # result text
        self.screen.blit(self.results2, results2_xy)
        self.screen.blit(self.results, results_xy)
        self.screen.blit(self.results3, results3_xy)
        # finish rext
        self.screen.blit(finish_key, finish_xy)

    @staticmethod
    def fonts():
        """
        This function is responsible for the characteristics of widgets.
        """
        # text fonts
        text_font = pygame.font.SysFont("georgia", self.text_size)
        header_font = pygame.font.SysFont('mannerliness', self.header_size)
        header_text = header_font.render('KEYBOARD TRAINER', True, 'white')
        header_text_2 = header_font.render('KEYBOARD TRAINER', True, 'black')
        text = text_font.render(self.user_text, True, self.color_text)
        finish_font = pygame.font.SysFont('georgia', self.finish_size)
        finish_key = finish_font.render('Press ENTER for finish!', True, 'white')

        # blit coord
        rect = max(self.len_rect, 150)  # here 150 - initial length of rect
        rect_size = (self.width / 2 - rect, 160, 2 * rect, 50)  # size increases as you enter text
        header2_xy = header_text.get_rect(center=(self.width / 2 + 4, 54))  # 54 is coord_y of header text's tone
        header_xy = header_text.get_rect(center=(self.width / 2, 50))  # 50 coord_y of header text
        text_xy = text.get_rect(center=(self.width / 2, 185))  # 185 is coord_y of text
        joke2_xy = self.joke.get_rect(center=(self.width / 2 + 1, 106))  # 106 is coord_y of joke's tone
        joke_xy = self.joke.get_rect(center=(self.width / 2, 105))  # 105 is coord_y of joke
        results2_xy = self.results.get_rect(center=(self.width / 2 + 1, 311))  # 311 is coord_y of result's tone
        results_xy = self.results.get_rect(center=(self.width / 2 + 1, 310))  # 310 is coord_y of result
        results3_xy = self.results3.get_rect(center=(self.width / 2 + 1, 351))  # 311 is coord_y of result's tone
        finish_xy = finish_key.get_rect(center=(self.width / 2, 500))  # 500 is coord_y of finish

        Training.display(header_text, header_text_2, text, finish_key, rect_size,
                     header2_xy, header_xy, joke2_xy, joke_xy, results2_xy,
                     results_xy, results3_xy, finish_xy, text_xy)


