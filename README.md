## Execution
 To execute the program, run the python script titled CodeRunner.py which is located in the src directory. 
 CodeRunner.py will run clean.py first then transform.py which are also located in the same directory.
 Two standard libraries namely 'os' and 're' were imported to run these scripts.
 The cleaned data can be found under /root/clean and the transformed data is within /root/transformed.

 Data Cleaning Module: Engineered a module to preprocess raw CHA (Chatman) files, removing extraneous metadata, annotations, and non-alphabetic characters to produce cleaned text files ready for further analysis. Implemented regex-based transformations to ensure data integrity and uniformity.
Phonetic Transformation Tool: Designed and developed a script to map English words to their ARPABET phonetic representations, facilitating the study of phonetics in linguistic research. Integrated error handling and data validation mechanisms to maintain high accuracy levels.
Automation and Scalability: Automated the processing of an extensive dataset by recursively traversing directory structures, thereby streamlining the workflow for transforming and cleaning hundreds of files with minimal manual intervention.
Performance Optimization: Employed efficient coding practices and optimized file handling operations to minimize processing times and resource usage, enabling the processing of large volumes of data with enhanced performance.


 
