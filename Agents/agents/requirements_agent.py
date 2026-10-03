import time
class RequirementsAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict) -> dict:
        text = state.get("clean_text", "")
        prompt = f"Extract key client requirements and objectives from this document text:\n\n{text}"
        response = self.llm.invoke(prompt)
        time.sleep(2)
        return {"requirements": response.content}