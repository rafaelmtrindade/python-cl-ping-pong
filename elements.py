from consoles import ConsoleNavigator
from time import sleep


class Animation:
    def __init__(self, frames: "list[str]", frame_rate: int = 12):
        self.frame_rate = frame_rate
        self.frames = frames

    def animate(self, nav: ConsoleNavigator, frame_top_row: int):
        for frame in self.frames:
            nav.move_cursor_to(frame_top_row, 0)
            a = nav.NAVIGATOR.get_cursor_pos()
            sleep(1/self.frame_rate)
            print(frame)


class AnimationCollection:
    def __init__(self,
                 crit: Animation,
                 hit: Animation,
                 miss: Animation,
                 mark: Animation,
                 serve: Animation):
        self.crit = crit
        self.hit = hit
        self.miss = miss
        self.mark = mark
        self.serve = serve

    def get_anim(self, anim: str) -> Animation:
        # crit hit mark miss serve
        if anim == 'crit':
            return self.crit
        if anim == 'hit':
            return self.hit
        if anim == 'mark':
            return self.mark
        if anim == 'miss':
            return self.miss
        # if anim == 'serve':
        #     return self.serve
        return self.hit  # REM: implementar animações faltando e remover


class Scoreboard:
    MIN_WIDTH = 29

    def __init__(self, nav: ConsoleNavigator, width: int = 39):
        if width < self.MIN_WIDTH:
            raise ValueError(
                f'largura insuficiente. Deve ser pelo menos {self.MIN_WIDTH}.')
        self.width = width
        self.navigator = nav
        nav.init_pos
        self.top_row = self.navigator.get_cursor_pos().get('row')

        self.top_border = '.' + '='*(self.width-2) + '.'
        print(self.top_border)
        self.print_scores()

    def print_scores(self, p1_sc: int = 0, p1_st: int = 0, p2_sc: int = 0, p2_st: int = 0):
        left_score_string = f'| {p1_sc:02} \\ {p1_st} |'
        right_score_string = f'| {p2_st} / {p2_sc:02} |'

        title_length = self.width - \
            len(left_score_string) - len(right_score_string)
        title_string = 'Ping-Pong'.center(title_length)

        self.navigator.move_cursor_to(self.top_row+1, 0)
        print(left_score_string + title_string + right_score_string)


class GameOverOverlay:
    MIN_WIDTH = 16

    def __init__(self, nav: ConsoleNavigator, top_row: int, p1_col: int, p2_col: int, width=39):
        if width < self.MIN_WIDTH:
            raise ValueError(
                f'largura insuficiente. Deve ser pelo menos {self.MIN_WIDTH}.')
        self.width = width
        self.navigator = nav
        self.top_row = top_row
        self.p1_col = p1_col
        self.p2_col = p2_col

    def print_overlay(self, winner: int):
        win_indicator = [
            'VITÓRIA',
            'V'
        ]
        gameover_msg = 'Fim de Jogo!'.center(self.width-2)
        gameover_msg_border = '|' + '='*(self.width - 2) + '|'

        col = self.p1_col if winner else self.p2_col

        # printar indicador de vencedor sobre o jogador
        self.navigator.move_cursor_to(self.top_row, col-3)
        print(win_indicator[0], end='')
        self.navigator.move_cursor_to(self.top_row+1, col)
        print(win_indicator[1], end='')

        # printar mensagem de game over
        self.navigator.move_cursor_to(self.top_row+4, 0)
        print(gameover_msg_border)
        self.navigator.move_cursor_by(0, 1)
        print(gameover_msg)
        print(gameover_msg_border)

        self.navigator.move_cursor_by(2)
        print()
