from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HFAdapter:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_step(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt")
        outputs = self.model(**inputs)
        logits = outputs.logits[:, -1, :].squeeze()
        return inputs.input_ids, logits

    def decode(self, token_ids):
        return self.tokenizer.decode(token_ids)
