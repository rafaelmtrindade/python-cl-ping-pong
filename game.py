#!/usr/bin/env python3

from time import sleep
from random import randint
from consoles import ConsoleNavigator
from props import *
from elements import Scoreboard, GameOverOverlay
from player import Player


NAVIGATOR = ConsoleNavigator(True)


class Game:
    def __init__(self, player1: Player, player2: Player, max_sets: int = 2):
        '''
        Passar 2 jogadores e a quantidade de sets necessária para o fim da partida.

        player1 será sempre o jogador da esquerda,

        player2 será sempre o jogador da direita.

        max_sets determina quantos sets são necessários para um jogador vencer a partida. Para escolher manualmente, passar max_sets = 0
        '''
        # futuramente tirar da tabela de chars

        self.player1 = player1
        self.player2 = player2

        self.max_sets = decide_max_sets(
            NAVIGATOR) if not max_sets else max_sets

        try:
            NAVIGATOR.hide_cursor()
            dims = [*NAVIGATOR.init_size]

            for i, d in enumerate((16, 39)):
                if dims[i] < d:
                    dims[i] = d

            NAVIGATOR.resize_window(*dims)
            NAVIGATOR.move_cursor_to_init_pos()
            print_win_condition(self.max_sets)

            NAVIGATOR.move_cursor_by(1)
            self.scoreboard = Scoreboard(NAVIGATOR)
            self.anim_frame_top_row = self.scoreboard.top_row+2
            self.overlay = GameOverOverlay(
                NAVIGATOR,
                self.anim_frame_top_row+1,
                10, 31)

            if randint(0, 1):
                self.active_player = self.player2
                self.other_player = self.player1
            else:
                self.active_player = self.player1
                self.other_player = self.player2

            self.run_game()
        except KeyboardInterrupt:
            NAVIGATOR.reset_window_size()
            NAVIGATOR.move_cursor_to_init_pos()
            NAVIGATOR.move_cursor_by(15, 0)
        finally:
            NAVIGATOR.show_cursor()

    def toggle_active_player(self, ap: Player):
        self.active_player = self.other_player
        self.other_player = ap

    def update_score(self):
        self.scoreboard.print_scores(
            self.player1.score,
            self.player1.sets,
            self.player2.score,
            self.player2.sets
        )

    def attempt_play(self, fail_threshold: int, on_fail: str):
        '''
        fail_threshold chance de falha para a jogada
        on_fail animação que deve ser usada em caso de falha na jogada
        '''
        ap = self.active_player
        op = self.other_player

        crit_chance = ap.base_crit + ap.crit_mod
        fail_chance = fail_threshold + ap.lose_mod
        roll = randint(0, 100)

        # TODO: adicionar chance de acertar a bola mas mandar pra fora da mesa
        # TODO: adicionar critical fail => debuff permanente até o fim do jogo
        if roll < fail_chance:
            self.animate(ap, on_fail)
            sleep(.5)
            return True
        elif roll == fail_chance:
            self.animate(ap, 'hit')
            op.add_crit_mod(op.strength)
        elif fail_chance < roll < 100 - crit_chance + ap.lose_mod:
            self.animate(ap, 'hit')
        else:
            self.animate(ap, 'crit')
            op.add_penalty(ap.strength + ap.lose_mod)
        ap.reset_penalty()
        ap.reset_crit_mod()
        return False

    def serve(self):
        self.animate(self.active_player, 'mark')
        return self.attempt_play(self.active_player.serve_fail_chance, 'fail_serve')

    def rebound(self):
        return self.attempt_play(100-self.active_player.skill, 'miss')

    def run_game(self):
        game_over = False
        self.player1.full_reset()
        self.player2.full_reset()

        while not game_over:
            self.play_round()
            self.update_score()
            self.toggle_active_player(self.active_player)
            game_over = self.player1.sets >= self.max_sets or self.player2.sets >= self.max_sets
        self.end_game()

    def play_round(self):
        self.player1.reset_crit_mod()
        self.player2.reset_crit_mod()
        self.player1.reset_penalty()
        self.player2.reset_penalty()

        is_round_over = self.serve()
        while not is_round_over:
            self.toggle_active_player(self.active_player)
            is_round_over = self.rebound()
        self.other_player.add_score()

    def end_game(self):
        winner = self.player1 if self.player1.sets > self.player2.sets else self.player2
        self.overlay.print_overlay(winner)

    # anims section
    def animate(self, player: Player, action: str):
        '''
        action pode ser: 'crit', 'hit', 'mark', 'miss'

        futuramente também: 'serve', 'fail_serve'
        '''
        anim = left_anims.get_anim(
            action) if player == self.player1 else right_anims.get_anim(action)
        if anim:
            anim.animate(NAVIGATOR, self.anim_frame_top_row)


if __name__ == '__main__':
    # Alterar as propriedades dos jogadores como quiser
    p1 = Player()
    p2 = Player(85)

    ######### ATENÇÃO ##########
    # Ao executar o jogo por um terminal especial (VSCode ou uma IDE, por exemplo),
    # certifique-se que o terminal possui dimensões de, pelo menos, 39x16 (larguraXaltura),
    # porque a correção automática de tamanho não funciona.
    # Caso contrário, o jogo não será exibido corretamente.
    game = Game(p1, p2, 0)
