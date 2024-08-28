import os
import pandas as pd
import spacy
import re

nlp = spacy.load("en_core_web_sm")
pd.set_option("display.max_rows", 200)

def OpenFiles(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                files.append((text, filename))
    return files

def Costs(filetext):
    doc = nlp(filetext)

    entites = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ent.label_ in {"MONEY"}]

    printed_sentences = set()

    points = 0

    if entites:
        for entity in entites:
            start_char = entity[1]

            for sent in doc.sents:
                if sent.start_char <= start_char < sent.end_char:
                    if sent.text not in printed_sentences:
                        points +=1
                        print(points,sent.text)
                        printed_sentences.add(sent.text)
                    break
    else:
        print("Not Found")

    print("\n")

def Fetchlink(filetext):
    url_regex = r"https?://[a-zA-Z0-9.-]+(?:/[^\s]*)?"

    links = re.findall(url_regex, filetext)

    valid_links = [link for link in links if link.endswith('.html') and not link.endswith('Cite')]

    # Print the valid URLs
    print(valid_links)

def main():
    directory = r'C:\Users\DELL\OneDrive\Desktop\LegalCaseAnalyser\BailiArticles'
    files = OpenFiles(directory)
    for file_text, filename in files:
        print(f"Processing file : {filename}")
        Costs(file_text)
        Fetchlink(file_text)

if __name__ =="__main__":
    main()