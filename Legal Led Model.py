import os
import json
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("nsi319/legal-led-base-16384")
model = AutoModelForSeq2SeqLM.from_pretrained("nsi319/legal-led-base-16384")

input_directory = r"C:\Users\DELL\OneDrive\Desktop\Programming\Projects\Freelancing\Penelope\articles"
output_directory = r"C:\Users\DELL\OneDrive\Desktop\Programming\Projects\Freelancing\Penelope\articles\NLP"
processed_files_path = r"C:\Users\DELL\OneDrive\Desktop\Programming\Projects\Freelancing\Penelope\articles\processed_files.json"

# Function to load processed_files from JSON, handling empty file or non-existent file
def load_processed_files():
    if os.path.exists(processed_files_path):
        with open(processed_files_path, 'r') as f:
            try:
                processed_files = json.load(f)
            except json.JSONDecodeError:
                processed_files = []
    else:
        processed_files = []
    return processed_files

processed_files = load_processed_files()

def summarize_text(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        legal_text = file.read()

    inputs = tokenizer(legal_text, return_tensors="pt", max_length=16384, truncation=True)

    summary_ids = model.generate(inputs["input_ids"], max_length=1024, min_length=30, length_penalty=2.0, num_beams=5, no_repeat_ngram_size=2, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Creating output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith(".txt") and filename not in processed_files:
        file_path = os.path.join(input_directory, filename)

        summary = summarize_text(file_path)

        output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_summary.txt")
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            output_file.write(summary)

        processed_files.append(filename)

# Save updated processed_files list to JSON
with open(processed_files_path, "w") as f:
    json.dump(processed_files, f)
