import time
class ResearchAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, state: dict) -> dict:
        prompt = f"In requirements ke mutabiq best industry practices aur extra helpful research context add karein:\n\nRequirements:\n{state['requirements']}"
        response = self.llm.invoke(prompt)
        time.sleep(2)
        return {"research_data": response.content}