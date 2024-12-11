from enum import Enum


class paymentStatus(Enum):
    success = 1
    failure = 2
    pending = 3
    refunded = 4
