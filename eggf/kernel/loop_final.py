from eggf.audit.trace import AuditTrace
from eggf.audit.hash_chain import HashChain

class RuntimeControlLoop:
    def __init__(self, iim, cee, rese, ecc, crim):
        self.iim = iim
        self.cee = cee
        self.rese = rese
        self.ecc = ecc
        self.crim = crim
        self.trace = AuditTrace()
        self.hash_chain = HashChain()

    def step(self, input_ids, logits):
        intercepted = self.iim.capture(input_ids, logits)
        compliance = self.cee.evaluate(intercepted)
        state = self.rese.transition(compliance)
        modified_logits = self.ecc.apply(logits, state)
        self.crim.adjust(state)

        record = {
            "input_ids": str(input_ids),
            "state": state,
            "compliance": compliance
        }

        self.trace.log(record)
        record_hash = self.hash_chain.hash_record(str(record))

        return modified_logits, state, compliance, record_hash
