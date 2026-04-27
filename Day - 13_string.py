# Day 13: String Methods practised by anshuraj-alonix
# 12th CBSE | CUET Bioinfo Aspirant

bio_text = " dna to rna conversion "

# 1. Space hata ke, Title case me lana
bio_text = bio_text.strip().title()
print("Clean:", bio_text) # Dna To Rna Conversion

# 2. DNA to RNA
dna = "ATGCATGC"
rna = dna.replace("T", "U")
print("DNA:", dna) # ATGCATGC
print("RNA:", rna) # AUGCAUGC 

# 3. Check karna ki Start codon hai ya nahi
codon = "AUG"
print("Start Codon hai?", codon.startswith("AUG")) # True
