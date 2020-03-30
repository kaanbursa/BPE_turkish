## Byte Pair Encoding for Turkish

Word tokenization is essential for natural language processing tasks. A group of researchers at [University
of Edinburgh](https://arxiv.org/pdf/1508.07909.pdf) influenced by Data Compression algorithm [Byte Pair Encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding)
and created an algorithm that can deal with new words by tokenizing substrings which is essential for
agglunative languages like Turkish. So the essential goals is to create a vocabulary of N size which can be determined by you.
Capture most used words and create tokens for them + capture all suffixes of the language so whenever a new word with suffixes is seen
the model will see what those suffixes were used like before and will be able to create a representation for the new word.


## How it works
1. Create a vocabulary from a dataset. In my case I used the [Turkish news dataset](https://www.kaggle.com/suleymancan/turkishnews70000/data) from kaggle.
2. For each word in the vocabulary separate words into characters
3. Count frequency of bi-grams of characters
4. Create a new word for the vocabulary for the most frequent character pair
5. Repeat until reached desired vocabulary size


## Encoding - Decoding

To encode the given sentence first we need to convert our token dictionary from longest word to shortest word. We add split each word in the sentence and add </w> to the end of word. We iterate through each token and if the substring of the word includes the token we put that token as tokenization process. Decoding is given our tokens we merge the word do not have </w> and add ‘ ‘ if the word has </w> at the end.

## References
- Rico Sennrich (2016). [Neural Machine Translation of Rare Words with Subword Units](https://www.aclweb.org/anthology/P16-1162.pdf)

- Lei Mao - [Byte Pair Encoding](https://leimao.github.io/blog/Byte-Pair-Encoding/)   
