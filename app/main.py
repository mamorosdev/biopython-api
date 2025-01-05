from fastapi import FastAPI, HTTPException
from Bio.Seq import Seq
import time

app = FastAPI()

@app.get("/api/time")
def get_current_time():
    return {"time": time.time()}

@app.get("/api/sequence/rna/{seq}")
def rna(seq: str):
    if not seq or seq.strip() == "":
        raise HTTPException(status_code=400, detail="DNA sequence is required")
    
    seq_obj = Seq(seq.upper())
    rna = seq_obj.transcribe()
    # Hem de convertir l'ARN a string per serialitzar el JSON.
    return { "rna": str(rna) }

if __name__ == "__main__":
    app.run()

