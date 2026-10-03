from agents.utils import markdown_table_to_dicts, clean_cell
from fastapi import FastAPI, UploadFile, File
import shutil
import os
from graph import app as agent_system

api_app = FastAPI()

@api_app.post("/process-document")
async def process_document(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    initial_state = {
        "pdf_path": temp_path,
        "loop_count": 0,
        "is_approved": False
    }
    
    result = agent_system.invoke(initial_state)
    
    if os.path.exists(temp_path):
        os.remove(temp_path)
        
        requirements_rows = markdown_table_to_dicts(result.get("requirements", ""))
    research_rows = markdown_table_to_dicts(result.get("research_data", ""))

    return {
        "status": "success",
        "requirements_rows": requirements_rows,
        "research_rows": research_rows,
        "draft": clean_cell(result.get("draft", "")),
        "result": result,   # purana format bhi rakha hai
    }