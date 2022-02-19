from time import sleep


class Animation:
    frame_rate = 12

    def __init__(self, frames: "list[str]"):
        self.frames = frames

        self.beggining_pos = '\033[F'*(self.frames[0].count('\n')+1)

    def animate(self):
        for frame in self.frames:
            sleep(1/self.frame_rate)
            print(f'{self.beggining_pos}{frame}')


left_player_hit = Animation([
    """
|---===============================---|
|  |                                  |
|  |    。                            |
|  |   Q_ 0  .-----\-----.  ,_0 _     |
|  |     / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |         °                        |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |             ⚬                    |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                 。               |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \  °  \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                      °           |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
])

left_player_crit = Animation([
    """
|---===============================---|
|  |                                  |
|  |    。                            |
|  |   Q_ 0  .-----\-----.  ,_0 _     |
|  |     / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |              。                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \    °\    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                          °       |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
])

left_player_miss = Animation([
    """
|---===============================---|
|  |                                  |
|  |  。                              |
|  |   Q_ 0  .-----\-----.  ,_0 _     |
|  |     / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
| ⚬|    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |⚬ o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,

    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/   °          |          |          |
|                                     |
|---===============================---|
    """,
])

left_player_mark = Animation([
    """
|---===============================---|
|  |     :                            |
|  |     v                            |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |     :                            |
|  |     v                            |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """
])

#######################################


#######################################

right_player_hit = Animation([
    """
|---===============================---|
|  |                                  |
|  |                             。   |
|  |    _ 0  .-----\-----.  ,_0 _,O   |
|  |  o' / \ |\     \     \    \      |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                       °          |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                  ⚬               |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |               。                 |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\  °  \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |         °                        |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """
])

right_player_crit = Animation([
    """
|---===============================---|
|  |                                  |
|  |                             。   |
|  |    _ 0  .-----\-----.  ,_0 _,O   |
|  |  o' / \ |\     \     \    \      |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                。                |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\°    \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |      °                           |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """
])

right_player_miss = Animation([
    """
|---===============================---|
|  |                                  |
|  |                                。|
|  |    _ 0  .-----\-----.  ,_0 _,O   |
|  |  o' / \ |\     \     \    \      |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _,O   |
|  |  o' / \ |\     \     \    \      |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """
])

right_player_mark = Animation([
    """
|---===============================---|
|  |                           :      |
|  |                           v      |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                           :      |
|  |                           v      |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """,
    """
|---===============================---|
|  |                                  |
|  |                                  |
|  |    _ 0  .-----\-----.  ,_0 _     |
|  |  o' / \ |\     \     \    \ `o   |
|  |____|\___|_`-----\-----`__ /|_____|
| /     / |     |          |  | \\     |
|/              |          |          |
|                                     |
|---===============================---|
    """
])
