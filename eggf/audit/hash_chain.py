import hashlib

class HashChain:
    def __init__(self):
        self.prev_hash = "0"

    def hash_record(self, record: str):
        combined = self.prev_hash + record
        new_hash = hashlib.sha256(combined.encode()).hexdigest()
        self.prev_hash = new_hash
        return new_hash
