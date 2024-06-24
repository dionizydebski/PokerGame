from enum import Enum


class PlayerState(Enum):
    FOLD = 1

class PlayerRole(Enum):
    DEALER = 1
    SMALL_BLIND = 2
    BIG_BLIND = 3

class GameState(Enum):
    FIRST = 5
    FLOP = 2
    TURN = 1
    RIVER = 0


