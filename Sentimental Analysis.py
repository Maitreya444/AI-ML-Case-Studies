import pandas as pd
import spacy
import os

# Load spaCy model
nlp = spacy.load("en_core_web_md")

pd.set_option("display.max_rows", 200)

def Ner_Case_Claimant(text):
    result = []
    doc = nlp(text)

    # Filter for entities related to Claimant
    entities = [(ent.text, ent.start_char, ent.end_char, ent.label_)
                for ent in doc.ents if ("Appellant" in ent.text or "solicitors" in ent.text or "Claimant" in ent.text or "Claimants" in ent.text or "Claimant's" in ent.text or "Client" in ent.text) and ent.label_ in {"ORG", "PERSON"}]
    
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
    doc = nlp(text)

    # Filter for entities related to Defendant
    entities = [(ent.text, ent.start_char, ent.end_char, ent.label_)
                for ent in doc.ents if ("Defendant" in ent.text or "Respondent" in ent.text or "defendant's" in ent.text or "defendant" in ent.text) and ent.label_ in {"ORG", "PERSON"}]
    
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

def ClaimantSentenceAnalysis(text, reference_sentence):
    doc = nlp(text)
    ref_doc = nlp(reference_sentence)

    # Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    # Calculate similarities between sentences and reference sentence
    similarities = []

    for sent in sentences:
        # Compare with the reference sentence
        ref_sim = ref_doc.similarity(nlp(sent))
        similarities.append((ref_sim, reference_sentence, sent))

    # Sort similarities by score in descending order
    similarities.sort(reverse=True, key=lambda x: x[0])

    # Collect the top 2 pairs without repeating sentences
    top_sentences = []
    used_sentences = set()

    for sim, ref_sent, sent in similarities:
        if len(top_sentences) >= 2:
            break
        if sent not in used_sentences:
            top_sentences.append((sim, ref_sent, sent))
            used_sentences.add(sent)

    result = []
    points = 1
    for sim, ref_sent, sent in top_sentences:
        result.append(f"{points}. Reference: {ref_sent} \nSentence: {sent} \nSimilarity Score: {sim:.2f}")
        points += 1
    
    return result

def DefendantSentenceAnalysis(text, reference_sentence):
    doc = nlp(text)
    ref_doc = nlp(reference_sentence)

    # Extract sentences
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]

    # Calculate similarities between sentences and reference sentence
    similarities = []

    for sent in sentences:
        # Compare with the reference sentence
        ref_sim = ref_doc.similarity(nlp(sent))
        similarities.append((ref_sim, reference_sentence, sent))

    # Sort similarities by score in descending order
    similarities.sort(reverse=True, key=lambda x: x[0])

    # Collect the top 2 pairs without repeating sentences
    top_sentences = []
    used_sentences = set()

    for sim, ref_sent, sent in similarities:
        if len(top_sentences) >= 2:
            break
        if sent not in used_sentences:
            top_sentences.append((sim, ref_sent, sent))
            used_sentences.add(sent)

    result = []
    points = 1
    for sim, ref_sent, sent in top_sentences:
        result.append(f"{points}. Reference: {ref_sent} \nSentence: {sent} \nSimilarity Score: {sim:.2f}")
        points += 1
    
    return result

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

    # Define reference sentences
    reference_sentence_claimant = "Claimant argues in the court"
    reference_sentence_defendant = "Defendant argues in the court"

    # Handle or display the output_content
    if output_content1:
        for entity in output_content1:
            analysis_results = ClaimantSentenceAnalysis(entity, reference_sentence_claimant)
            print("Claimants:")
            for analysis_result in analysis_results:
                print(analysis_result)

    if output_content2:
        for entity in output_content2:
            analysis_results = DefendantSentenceAnalysis(entity, reference_sentence_defendant)
            print("Defendants:")
            for analysis_result in analysis_results:
                print(analysis_result)

if __name__ == "__main__":
    main()
