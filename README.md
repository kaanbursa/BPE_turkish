## Byte Pair Encoding for Turkish

Word tokenization is essential for natural language processing tasks. A group of researchers at [University 
of Edinburgh](https://arxiv.org/pdf/1508.07909.pdf) influenced by Data Compression algorithm [Byte Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
and created an algorithm that can deal with new words by tokenizing substrings which is essential for
agglunative languages like Turkish. So the essential goals is to create a vocabulary of N size which can be determined by you.
Capture most used words and create tokens for them + capture all suffixes of the language so whenever a new word with suffixes is seen
the model will see what those suffixes were used like before and will be able to create a representation for the new word.


## How it works
1. Create a vocabulary from a dataset. In my case I used the [Turkish news dataset](https://www.kaggle.com/suleymancan/turkishnews70000/data) from kaggle.
2. 