from time import sleep
from random import randint
from colorama import init
from player import Player


class Game:
    manual_choice = True

    def __init__(self, player1: Player, player2: Player):
        '''
        Passar os 2 jogadores que deseja jogar.

        player1 será sempre o jogador da esquerda,

        player2 será sempre o jogador da direita.
        '''
        # futuramente tirar da tabela de chars
        player1.set_side('left')
        player2.set_side('right')

        self.player1 = player1
        self.player2 = player2

        self.win = self._decide_max_score() if self.manual_choice else 2

        if randint(0, 1):
            self.active_player = self.player2
            self.other_player = self.player1
        else:
            self.active_player = self.player1
            self.other_player = self.player2

        self.run_game()

    def _decide_max_score(self):
        print('\nA cada 15 pontos, se forma um set.')
        print('Escolha abaixo um formato para este jogo:')
        try:
            i = int(input('Melhor de: '))
        except ValueError:
            i = 0
        if not isinstance(i, int) or i % 2 == 0 or i <= 0:
            i = 3
        print(f'Jogando melhor de {i}!')
        return i // 2 + 1

    def toggle_active_player(self, ap: Player):
        self.active_player = self.other_player
        self.other_player = ap

    def update_score(self, cursor_pos: int = 0):
        print('\033[F'*cursor_pos, end='')
        print('.==='+'='*31 + '===.')
        print(f'| {self.player1.score:02} | {self.player1.sets} |' +
              'Ping-Pong'.center(19) + f'| {self.player2.score:02} / {self.player2.sets} |')
        if cursor_pos:
            print('\n'*10, end='')

    def attempt_play(self, fail_threshold: int, on_fail):
        ap = self.active_player
        op = self.other_player

        crit_chance = ap.base_crit + ap.crit_mod
        fail_chance = fail_threshold + ap.lose_mod
        roll = randint(0, 100)

        # TODO: adicionar chance de acertar a bola mas mandar pra fora da mesa
        # TODO: adicionar critical fail => debuff permanente até o fim do jogo
        if roll < fail_chance:
            on_fail()
            sleep(.5)
            return True
        elif roll == fail_chance:
            ap.hit()
            op.add_crit_mod(op.strength)
        elif fail_chance < roll < 100 - crit_chance + ap.lose_mod:
            ap.hit()
        else:
            ap.crit_hit()
            op.add_penalty(ap.strength + ap.lose_mod)
        ap.reset_penalty()
        ap.reset_crit_mod()
        return False

    def serve(self):
        self.active_player.mark()
        return self.attempt_play(self.active_player.serve_fail_chance, self.active_player.fail_serve)

    def rebound(self):
        return self.attempt_play(100-self.active_player.skill, self.active_player.miss)

    def run_game(self):
        game_over = False
        self.player1.full_reset()
        self.player2.full_reset()

        print()
        self.update_score()
        print('\n'*9)
        while not game_over:
            self.play_round()
            self.update_score(12)
            self.toggle_active_player(self.active_player)
            game_over = self.player1.sets >= self.win or self.player2.sets >= self.win
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
        print('\033[F'*9, end='')
        if self.player1.sets >= self.win:
            print('|  |   VITÓRIA')
            print('|  |      V ')
        else:
            print('|  |' + 'VITÓRIA'.rjust(30))
            print('|  |' + 'V'.rjust(27))
        print()
        print('|'.ljust(15, '-') + '=========' + '|'.rjust(15, '-'))
        print(f'|' +
              'Fim de Jogo!'.center(37) + f'|')
        print('|'.ljust(15, '-') + '=========' + '|'.rjust(15, '-'))
        print('\n'*3)


init()

if __name__ == '__main__':
    # Alterar as propriedades dos jogadores como quiser
    p1 = Player()
    p2 = Player(85)
    game = Game(p1, p2)
