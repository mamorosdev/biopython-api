from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
import sys

dna: str = ""
if len(sys.argv) != 2:
    print("Instruccions d'ús: " + sys.argv[0] + " <cadena d'ADN>")
    sys.exit()
else:
    dna = sys.argv[1]
    # Convertim la cadena a objecte Seq.
    dna_seq = Seq(dna)

print(f"Seqüència ADN original: {dna}")
print(f"Seqüència ADN complementaria : {dna_seq.complement()}")
arn = dna_seq.transcribe()
print(f"Seqüència ARN: {arn}")

print(f"Percentatge GC: {gc_fraction(dna)}")
