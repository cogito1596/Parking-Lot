import uuid
from .payment_type import PaymentType
from .payment_status import paymentStatus
from datetime import datetime


class Payment:
    def __init__(
        self,
        amount,
        bill: int,
        payment_type: PaymentType,
        payment_status: paymentStatus,
        ref_id: str,
        paid_at: datetime,
    ):
        self.amount = amount
        self.payment_status = payment_status
        self.payment_type = payment_type
        self.bill = bill
        self.ref_id = ref_id
        self.paid_at = paid_at
        self.id = uuid.uuid4()
