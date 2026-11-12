class QuestionGenerator:
    def __init__(self):
        self.var_a = None
        self.var_b = None

    def addition_generation(self) -> tuple[str, float]:
        self.var_a = 10
        self.var_b = 5
        answer = self.var_a + self.var_b
        return f"What is {self.var_a} + {self.var_b}?", answer
