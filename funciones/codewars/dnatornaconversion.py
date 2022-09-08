def dna_to_rna(dna):
    return dna.replace('t','u')

conversion = dna_to_rna('gcat')
print(conversion)