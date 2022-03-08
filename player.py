class Player:
    player_count = 0

    def __init__(self, skill: int = 70, base_crit: int = 0, name: str = ''):
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
