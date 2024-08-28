import os
import re

def OpenFile(FilePath):
    files = []
    # Check if the given path is a directory
    if os.path.isdir(FilePath):
        for filename in os.listdir(FilePath):
            if filename.endswith(".txt"):
                file_path = os.path.join(FilePath, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    files.append(text)  # Append the text directly
    else:
        print(f"The path {FilePath} is not a valid directory.")
    return files

def Conclusion(FileText):
    print("Conclusion Function started : ")

    result = []

    pattern = r'Conclusion\s*(.*?)(?:\n = \0|\Z)'

    match = re.search(pattern, FileText, re.DOTALL| re.IGNORECASE)

    result.append('Conclusion : ')

    if match:
        result.append (match.group(1).strip())  # Return the matched string
        print("Conclusion Found")
        #print(result)

    elif match:
        pattern = r'Summary\s*(.*?)(?:\n = \0|\Z)'

        match = re.search(pattern, FileText, re.DOTALL| re.IGNORECASE)
        result.append (match.group(1).strip())
        print ("Summary found")

    full_text = ' '.join(result)

    # Check if the full text exceeds 3096 characters
    print(len(full_text))
    #print(full_text)

    if(len(full_text)) > 3096:
        print("More")
        sentences = re.split(r'(?<=[.!?])\s+', full_text)
        limited_text = ' '.join(sentences[:7])
        
        # Print only the limited text
        #print(limited_text)

        return limited_text

    else:
        return full_text

def main():
    FilePath = r"C:\Users\DELL\OneDrive\Desktop\update\Civil"
    file_texts = OpenFile(FilePath)  # Get all file contents

    for FileText in file_texts:  # Iterate over each file's text
        #print(FileText)  # Optional: Print the content of the file
        conclusion_result = Conclusion(FileText)  # Pass each file's text to the Conclusion function
        print(conclusion_result)  # Print the result

if __name__ == "__main__":
    main()
