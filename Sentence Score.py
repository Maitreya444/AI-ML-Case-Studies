import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Define the documents
doc1 = nlp("Defendant argues in the Court")

# Sentences from the provided text
sentences = [
    "Third, the Defendant cannot rely on the submission that there was an implied agreement that it could render interim statute bills.",
    "Fourth, the Defendant cannot rely on the fact that the Claimant made regular payments on account as a basis for inferring, from this conduct, an agreement for the delivery of interim statute bills.",
    "Given that the retainer did not provide for the Defendant’s periodic invoices to be interim statute bills, when adopting the reasoning of CJ Leonard in Ivanishvili (ibid), there is no basis upon which I can infer from the fact of payment any agreement to the contrary.",
    "Ultimately, the bills rendered by the Defendant in October 2017 constituted a series of invoices which requested interim payments on account.",
    "On the question of estimates, the Claimant avers that the Defendant failed to provide him with adequate costs information and, specifically, failed to provide estimates in accordance with its statutory and professional obligations.",
    "Pursuant to the 34 disputed invoices, the Defendant charged the Claimant a total of £225,697.60 (including VAT), to a point where witness statements, any expert reports, further CCMC/CTR, trial preparation and trial were yet to occur.",
    "Turning to the ‘s.74(3) SA issue’, the Claimant submits that as this was a contentious County Court action, the Defendant was subject to a statutory prohibition that limits the amount payable by the Claimant to a sum which could have been allowed in respect of an item on inter partes assessment.",
    "This fact, submits the Claimant, does not appear to have been acknowledged or recognised by the Defendant in its invoices/billing.",
    "The Defendant, in summary, submits that the Claimant was “provided with proper costs information” in that “numerous costs update letters [were] sent, as well as the regular invoicing” (Defendant’s Skeleton Argument, para. 26).",
    "Looking at the table of relevant correspondence set out in the Defendant’s Skeleton Argument, however, it seems common ground that the last relevant letter was that sent on 5th October 2021 and that the last estimate provided by the Defendant to the Claimant was £150,000 – £175,000 (plus VAT) to completion.",
    "With regard to the s.74(3) SA 1974 point, the Defendant points out that the costs bill to the Claimant “did not exceed the estimated costs in the budget”, with the consequence that the issue is unlikely to be of practical relevance on assessment.",
    "The Defendant, in summary bemoans “excessive delay in this case”, referring again to the fact that the Claimant’s action issued in April 2022 only sought assessment of the 8 most recent invoices.",
    "Echoing the evidence of Ms Wong (380), it was submitted that the Defendant has been prejudiced by this delay, in terms of cost protection in seeking an assessment of the earlier invoices now, belatedly ordered.",
    "In this case, in fact, the Claimant was clear from the outset that he intended to challenge the entirety of the Defendant’s billing, and that this desire was considered repeatedly in correspondence prior to the Application issued in May 2023.",
    "Given, moreover, payments made by the Claimant account for over 85% of the overall billing, the Defendant has not been substantively deprived of funds and there is, contrary to the solicitor’s submission, no scope (at least at this stage) for a further payment on account and/or any form of wasted costs order."
]

# Compute similarity between doc1 and each sentence
for i, sentence in enumerate(sentences, start=1):
    doc = nlp(sentence)
    similarity = doc1.similarity(doc)
    print(f"Similarity between doc1 and sentence {i}: {similarity:.4f}")
