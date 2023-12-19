import tiktoken

class TokenCount:
    
    def __init__(self, model = 'gpt-3.5-turbo'):
        self.enc = tiktoken.encoding_for_model(model)

    def count_tokens(self, transcript):
        return len(self.enc.encode(transcript))

