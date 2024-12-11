from enum import Enum


class PaymentType(Enum):
    cash = 1
    credit_card = 2
    debit_card = 3
    upi = 4
