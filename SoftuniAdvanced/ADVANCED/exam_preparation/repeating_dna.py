def get_repeating_DNA(test):
    dna = test
    all_subsequences = {}
    for el in range(len(dna) - 9):
        sub_seq = dna[el:el+10]
        all_subsequences.setdefault(sub_seq, 0)
        all_subsequences[sub_seq] += 1
    final = []

    for key, value in all_subsequences.items():
        if value > 1:
            final.append(key)
    return final


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)