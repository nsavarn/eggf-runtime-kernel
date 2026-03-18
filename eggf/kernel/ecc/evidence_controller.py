class EvidenceController:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def validate(self, output_text):
        for evidence in self.knowledge_base:
            if evidence in output_text:
                return True
        return False

    def enforce(self, output_text):
        if not self.validate(output_text):
            raise Exception("Output blocked: No supporting evidence")
        return output_text
