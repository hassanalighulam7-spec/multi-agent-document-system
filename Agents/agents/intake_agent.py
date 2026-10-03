import pypdf
import time

class IntakeAgent:
    def run(self, state: dict) -> dict:
        pdf_path = state.get("pdf_path", "")
        extracted_text = ""
        try:
            reader = pypdf.PdfReader(pdf_path)
            for page in reader.pages:
                extracted_text += page.extract_text() or ""
        except Exception as e:
            extracted_text = f"Error reading PDF: {e}"
        time.sleep(2)
        return {"clean_text": extracted_text}