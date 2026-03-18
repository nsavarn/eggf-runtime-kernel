class AdvancedComplianceEngine:
    def __init__(self, keywords=None):
        self.keywords = keywords or ["insider trading", "fraud", "confidential"]

    def evaluate(self, intercepted_data):
        input_ids = intercepted_data.get("input_ids")
        logits = intercepted_data.get("logits")

        risk_score = 1.0

        # Simple keyword heuristic (placeholder for ML model)
        for token in input_ids:
            if any(k in str(token).lower() for k in self.keywords):
                risk_score -= 0.5

        return [risk_score, 0.9, 0.8]
