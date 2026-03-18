class InferenceInterceptionModule:
    def capture(self, input_ids, logits):
        return {
            "input_ids": input_ids,
            "logits": logits
        }

    def modify_logits(self, logits, mask_indices=None):
        if mask_indices:
            for idx in mask_indices:
                logits[idx] = float('-inf')
        return logits
