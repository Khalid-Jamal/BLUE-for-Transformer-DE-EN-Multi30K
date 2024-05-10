import nltk
from nltk.translate.bleu_score import sentence_bleu

# Function to read lines from a file and split into words
def read_and_preprocess(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        # Read lines, strip whitespace, and split into words
        lines = [line.strip().split() for line in file.readlines()]
    return lines

# Load sentences from files
ref_sentences = read_and_preprocess('results\enco.ref')  # ref standard translations
machine_sentences = read_and_preprocess('results\enco.con')  # Machine translations

# Check if both files have the same number of sentences
assert len(ref_sentences) == len(machine_sentences), "Files should have the same number of lines."

# Calculate BLEU scores for each sentence pair
individual_bleu_scores = []
for reference, concluded in zip(ref_sentences, machine_sentences):
    # Calculate BLEU score for this sentence pair
    score = sentence_bleu([reference], concluded)
    individual_bleu_scores.append(score)

# Calculate the average BLEU score
average_bleu_score = sum(individual_bleu_scores) / len(individual_bleu_scores)
print(f"Average BLEU score for the 100 sentences: {average_bleu_score:.4f}")