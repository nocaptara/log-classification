# Log Classification App

## Overview

The **Log Classification App** is a web-based tool that classifies log messages from a CSV file using various classification methods, including **Regular Expressions (Regex)**, **BERT**, and **LLM (Large Language Model)**. The frontend is built using **Streamlit**, while the backend API is powered by **FastAPI**.

## Features

- Upload a CSV file containing logs for classification.
- Classify logs using:
  - **Regex-based classification** for structured logs.
  - **BERT-based classification** for unstructured logs.
  - **LLM-based classification** for logs from specific sources (e.g., `LegacyCRM`).
- Download classified logs as a CSV file.
- Fast and efficient processing via FastAPI.

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Log Classification Methods:**
  - **Regex-based** (`processor_regex.py`)
  - **BERT-based** (`processor_bert.py`)
  - **LLM-based** (`processor_llm.py`)
- **File Handling:** Pandas
- **LLM API:** Groq API (Llama-based model)

---

## Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/your-repo/log-classification.git
cd log-classification
