# Log Classification System

A robust, hybrid log classification system that combines regex rules, machine learning (BERT + Logistic Regression), and LLM-based classification to accurately categorize IT and application logs. This project is designed for scalable, automated log analysis with both a web UI and REST API.

---

## Features

- **Hybrid Classification Pipeline**
  - **Regex-based:** Fast, rule-based labeling for common log patterns.
  - **BERT + Logistic Regression:** Handles complex or ambiguous logs using semantic embeddings.
  - **LLM (Llama-3 via Groq):** For rare/legacy logs and nuanced cases.
- **User-friendly Streamlit UI:** Upload logs, classify, preview, and download results.
- **REST API (FastAPI):** Programmatic access for integration and automation.
- **Extensible:** Easily add new regex rules or retrain ML models as log formats evolve.

---

## Folder Structure

```
.
├── app.py                  # Streamlit UI
├── server.py               # FastAPI backend
├── classify.py             # Hybrid classification logic
├── processor_regex.py      # Regex-based classification
├── processor_bert.py       # BERT + Logistic Regression classifier
├── processor_llm.py        # LLM-based classification (Groq API)
├── models/                 # Saved ML models (e.g., log_classifier.joblib)
├── resources/              # Test CSVs, output files, etc.
├── requirements.txt        # Dependencies
```

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download/Train ML Model

- Ensure `models/log_classifier.joblib` exists.  
- To retrain, use your labeled logs and `scikit-learn`.

### 3. Set API Keys

For LLM classification, set your Groq API key in a `.env` file:

```env
GROQ_API_KEY=your_key_here
```

### 4. Start the Backend

```bash
uvicorn server:app --reload
```

- API available at `http://127.0.0.1:8000/`
- Interactive docs at `/docs`

### 5. Run the Streamlit UI

```bash
streamlit run app.py
```

- Open the provided local URL in your browser.

---

## Usage

### Streamlit UI

1. Launch the app.
2. Upload a CSV file with `source` and `log_message` columns.
3. Click "Classify Logs".
4. Preview and download the classified results.

### API

- **Endpoint:** `POST /classify/`
- **Input:** CSV file (`source`, `log_message`)
- **Output:** CSV with added `target_label` column

---

## How It Works

1. **Upload logs** via UI or API.
2. **For each log:**
   - If `source` is "LegacyCRM", classify with LLM (`processor_llm.py`).
   - Else, try regex patterns (`processor_regex.py`).
   - If no regex match, use BERT+Logistic Regression (`processor_bert.py`).
3. **Results** are returned as a CSV with predicted labels.

---

## Example Regex Patterns

- `User User\d+ logged (in|out).` → User Action  
- `Backup completed successfully.` → System Notification  
- `Account with ID .* created by .*` → User Action

---

## Example ML Categories

- HTTP Status  
- Critical Error  
- Security Alert  
- Resource Usage  
- System Notification  
- User Action  
- Workflow Error  
- Deprecation Warning  
- Unclassified

---

## Sample Input CSV

| source        | log_message                                       |
|---------------|---------------------------------------------------|
| ModernCRM     | User User123 logged in.                           |
| BillingSystem | Backup completed successfully.                    |
| LegacyCRM     | The 'ReportGenerator' module will be retired ...  |

---

## Sample Output CSV

| source        | log_message                                       | target_label         |
|---------------|---------------------------------------------------|----------------------|
| ModernCRM     | User User123 logged in.                           | User Action          |
| BillingSystem | Backup completed successfully.                    | System Notification  |
| LegacyCRM     | The 'ReportGenerator' module will be retired ...  | Deprecation Warning  |

---

## Extending the System

- **Add new regex patterns:** Edit `processor_regex.py`.
- **Retrain ML model:** Use your labeled logs and update `models/log_classifier.joblib`.
- **Update LLM prompt or categories:** Edit `processor_llm.py`.

---

## License

This project is for educational use only.  
© 2025 Your Name/Organization. All rights reserved.

---

**For questions or contributions, open an issue or pull request!**
