import random
while True:
    try:
        length = int(input("Please enter the sequence length here: "))
        if length <= 0:
            print("Invalid input! Gotta be a positive number, pal.")
            continue
        break
    except ValueError:
        print("That's not even a number! Try again.")

seq_id = input("Please Enter the sequence ID: ")
description = input("You better provide that description boy: ")
name = input("Enter your name pretty boy!!! ")

nucleotides = ['A', 'C', 'G', 'T']
sequence = ''.join(random.choice(nucleotides) for _ in range(length))  # correct version

insert_position = random.randint(0, len(sequence))
sequence_with_name = sequence[:insert_position] + name + sequence[insert_position:]

filename = f"{seq_id}.fasta"
with open(filename, "w") as f:
    f.write(f">{seq_id} {description}\n")
    for i in range(0, len(sequence_with_name), 60):
        f.write(sequence_with_name[i:i+60] + "\n")

count_A = sequence.count("A")
count_C = sequence.count("C")
count_G = sequence.count("G")
count_T = sequence.count("T")

percent_A = (count_A / length) * 100
percent_C = (count_C / length) * 100
percent_G = (count_G / length) * 100
percent_T = (count_T / length) * 100
cg_ratio = ((count_C + count_G) / (count_A + count_T)) * 100 if (count_A + count_T) > 0 else 0

print(f"\nThe sequence was saved to the file {filename}")
print("Sequence statistics:")
print(f"A: {percent_A:.1f}%")
print(f"C: {percent_C:.1f}%")
print(f"G: {percent_G:.1f}%")
print(f"T: {percent_T:.1f}%")
print(f"CG/AT ratio: {cg_ratio:.2f}%")