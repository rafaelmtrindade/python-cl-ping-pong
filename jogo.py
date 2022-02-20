from player import Player
from random import randint


class Jogo:
    def __init__(self):
        # futuramente tirar da tabela de chars
        self.player1 = Player('left', '', 85)
        self.player2 = Player('right', '', 80)

        if randint(0, 1):
            self.active_player = self.player2
            self.other_player = self.player1
        else:
            self.active_player = self.player1
            self.other_player = self.player2

        self.start_game()

    def toggle_active_player(self, ap: Player):
        self.active_player = self.other_player
        self.other_player = ap

    def update_score(self):
        pass

    def attempt_play(self, fail_threshold: int, on_fail):
        ap = self.active_player
        op = self.other_player

        crit_chance = ap.base_crit + ap.crit_mod

        roll = randint(0, 100)

        # modify to include chance of hitting it but landing it out of the table
        if roll < fail_threshold:
            on_fail()
            return True
        elif roll == fail_threshold:
            ap.hit()
            op.buff_crit(op.strength)
        elif fail_threshold < roll < crit_chance:
            ap.hit()
        else:
            ap.crit_hit()
            op.add_penalty(ap.strength)
        return False

    def serve(self):
        self.active_player.mark()
        return self.attempt_play(self.active_player.serve_fail_chance, self.active_player.fail_serve)

    def rebound(self):
        return self.attempt_play(self.active_player.skill, self.active_player.miss)

    def start_game(self):
        game_over = False
        self.player1.full_reset()
        self.player2.full_reset()
        print('\n'*11)

        while not game_over:
            self.play_round()
            self.update_score()
            self.toggle_active_player(self.active_player)
            game_over = self.player1.sets >= 3 or self.player2.sets >= 3

    def play_round(self):
        is_round_over = self.serve()
        while not is_round_over:
            self.toggle_active_player(self.active_player)
            is_round_over = self.rebound()
        self.other_player.add_point()


if __name__ == '__main__':
    jogo = Jogo()

    # 1. Criar/Selecionar jogadores 1 e 2

    # 2. Coletar apostas

    # 3. Coin flip para determinar quem começa
    # resetar sets, pontos
    # 4. Resetar modificadores de crit e falha
    # 5. Marcar jogador que vai começar
    # 6. Rolar saque
    # a. Sucesso Critico:
    # i. jogador ativo -> animação de critico
    # b. Sucesso:
    # i. jogador ativo -> animação acerto
    # c. Quase falha:
    # i. jogador ativo -> animação acerto
    # ii. mudar jogador ativo
    # iii. adicionar chance de critico para jogador ativo
    # d. Falha:
    # i.   jogador ativo -> animação falha saque
    # ii.  mudar jogador ativo
    # iii. marcar ponto para jogador ativo
    # iv.  Atualizar placar -> 4.
    # 7.  Mudar jogador ativo
    # 8. Rolar rebate no jogador ativo
    # a. Sucesso Critico -> 5.a.i.
    # b. Sucesso -> 5.b.i.
    # c. Quase falha:
    # i.   jogador ativo -> animação quase falha rebate
    # ii.  mudar jogador ativo
    # iii. adicionar chance de critico para jogador ativo
    # d. Falha:
    # i.   jogador ativo -> animação falha rebate
    # ii.  mudar jogador ativo
    # iii. marcar ponto para jogador ativo
    # iv.  atualizar placar -> 4.
