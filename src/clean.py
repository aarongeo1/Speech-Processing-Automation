import os
import re

def clean_cha_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    # Use regular expressions to remove headers, extraneous information, and handle * lines
    cleaned_content = re.sub(r'@.*?(\n|$)', '', content, flags=re.DOTALL)
    cleaned_content = re.sub(r'%.*?(\n|$)', '', cleaned_content, flags=re.DOTALL)
    cleaned_content = re.sub(r'\*[^:]*:', '', cleaned_content, flags=re.DOTALL)  # Removes lines starting with '*' up to ':'

    # Remove content between "NAK" markers including "NAK"
    cleaned_content = re.sub(r'NAK[^NAK]*NAK', '', cleaned_content)

    # Remove expressions like "&=laughs" and "=! gasps" while keeping the rest of the line
    #cleaned_content = re.sub(r'[&=!]*[a-zA-Z]+', '', cleaned_content)

    # Remove lines with only '0' in conversation by matching and replacing with an empty string
    cleaned_content = re.sub(r'^\s*0\s*\.\s*$', '', cleaned_content, flags=re.MULTILINE)

    # Remove all characters except for letters, digits, spaces and '
    cleaned_content = re.sub(r'[^\w\s\'-]', '', cleaned_content)

    # remove numbers
    cleaned_content = re.sub(r'[0-9_]', '', cleaned_content)
    # Remove empty lines
    cleaned_content = '\n'.join(line for line in cleaned_content.split('\n') if line.strip())

    # Write the cleaned content to a new .txt file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(cleaned_content)

# Main function to process all CHA files in the 'Data/' directory
def main():
    data_dir = '..Data/'
    clean_dir = '..clean/'

    # Recursively traverse directories
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.cha'):
                input_file_path = os.path.join(root, file)
                # Create output directory structure in 'clean/' directory
                output_file_path = os.path.join(clean_dir, os.path.relpath(input_file_path, data_dir)).replace('.cha', '.txt')
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                clean_cha_file(input_file_path, output_file_path)

if __name__ == '__main__':
    main()
