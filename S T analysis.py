# import required modules and packages
from Bio import SeqIO

# read protein sequence
#seq = [str(record.seq) for record in SeqIO.parse("sequence.fasta", "fasta")][0]
sequence = input("Enter the protein sequence filename: ")
seq = [str(record.seq) for record in SeqIO.parse(sequence, "fasta")][0]
# length of protein sequence
N = len(seq)
print(f"Length of Sequence: {N}\n{seq}")

# Count Serine (S)
s = seq.count("S")
# calculate percentage of S
s_pcnt = round((s/N)*100, 2)

# Count Threonine (T)
t = seq.count("T")
# calculate percentage of T
t_pcnt = round((t/N)*100, 2)

print(f"Percentage of Serine (S): {s_pcnt}%")
print(f"Percentage of Threonine (T): {t_pcnt}%")
