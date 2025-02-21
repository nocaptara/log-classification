import joblib
from sentence_transformers import SentenceTransformer

model_embedding = SentenceTransformer('all-MiniLM-L6-v2')  
model_classification = joblib.load("models/log_classifier.joblib")

def classify_with_bert(log_message):
    message_embedding = model_embedding.encode(log_message)  # ✅ Correct variable name
    probabilities = model_classification.predict_proba([message_embedding])[0]  # ✅ Added missing probability computation
    
    max_prob = max(probabilities)  # ✅ Now probabilities are properly defined
    if max_prob < 0.5:
        return "Unclassified"
    
    predicted_label = model_classification.predict([message_embedding])[0]  # ✅ Corrected variable name
    return predicted_label

if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)
