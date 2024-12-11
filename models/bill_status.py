from enum import Enum


class BillStatus(Enum):
    Paid = 1
    Unpaid = 2
    PartiallyPaid = 3
    Overdue = 4
