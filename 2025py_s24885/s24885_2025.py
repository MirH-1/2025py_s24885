import random

def generate_dna_sequence():
    while True:
        try:
            seq_length = int(input("Please enter the sequence length here: "))
            if seq_length <= 0:
                print("Invalid input! It must be a positive number.")
                continue
            break
        except ValueError:
            print("That's not even a number! Try again.")

    seq_id = input("Please enter the sequence ID: ")
    description = input("You better provide that description: ")
    user_name = input("Enter your name: ")

    nucleotides = ['A', 'C', 'G', 'T']
    dna_sequence = ''.join(random.choice(nucleotides) for _ in range(seq_length))

    insert_position = random.randint(0, len(dna_sequence))
    sequence_with_name = dna_sequence[:insert_position] + user_name + dna_sequence[insert_position:]

    file_name = f"{seq_id}.fasta"
    with open(file_name, "w") as file:
        file.write(f">{seq_id} {description}\n")
        for i in range(0, len(sequence_with_name), 60):
            file.write(sequence_with_name[i:i + 60] + "\n")

    count_a = dna_sequence.count("A")
    count_c = dna_sequence.count("C")
    count_g = dna_sequence.count("G")
    count_t = dna_sequence.count("T")

    percent_a = (count_a / seq_length) * 100
    percent_c = (count_c / seq_length) * 100
    percent_g = (count_g / seq_length) * 100
    percent_t = (count_t / seq_length) * 100
    cg_ratio = ((count_c + count_g) / (count_a + count_t)) * 100 if (count_a + count_t) > 0 else 0

    print(f"\nThe sequence was saved to the file {file_name}")
    print("Sequence statistics:")
    print(f"A: {percent_a:.1f}%")
    print(f"C: {percent_c:.1f}%")
    print(f"G: {percent_g:.1f}%")
    print(f"T: {percent_t:.1f}%")
    print(f"CG/AT ratio: {cg_ratio:.2f}%")

# Run the function
generate_dna_sequence()