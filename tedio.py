from random import randint
from time import sleep

player1 = {
    "name": 'Jogador 1',
    "active": True,
    "base_lose": 30,
    "lose_mod": 0
}
player2 = {
    "name": 'Jogador 2',
    "active": False,
    "base_lose": 30,
    "lose_mod": 0
}


def change_active():
    if player1.get('active'):
        player2['active'] = True
        player1['active'] = False
    else:
        player1['active'] = True
        player2['active'] = False


def eval_round(active_player, other_player):
    lose_threshold = active_player.get(
        'base_lose') - active_player.get('lose_mod')
    roll = randint(1, 100)
    active_player['lose_mod'] = 0
    change_active()

    sleep(.5)

    if roll <= lose_threshold:
        print(f'{active_player.get("name")} não conseguiu rebater!')
        return active_player
    elif lose_threshold < roll < 100:
        print(f'{active_player.get("name")} rebateu!')
        return other_player
    else:
        print(f'{active_player.get("name")} rebateu a bola com muita força!')
        other_player['lose_mod'] = 10
        return other_player


game_not_lost = True
ap = player1
op = player2


print(f'{ap.get("name")} sacou!')
while game_not_lost:
    ap = player1 if player1.get('active') else player2
    op = player1 if ap == player2 else player2

    if eval_round(op, ap) == op:
        game_not_lost = False

print(f'Fim de jogo! {ap.get("name")} ganhou!')
