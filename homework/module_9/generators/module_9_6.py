def all_variants(text):
    for substr_len in range(1, len(text) + 1):
        start_pos = 0
        end_pos = start_pos + substr_len
        while end_pos < len(text) + 1:
            yield text[start_pos: end_pos]
            start_pos += 1
            end_pos += 1

a = all_variants("abcdef")
for i in a:
    print(i)