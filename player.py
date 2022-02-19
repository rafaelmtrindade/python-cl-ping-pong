import anims


class Player:
    player_count = 0

    def __init__(self, side: str, name: str, skill: int = 70, crit_mod: int = 0):
        self.active = False
        self.lose_mod = 0
        self.player_count += 1

        self.name = name if name else f'Jogador {self.player_count}'

        if isinstance(skill, int) and 0 < skill < 100:
            self.skill = skill
        else:
            self.skill = 60

        self.strength = self.skill // 3

        if isinstance(crit_mod, int) and 0 <= crit_mod < 40:
            self.crit_mod = crit_mod
        else:
            self.crit_mod = 0

        if side == 'left':
            self.hit_anim = anims.left_player_hit
            self.crit_anim = anims.left_player_crit
            self.miss_anim = anims.left_player_miss
            self.mark_anim = anims.left_player_mark
        else:
            self.hit_anim = anims.right_player_hit
            self.crit_anim = anims.right_player_crit
            self.miss_anim = anims.right_player_miss
            self.mark_anim = anims.right_player_mark

    def toggle_active(self):
        self.active = not self.active

    def apply_penalty(self, strength_mod):
        self.lose_mod += strength_mod

    def reset_penalty(self):
        self.lose_mod = 0

    # implement xp gain
    def hit(self):
        self.hit_anim.animate()

    def crit_hit(self):
        self.crit_anim.animate()

    def miss(self):
        self.miss_anim.animate()

    def mark(self):
        self.mark_anim.animate()


# TEST ANIMS
# player1.print_stats()
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
    # understanding cursor navigation
    # print('line 1')
    # print('line 2')
    # print('line 3')
    # print('line 4')
    # print('line 5', end='')

    # sleep(2)
    # print("\033[F\033[Fnew line 3")

    # testing anim length
    # print(f'{player1_hit[0]}', end=back_to_start)
    # sleep(2)
    # print('got here', end='\n\n\n\n\n\n\n')
