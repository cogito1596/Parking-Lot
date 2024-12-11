from enum import Enum


class GateStatus(Enum):
    open = 1
    closed = 2
    under_maintainance = 3
    error = 4
