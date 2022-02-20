import anims


class Player:
    player_count = 0

    def __init__(self, skill: int = 70, base_crit: int = 0, name: str = '', side: str = ''):
        if side:
            self.set_side()

        if isinstance(skill, int) and 0 < skill < 100:
            self.skill = skill
        else:
            self.skill = 60

        self.strength = self.skill // 3
        self.serve_fail_chance = (100 - self.skill) // 6

        if isinstance(base_crit, int) and 0 <= base_crit <= 50:
            self.base_crit = base_crit
        else:
            self.base_crit = 0

        self.player_count += 1

        self.full_reset()
        self.name = name if name else f'Jogador {self.player_count}'

    def set_side(self, side: str = 'left'):
        self.side = 'right' if side != 'left' else side
        if side == 'left':
            self.hit_anim = anims.left_player_hit
            self.crit_anim = anims.left_player_crit
            self.miss_anim = anims.left_player_miss
            self.mark_anim = anims.left_player_mark
            # self.fail_serve_anim = anims.left_player_fail_serve
        else:
            self.hit_anim = anims.right_player_hit
            self.crit_anim = anims.right_player_crit
            self.miss_anim = anims.right_player_miss
            self.mark_anim = anims.right_player_mark
            # self.fail_serve_anim = anims.right_player_fail_serve

    def add_crit_mod(self, amount: int):
        self.crit_mod += amount

    def reset_crit_mod(self):
        self.crit_mod = 0

    def add_penalty(self, strength_mod):
        self.lose_mod += strength_mod

    def reset_penalty(self):
        self.lose_mod = 0

    def add_score(self):
        if self.score == 14:
            self.score = 0
            self.sets += 1
        else:
            self.score += 1

    def reset_score(self):
        self.score = 0
        self.sets = 0

    def full_reset(self):
        self.reset_crit_mod()
        self.reset_penalty()
        self.reset_score()

    def mod_reset(self):
        self.reset_crit_mod()
        self.reset_penalty()

    # TODO: Sistema de XP
    # Level up -> ganha pontos pra colocar em:
    #   b_crit, strength ou skill
    # TODO: Criar e permitir adicionar bonus de critico base para:
    #   rebater
    #   saques

    #### ANIMATIONS ####
    # TODO: criar animação
    def fail_serve(self):
        pass
        # self.serve_fail_anim.animate()

    def hit(self):
        self.hit_anim.animate()

    def crit_hit(self):
        self.crit_anim.animate()

    def miss(self):
        self.miss_anim.animate()

    def mark(self):
        self.mark_anim.animate()


# TEST ANIMS
if __name__ == '__main__':
    player1 = Player('', -1, 'left')
    player2 = Player('', -1, 'right')
    print('\n'*12)

    for i in range(3):
        player1.hit()
        # player1.animate_crit()
        player2.hit()
        # player2.animate_crit()
    # player1.animate_miss()
    player1.crit_hit()
    player2.miss()
