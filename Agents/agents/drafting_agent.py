
import time
class DraftingAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict) -> dict:
        reqs = state.get("requirements", "")
        research = state.get("research_data", "")
        feedback = state.get("audit_feedback", "")
        loop_count = state.get("loop_count", 0) + 1

        prompt = f"""Draft a comprehensive professional report based on:
Requirements: {reqs}
Research: {research}
Previous Audit Feedback (if any): {feedback}
"""

        response = self.llm.invoke(prompt)
        
        # Content handling for safe output format
        content = response.content
        if isinstance(content, list):
            content = " ".join([str(item) for item in content])
        else:
            content = str(content)
        time.sleep(2)    
        return {"draft": content, "loop_count": loop_count}