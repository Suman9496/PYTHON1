import transformers

# Load a pre-trained language model
model = transformers.AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")

# Encode a sentence
sentence = "This is a positive sentiment sentence."
encoded_sentence = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")(sentence, return_tensors="pt")

# Predict the sentiment of the sentence
outputs = model(encoded_sentence)
predictions = outputs.logits.argmax(dim=-1)

# Print the prediction
print(predictions)
