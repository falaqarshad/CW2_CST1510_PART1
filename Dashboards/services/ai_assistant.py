class AIAssistant:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.history = []

    def send_message(self, message: str) -> str:
        self.history.append(message)
        return f"[AI Response] {message}"

    def clear_history(self):
        self.history.clear()