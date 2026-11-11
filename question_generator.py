class QuestionGenerator:
    def __init__(self):
        self.var_a = None
        self.var_b = None
        self.answer = None

    def addition_generation(self) -> str:
        self.var_a = 10
        self.var_b = 5
        self.answer = self.var_a + self.var_b
        return f"What is {self.var_a} + {self.var_b}?"
