class GateRepo:
    def __init__(self):
        self.gates = {}

    def find_gate(self, gate_id):
        if gate_id in self.gates:
            return self.gates[gate_id]
        return None
