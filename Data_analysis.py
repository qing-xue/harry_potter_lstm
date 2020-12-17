import numpy

filename1 = "./data/Harry_Potter1-7.txt"
filename2 = "./data/171160.txt"
raw_text_1 = open(filename1, 'r', encoding='utf-8').read()
raw_text_1 = raw_text_1.lower()
chars_1 = sorted(list(set(raw_text_1)))
n_chars_1 = len(raw_text_1)
n_vocab_1 = len(chars_1)
print("Harry_Potter's Total Characters:",n_chars_1)
print("Harry_Potter's Total Vocab: ", n_vocab_1)

raw_text_2 = open(filename2, 'r', encoding='utf-8').read()
chars_2 = sorted(list(set(raw_text_2)))
n_chars_2 = len(raw_text_2)
n_vocab_2 = len(chars_2)
print("ShuiHuzhuan's Total Characters:",n_chars_2)
print("ShuiHuzhuan's Total Vocab: ", n_vocab_2)

