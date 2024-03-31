import os
import re

def transform_file(input_file_path, output_file_path):
    # Create a dictionary from the ArpaBET CMU dict file
    arpa_dict = {}
    with open("CMUdict.txt", "r", encoding='ISO-8859-1') as arpa_file:
        for line in arpa_file:
            if line.startswith(';'):
                continue
            match = re.match(r'^\s*([^ ]+)\s+(.+)$', line)
            if match:
                word = match.group(1).upper()  # Convert to uppercase for case-insensitivity
                arpa_representation = match.group(2)
                # arpa_representation = re.sub(r'\d', '', arpa_representation)  // this will remove all the numbers such as AA[1] from the arpa_rep
                arpa_dict[word] = arpa_representation
                
    #Open input and output files
    with open(input_file_path, "r", encoding='ISO-8859-1') as input_file, open(output_file_path, "w", encoding='ISO-8859-1') as output_file:
        # Process each line in the input file
        for line in input_file:
            words = line.strip().split()
            arpa_pronoun_word = []

            for word in words:
                # Lookup word in the ArpaBET dictionary or use the original word
                arpa_word = arpa_dict.get(word.upper(), "")
                arpa_pronoun_word.append(arpa_word)

            # Write the ArpaBET representation of the line to the output file
            output_file.write(" ".join(arpa_pronoun_word) + "\n")
    
    
# Main function to process all CHA files in the 'Data/' directory
def main():
    clean_dir = 'clean/'
    transform_dir = 'transformed/'
    
    # input_file_path = "src/ruth.txt"
    # output_file_path = "src/trans_ruth.txt"
    # transform_file(input_file_path, output_file_path)
    
    # Recursively traverse directories
    for root, _, files in os.walk(clean_dir):
        for file in files:
            if file.endswith('.txt'):
                input_file_path = os.path.join(root, file)
                # Create output directory structure in 'transform/' directory
                output_file_path = os.path.join(transform_dir, os.path.relpath(input_file_path, clean_dir))
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                transform_file(input_file_path, output_file_path)

if __name__ == '__main__':
    main()
