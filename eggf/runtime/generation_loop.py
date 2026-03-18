import torch

def generate_with_control(adapter, loop, prompt, max_tokens=20):
    input_ids, logits = adapter.generate_step(prompt)
    generated = input_ids[0].tolist()

    for _ in range(max_tokens):
        logits = loop.step(generated, logits.tolist())

        probs = torch.softmax(torch.tensor(logits), dim=-1)
        next_token = torch.argmax(probs).item()

        generated.append(next_token)
        input_ids = torch.tensor([generated])
        outputs = adapter.model(input_ids)
        logits = outputs.logits[:, -1, :].squeeze()

    return adapter.decode(generated)
