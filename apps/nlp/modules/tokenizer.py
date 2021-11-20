import numpy as np


sentence = 'Taclḥiyt nɣ Taclḥit nɣ Tasusit tga yat tutlayt tamaziɣt illan ɣ lmɣrib, middn li sis isawaln gan Iclḥiyn.'
token_sequence = str.split(sentence)
vocab = sorted(set(token_sequence))
', '.join(vocab)
num_tokens = len(token_sequence)
vocab_size = len(vocab)
onehot_vectors = np.zeros((
    num_tokens,
    vocab_size), int)
for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1

' '.join(vocab)

