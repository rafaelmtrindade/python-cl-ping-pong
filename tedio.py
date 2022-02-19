from random import randint
from player import Player


def change_active():
    player1.toggle_active()
    player2.toggle_active()


def eval_round(active_player: Player, other_player: Player):
    lose_threshold = 100 - active_player.skill + active_player.lose_mod
    roll = randint(1, 100)
    active_player.reset_penalty()
    change_active()

    if roll <= lose_threshold:
        active_player.miss()
        return active_player
    elif lose_threshold < roll < 100 - active_player.crit_mod:
        active_player.hit()
        return other_player
    else:
        active_player.crit_hit()
        other_player.apply_penalty(active_player.strength)
        return other_player


player1 = Player('left', 'Jorge', 85)
player2 = Player('right', 'Mateus', 80)


ap = player1
op = player2
ap.toggle_active()

round_not_lost = True
print(f'{ap.name} sacou!')

print('\n'*11)

ap.hit()
while round_not_lost:
    ap = player1 if player1.active else player2
    op = player1 if ap == player2 else player2

    if eval_round(op, ap) == op:
        round_not_lost = False
else:
    print(f'{ap.name} ganhou!')
