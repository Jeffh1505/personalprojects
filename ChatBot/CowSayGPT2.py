class ChatBot:
    def __init__(self):
        from transformers import GPT2Tokenizer, GPT2LMHeadModel
        self.model_type = 'gpt2-xl'
        self.device = 'cuda'
        self.model = GPT2LMHeadModel.from_pretrained(self.model_type)
        self.model.config.pad_token_id = self.model.config.eos_token_id  # suppress a warning

    def generate(self, prompt='', num_samples=10, steps=20, do_sample=True):
        from transformers import GPT2Tokenizer
        import torch

        tokenizer = GPT2Tokenizer.from_pretrained(self.model_type)
        encoded_input = tokenizer(prompt, return_tensors='pt').to(self.device)
        x = encoded_input['input_ids'].expand(num_samples, -1) if prompt else None

        # forward the model `steps` times to get samples, in a batch
        y = self.model.generate(x, max_new_tokens=steps, do_sample=do_sample, top_k=40)

        for i in range(num_samples):
            out = tokenizer.decode(y[i].cpu().squeeze())
            print('-' * 80)
            print(out)


user_input = input("What would you like to say to the chatbot?: ")
chatbot = ChatBot()
chatbot.generate(user_input)
