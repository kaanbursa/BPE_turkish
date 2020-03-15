import re, collections

class BytePairEncoder():

    def __init__(self):
        self.vocab = collections.defaultdict(int)
        self.tokens = collections.defaultdict(int)

    def get_vocab(self, filename):
        vocab = collections.defaultdict(int)
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    vocab[' '.join(list(word)) + ' </w>'] += 1
        return vocab


    def get_stats(self,vocab):
        pairs = collections.defaultdict(int)
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pairs[symbols[i],symbols[i+1]] += freq
        return pairs

    def merge_vocab(self, pair, v_in):
        v_out = {}
        bigram = re.escape(' '.join(pair))
        p = re.compile(r'(?<!\S)' + bigram + r'(?<!\S)')
        for word in v_in:
            w_out = p.sub(''.join(pair), word)
            v_out[w_out] = v_in[word]

        return v_out

    def get_tokens(self, vocab):
        tokens = collections.defaultdict(int)
        for word, freq in vocab.items():
            word_tokens = word.split()
            for token in word_tokens:
                tokens[token] += freq
        return tokens

    def get_tokens_from_vocab(self):
        tokens_frequencies = collections.defaultdict(int)
        vocab_tokenization = {}
        for word, freq in self.vocab.items():
            word_tokens = word.split()
            for token in word_tokens:
                tokens_frequencies[token] += freq
            vocab_tokenization[''.join(word_tokens)] = word_tokens
            return tokens_frequencies, vocab_tokenization


    def measure_token(self,token):
        if token[-4:] == '</w>':
            return len(token[:-4]) + 1
        else:
            return len(token)

    def tokenize_word(self, string, sorted_tokens, unknown_token='</u>'):
        if string == '':
            return []
        if sorted_tokens == []:
            return [unknown_token]

        string_tokens = []
        for i in range(len(sorted_tokens)):
            token = sorted_tokens[i]
            token_reg = re.escape(token.replace('.', '[.]'))
            matched_positions = [(m.start(0), m.end(0)) for m in re.finditer(token_reg, string)]
            if len(matched_positions) == 0:
                continue
            substring_end_positions = [matched_position[0] for matched_position in matched_positions]
            substring_start_position = 0
            for substring_end_position in substring_end_positions:
                substring = string[substring_start_position:substring_end_position]
                string_tokens += self.tokenize_word(string=substring,sorted_tokens=sorted_tokens[i+1:], unknown_token=unknown_token)
                string_tokens += [token]
                substring_start_position = substring_end_position + len(token)
            remaining_substring = string[substring_start_position:]
            string_tokens += self.tokenize_word(string=remaining_substring, sorted_tokens=sorted_tokens[i + 1:],
                                           unknown_token=unknown_token)
            break
        return string_tokens

