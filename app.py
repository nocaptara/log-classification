import streamlit as st
import requests
import pandas as pd
from io import BytesIO

# FastAPI Backend URL
FASTAPI_URL = "http://127.0.0.1:8000/classify/"

# Streamlit App UI
st.title("Log Classification App")
st.write("Upload a CSV file containing logs for classification.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Display uploaded file
    st.write("Uploaded file:", uploaded_file.name)

    if st.button("Classify Logs"):
        with st.spinner("Processing..."):
            # 🔹 FIXED: Send file in the correct format
            files = {"file": ("filename.csv", uploaded_file, "text/csv")}  # Proper file tuple

            try:
                response = requests.post(FASTAPI_URL, files=files)

                if response.status_code == 200:
                    # 🔹 FIXED: Ensure response content is properly parsed
                    df = pd.read_csv(BytesIO(response.content), encoding="utf-8")  

                    st.write("### Classified Data Preview:")
                    st.dataframe(df)

                    # Create a download link
                    st.download_button(
                        label="Download Classified CSV",
                        data=response.content,
                        file_name="classified_output.csv",
                        mime="text/csv",
                    )
                else:
                    error_message = response.json().get("detail", "Unknown error occurred.")  # 🔹 FIXED: Handle error messages better
                    st.error(f"Error: {error_message}")

            except requests.exceptions.RequestException as e:
                st.error(f"Failed to connect to server: {str(e)}")  # 🔹 FIXED: Handle server connection errors gracefully
