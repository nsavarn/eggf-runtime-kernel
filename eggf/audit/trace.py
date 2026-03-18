import time

class AuditTrace:
    def __init__(self):
        self.records = []

    def log(self, data):
        record = {"timestamp": time.time(), **data}
        self.records.append(record)

    def get_trace(self):
        return self.records
