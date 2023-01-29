# import required modules / packages
from Bio import SeqIO

# read sequence
#seq = [str(record.seq) for record in SeqIO.parse("sequence.fasta", "fasta")][0]
sequence = input("Enter the protein sequence filename: ")
seq = [str(record.seq) for record in SeqIO.parse(sequence, "fasta")][0]
# length of protein
N = len(seq)
print(f"Length of Sequence: {N}\n{seq}")

# Count Serine (S)
s = seq.count("S")
# calculate percent of S
s_pcnt = round((s/N)*100, 2)

# Count Threonine (T)
t = seq.count("T")
# calculate percent of T
t_pcnt = round((t/N)*100, 2)

print(f"Percentage of Serine (S): {s_pcnt}%")
print(f"Percentage of Threonine (T): {t_pcnt}%")
