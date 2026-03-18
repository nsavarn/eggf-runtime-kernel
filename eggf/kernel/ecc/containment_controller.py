class ContainmentController:
    def apply(self, logits, state):
        if state == "RESTRICTED":
            return self._mask_logits(logits)
        elif state == "ESCALATED":
            raise Exception("Generation Halted: Escalated State")
        return logits

    def _mask_logits(self, logits):
        # Simple mask example
        return [l if i % 2 == 0 else float('-inf') for i, l in enumerate(logits)]
