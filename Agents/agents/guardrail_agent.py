import time

class GuardrailAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict) -> dict:
        pdf_path = state.get("pdf_path", "")
        
        prompt = f"Check if this file path or topic is safe to process: {pdf_path}. Reply with SAFE or UNSAFE."
        response = self.llm.invoke(prompt)
        
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
        else:
            content = str(content)
            
        is_safe = "SAFE" in content.upper() and "UNSAFE" not in content.upper()
        
        # --- Yahan add karein (return se pehle) ---
        time.sleep(2)
        
        return {"is_safe": is_safe}