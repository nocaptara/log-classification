import os  # 🔹 FIXED: Added for handling file paths
import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

from classify import classify

app = FastAPI()

@app.post("/classify/")
async def classify_logs(file: UploadFile):
    # 🔹 FIXED: Ensure file extension check is case insensitive
    if not file.filename.lower().endswith('.csv'):
        raise HTTPException(status_code=400, detail=f"File must be a CSV. Uploaded: {file.filename}")

    try:
        # 🔹 FIXED: Use 'utf-8' encoding to handle special characters
        df = pd.read_csv(file.file, encoding="utf-8")

        # 🔹 FIXED: Added a check for missing or empty CSV files
        if df.empty:
            raise HTTPException(status_code=400, detail="Uploaded CSV file is empty.")

        # 🔹 FIXED: Ensure required columns exist
        required_columns = {"source", "log_message"}
        if not required_columns.issubset(df.columns):
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")

        # Perform classification
        df["target_label"] = classify(list(zip(df["source"], df["log_message"])))

        print("Dataframe:", df.to_dict())

        # 🔹 FIXED: Ensure 'resources' directory exists before saving the file
        output_dir = "resources"
        os.makedirs(output_dir, exist_ok=True)  
        output_file = os.path.join(output_dir, "output.csv")

        df.to_csv(output_file, index=False)
        print(f"File saved to {output_file}")

        return FileResponse(output_file, media_type='text/csv', filename="classifiedlogs_output.csv")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        file.file.close()
