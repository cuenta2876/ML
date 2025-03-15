from transformers import pipeline

classifier = pipeline("text-classification", model="bert-base-multilingual-cased", device=-1)

def process_text(text):
    return classifier(text)