import random  # Importing the random module for generating random numbers and sequences

'''
length = int(input("Enter the sequence length: "))
sequence_id = input("Enter the sequence ID: ")
description = input("Provide a description of the sequence: ")
name = input("Enter your name: ")

nucleotides = ['A', 'C', 'G', 'T']
dna_sequence = ''.join(random.choices(nucleotides, k=length))

insert_position = random.randint(0, length)
sequence_with_name = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]

a_count = dna_sequence.count('A')
c_count = dna_sequence.count('C')
g_count = dna_sequence.count('G')
t_count = dna_sequence.count('T')

total = length
a_percent = (a_count / total) * 100
c_percent = (c_count / total) * 100
g_percent = (g_count / total) * 100
t_percent = (t_count / total) * 100
cg_ratio = ((c_count + g_count) / total) * 100

fasta_filename = sequence_id + '.fasta'
with open(fasta_filename, 'w') as fasta_file:
    fasta_file.write(f">{sequence_id} {description}\n")
    fasta_file.write(sequence_with_name + '\n')

print(f"The sequence was saved to the file {fasta_filename}")
print("Sequence statistics:")
print(f"A: {a_percent:.1f}%")
print(f"C: {c_percent:.1f}%")
print(f"G: {g_percent:.1f}%")
print(f"T: {t_percent:.1f}%")
print(f"%CG: {cg_ratio:.1f}")
'''

# PURPOSE: Generate a random DNA sequence in FASTA format with inserted username, compute statistics and save to a file
# CONTEXT: Assignment for bioinformatics programming course
# AUTHOR: [Fetia Fanfan]
# DATE: [8-5-2025]

# === USER INPUT SECTION ===

# Improvement I: Adding input validation to ensure the user inputs a positive integer for the sequence length
# ORIGINAL:
# length = int(input("Enter the sequence length: "))
# MODIFIED (adds input validation to avoid crashes with invalid input):
while True:
    try:
        seq_length = int(input("Enter the sequence length: "))  # Ask for sequence length and convert to int
        if seq_length <= 0:  # Reject non-positive numbers
            raise ValueError  # Manually raise error for non-positive input
        break  # Exit loop if input is valid
    except ValueError:
        print("Please enter a valid positive integer for the sequence length.")  # Error message for invalid input

# Ask for the sequence ID (used as the filename and in FASTA header)
sequence_id = input("Enter the sequence ID: ")

# Ask for the sequence description (included in the FASTA header)
description = input("Provide a description of the sequence: ")

# Ask for the user's name (to be inserted randomly in the sequence)
user_name = input("Enter your name: ")

# List of valid DNA nucleotide characters
nucleotides = ['A', 'C', 'G', 'T']


# === FUNCTION DEFINITIONS ===

# Improvement II: Moved DNA sequence generation to a function for modularity and reusability
# ORIGINAL:
# dna_sequence = ''.join(random.choices(nucleotides, k=length))
# MODIFIED (moved to function for modularity and reusability):
def generate_dna_sequence(seq_len):
    return ''.join(random.choices(nucleotides, k=seq_len))  # Join randomly chosen nucleotides into a single string


# Improvement III: Insert name function for better clarity and testability
# ORIGINAL:
# sequence_with_name = dna_sequence[:insert_position] + name + dna_sequence[insert_position:]
# MODIFIED (moved to function to clarify intent and improve testability):
def insert_name(sequence, name_to_insert, position):
    return sequence[:position] + name_to_insert + sequence[position:]  # Insert name in the middle of the sequence


# === SEQUENCE CREATION ===

dna_sequence = generate_dna_sequence(seq_length)  # Generate the DNA sequence of specified length

insert_position = random.randint(0, seq_length)  # Choose a random position in the sequence to insert the name

sequence_with_name = insert_name(dna_sequence, user_name, insert_position)  # Insert name into the sequence

# === STATISTICS CALCULATION ===

# Count each nucleotide in the original DNA sequence (not including name)
nucleotide_counts = {nuc: dna_sequence.count(nuc) for nuc in nucleotides}  # Dictionary of counts for A, C, G, T
a_count = nucleotide_counts['A']  # Count of 'A'
c_count = nucleotide_counts['C']  # Count of 'C'
g_count = nucleotide_counts['G']  # Count of 'G'
t_count = nucleotide_counts['T']  # Count of 'T'

# Total number of nucleotides (equal to the input length)
total = seq_length

# Calculate percentage of each nucleotide
a_percent = (a_count / total) * 100
c_percent = (c_count / total) * 100
g_percent = (g_count / total) * 100
t_percent = (t_count / total) * 100

# Calculate CG content ratio as percentage
cg_ratio = ((c_count + g_count) / total) * 100

# === WRITE TO FASTA FILE ===

fasta_filename = sequence_id + '.fasta'  # Create filename based on sequence ID

with open(fasta_filename, 'w') as fasta_file:  # Open file for writing
    fasta_file.write(f">{sequence_id} {description}\n")  # Write FASTA header
    fasta_file.write(sequence_with_name + '\n')  # Write sequence (with name inserted) on the next line

# === OUTPUT STATISTICS TO USER ===

print(f"The sequence was saved to the file {fasta_filename}")  # Inform user file was saved
print("Sequence statistics:")  # Header for statistics
print(f"A: {a_percent:.1f}%")  # Print % of A
print(f"C: {c_percent:.1f}%")  # Print % of C
print(f"G: {g_percent:.1f}%")  # Print % of G
print(f"T: {t_percent:.1f}%")  # Print % of T
print(f"%CG: {cg_ratio:.1f}")  # Print CG ratio
