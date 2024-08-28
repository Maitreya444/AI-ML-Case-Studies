import pandas as pd
import spacy
import os

directory = r"C:\Users\DELL\OneDrive\Desktop\Programming\Projects\Freelancing\Penelope\summary"

nlp = spacy.load("en_core_web_md")

pd.set_option("display.max_rows", 200)

def Ner_Case_Claimant(text):
    result = []
    content = text

    doc = nlp(content)

    # Filter for "Claimant" or "Appellant"
    entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ("Appellant" in ent.text or "solicitors" in ent.text or "Claimant" in ent.text or "Claimants" in ent.text or "Claimant's" in ent.text or "Client" in ent.text) and ent.label_ in {"ORG", "PERSON"}]
    
    printed_sentences = set()

    if entities:
        for entity in entities:
            start_char = entity[1]

            for sent in doc.sents:
                if sent.start_char <= start_char < sent.end_char:
                    if sent.text not in printed_sentences:
                        result.append(f"{sent.text}\n")
                        printed_sentences.add(sent.text)
                    break
    else:
        result.append("Claimant not found\n")

    return ''.join(result)

def Ner_Case_Defendant(text):
    result = []
    content = text

    doc = nlp(content)

    # Filter for "Defendant" or "Respondent"
    entities = [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ("Defendant" in ent.text or "Respondent" in ent.text or "defedant's" in ent.text or "defedant" in ent.text) and ent.label_ in {"ORG", "PERSON"}]
    
    printed_sentences = set()

    if entities:
        for entity in entities:
            start_char = entity[1]

            for sent in doc.sents:
                if sent.start_char <= start_char < sent.end_char:
                    if sent.text not in printed_sentences:
                        result.append(f"{sent.text}\n")
                        printed_sentences.add(sent.text)
                    break
    else:
        result.append("Defendant not found\n")

    return ''.join(result)

def ClaimantAnalysis(text):
    doc = nlp(text)

    # Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    # Calculate similarities between sentences
    similarities = []

    for i in range(len(sentences)):
        for j in range(i+1, len(sentences)):
            sim = nlp(sentences[i]).similarity(nlp(sentences[j]))
            similarities.append((sim, sentences[i], sentences[j]))

    # Sort similarities by score in descending order
    similarities.sort(reverse=True, key=lambda x: x[0])

    # Collect the top 2 pairs without repeating sentences
    top_sentences = []
    used_sentences = set()

    for sim, sent1, sent2 in similarities:
        if len(top_sentences) >= 1:
            break
        if sent1 not in used_sentences and sent2 not in used_sentences:
            top_sentences.append((sim, sent1, sent2))
            used_sentences.add(sent1)
            used_sentences.add(sent2)

    result1 = []
    points = 1
    for sim, sent1, sent2 in top_sentences:
        result1.append(f"{points}. {sent1}")
        points += 1
        result1.append(f"{points}. {sent2}")
        points += 1
    
    return result1

def DefendantAnalysis(text):
    doc = nlp(text)

    # Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    # Calculate similarities between sentences
    similarities = []

    for i in range(len(sentences)):
        for j in range(i+1, len(sentences)):
            sim = nlp(sentences[i]).similarity(nlp(sentences[j]))
            similarities.append((sim, sentences[i], sentences[j]))

    # Sort similarities by score in descending order
    similarities.sort(reverse=True, key=lambda x: x[0])

    # Collect the top 2 pairs without repeating sentences
    top_sentences = []
    used_sentences = set()

    for sim, sent1, sent2 in similarities:
        if len(top_sentences) >= 1:
            break
        if sent1 not in used_sentences and sent2 not in used_sentences:
            top_sentences.append((sim, sent1, sent2))
            used_sentences.add(sent1)
            used_sentences.add(sent2)

    result1 = []
    points = 1
    for sim, sent1, sent2 in top_sentences:
        result1.append(f"{points}. {sent1}")
        points += 1
        result1.append(f"{points}. {sent2}")
        points += 1
    
    return result1

def main():
    output_content1 = []
    output_content2 = []

    filename = r"C:\Users\DELL\OneDrive\Desktop\Civil\COST_MEGA_BITES_168__AN_EXHAUSTING_READ_V_BUDGETS_THAT_ARE_DESCRIBED_AS_ABSURDLY_HIGH_WHOLLY_EXCESSIVE_AND_WHICH_STRAINS_ALL_CREDULITY.txt"
    if filename.endswith(".txt"):
        file_path = filename
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            claimant_summary = Ner_Case_Claimant(text)
            output_content1.append(claimant_summary)
            print(f"NER in Case {filename}")
            defendant_summary = Ner_Case_Defendant(text)
            output_content2.append(defendant_summary)

    # Handle or display the output_content
    if output_content1:
        for entity in output_content1:
            analysis_results = ClaimantAnalysis(entity)
            print("Claimants:")
            for analysis_result in analysis_results:
                print(analysis_result)

    if output_content2:
        for entity in output_content2:
            analysis_results = DefendantAnalysis(entity)
            print("Defedants:")
            for analysis_result in analysis_results:
                print(analysis_result)

if __name__ == "__main__":
    main()
