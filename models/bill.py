import uuid
from .gate import Gate
from datetime import datetime
from typing import List
from .bill_status import BillStatus


class Bill:
    def __init__(
        self,
        id: int,
        exit_time: datetime,
        token,
        exited_at,
        payments: List,
        total_amount: int,
        bill_status: BillStatus,
    ):
        self.id = uuid.uuid4()
        self.exit_time = exit_time
        self.token = token
        self.exited_at = exited_at
        self.payments = payments
        self.total_amount = total_amount
        self.bill_status = bill_status
