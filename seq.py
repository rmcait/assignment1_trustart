def shift_right(seq):
    a = list(seq)
    last_element = a.pop()
    a.insert(0, last_element)
    string_seq = ''.join(a)
    return string_seq

seq = input('seqを入力してください:')
shifted_seq = shift_right(seq)
print(shifted_seq)





