class SlotRepo:
    def __init__(self):
        self.slots = {}

    def update_slot_repo(self, slot, status):
        self.slots[slot.id] = slot
        slot.status = status
        return slot
