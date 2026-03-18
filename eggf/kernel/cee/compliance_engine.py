class ComplianceEvaluationEngine:
    def evaluate(self, intercepted_data):
        logits = intercepted_data.get("logits")

        # Simple heuristic (MVP)
        score = max(logits) if logits is not None else 1.0

        # Normalize mock compliance vector
        return [float(score) % 1, 0.9, 0.8]
