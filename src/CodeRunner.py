import os
import re
from clean import clean_cha_file
from transform import transform_file


def main():
    data_dir = 'Data/'
    clean_dir = 'clean/'
    transform_dir = 'transformed/'

    # Step 1: Perform Cleaning
    for root, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.cha'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(clean_dir, os.path.relpath(input_file_path, data_dir)).replace('.cha', '.txt')
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                clean_cha_file(input_file_path, output_file_path)
    print("Cleaning complete")
    print("transform in progress")
    # Step 2: Perform Transformation
    for root, _, files in os.walk(clean_dir):
        for file in files:
            if file.endswith('.txt'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(transform_dir, os.path.relpath(input_file_path, clean_dir))
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                transform_file(input_file_path, output_file_path)
    print("transform complete")

if __name__ == '__main__':
    main()
