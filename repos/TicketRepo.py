class TicketRepo:
    def __init__(self):
        self.count = -1
        self.__tickets = {}

    def add_ticket(self, ticket):
        new_id = self.count + 1
        ticket.ticket_id = new_id
        self.__tickets[ticket.ticket_id] = ticket
        self.count += 1
        return ticket
