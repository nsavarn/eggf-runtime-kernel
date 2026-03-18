class ExecutionStateController:
    def __init__(self, thresholds):
        self.state = "SAFE"
        self.thresholds = thresholds

    def transition(self, compliance_vector):
        min_val = min(compliance_vector)
        if min_val < self.thresholds["T3"]:
            self.state = "ESCALATED"
        elif min_val < self.thresholds["T2"]:
            self.state = "RESTRICTED"
        elif min_val < self.thresholds["T1"]:
            self.state = "CONDITIONAL"
        else:
            self.state = "SAFE"
        return self.state
