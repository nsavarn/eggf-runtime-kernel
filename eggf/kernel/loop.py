class RuntimeControlLoop:
    def __init__(self, iim, cee, rese, ecc, crim):
        self.iim = iim
        self.cee = cee
        self.rese = rese
        self.ecc = ecc
        self.crim = crim

    def step(self, input_ids, logits):
        intercepted = self.iim.capture(input_ids, logits)
        compliance = self.cee.evaluate(intercepted)
        state = self.rese.transition(compliance)
        logits = self.ecc.apply(logits, state)
        self.crim.adjust(state)
        return logits
