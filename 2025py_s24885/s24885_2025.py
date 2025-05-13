"""
DNA Sequence Generator in FASTA Format
Author: Mir Haidar

This program generates a random DNA sequence of a user-specified length,
inserts the user's name at a random location within the sequence,
calculates the percentage of each nucleotide, and the CG/AT ratio,
then saves the result in a FASTA format file.
"""

import random

# Prompt the user to enter the desired DNA sequence length
while True:
    try:
        sequence_length = int(input("Please enter the sequence length here: "))
        if sequence_length <= 0:
            print("Invalid input! Must be a positive number.")
            continue
        break
    except ValueError:
        print("That's not even a number! Try again.")

# Prompt for sequence metadata
sequence_id = input("Enter the sequence ID: ")
sequence_description = input("Provide a description of the sequence: ")
user_name = input("Enter your name (will be inserted into the sequence): ")

# Define the possible nucleotides
nucleotides = ['A', 'C', 'G', 'T']

# ORIGINAL:
# sequence = ''.join(random.choice(nucleotides) for _ in range(sequence_length))
# MODIFIED (wrapped in a function for reuse and testing purposes):
def generate_dna_sequence(length):
    """Generate a random DNA sequence of the specified length."""
    return ''.join(random.choice(nucleotides) for _ in range(length))

original_sequence = generate_dna_sequence(sequence_length)

# Insert the user's name at a random location (not counted in statistics)
insertion_index = random.randint(0, len(original_sequence))
# MODIFIED (renamed for clarity and avoiding shadowing):
sequence_with_name_inserted = original_sequence[:insertion_index] + user_name + original_sequence[insertion_index:]

# Save the sequence to a .fasta file using the specified format
fasta_filename = f"{sequence_id}.fasta"
with open(fasta_filename, "w") as fasta_file:
    fasta_file.write(f">{sequence_id} {sequence_description}\n")
    for i in range(0, len(sequence_with_name_inserted), 60):
        fasta_file.write(sequence_with_name_inserted[i:i+60] + "\n")

# Count nucleotides in the original sequence (excluding name)
count_A = original_sequence.count('A')
count_C = original_sequence.count('C')
count_G = original_sequence.count('G')
count_T = original_sequence.count('T')

# Calculate nucleotide percentages
percent_A = (count_A / sequence_length) * 100
percent_C = (count_C / sequence_length) * 100
percent_G = (count_G / sequence_length) * 100
percent_T = (count_T / sequence_length) * 100

# MODIFIED (clarified formula + renamed for precision):
cg_at_ratio_percent = ((count_C + count_G) / (count_A + count_T)) * 100 if (count_A + count_T) > 0 else 0

# Display the results
print(f"\nThe sequence was saved to the file {fasta_filename}")
print("Sequence statistics:")
print(f"A: {percent_A:.1f}%")
print(f"C: {percent_C:.1f}%")
print(f"G: {percent_G:.1f}%")
print(f"T: {percent_T:.1f}%")
print(f"CG/AT ratio: {cg_at_ratio_percent:.2f}%")