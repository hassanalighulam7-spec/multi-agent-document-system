import time
class AuditAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict) -> dict:
        draft = state.get("draft", "")
        prompt = f"Audit this draft for quality and accuracy:\n\n{draft}\n\nIs it high quality and ready? Reply format:\nAPPROVED: Yes/No\nFEEDBACK: <your detailed notes>"
        response = self.llm.invoke(prompt)
        
        # Format response content properly if it's a list or str
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
        else:
            content = str(content)
        
        is_approved = "APPROVED: YES" in content.upper()
        time.sleep(2) 
        return {"is_approved": is_approved, "audit_feedback": content}
