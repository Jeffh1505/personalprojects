from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import cowsay
class ChatBot:
    def __init__(self):
        self.model_type = 'gpt2-xl'
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = GPT2LMHeadModel.from_pretrained(self.model_type)
        self.model.config.pad_token_id = self.model.config.eos_token_id  # suppress a warning

    def generate(self, prompt='', num_samples=10, steps=20, do_sample=True):
        tokenizer = GPT2Tokenizer.from_pretrained(self.model_type)
        encoded_input = tokenizer(prompt, return_tensors='pt').to(self.device)
        x = encoded_input['input_ids'].expand(num_samples, -1) if prompt else None

        # Forward the model `steps` times to get samples, in a batch
        y = self.model.generate(x, max_length=steps, do_sample=do_sample, top_k=1)

        for i in range(num_samples):
            out = tokenizer.decode(y[i].cpu().squeeze())
        print(cowsay.get_output_string("cow", out))


def main():
    chatbot = ChatBot()
    while True:
        user_input = input("What would you like to say to the chatbot?: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        chatbot.generate(user_input)


if __name__ == "__main__":
    main()
