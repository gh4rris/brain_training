import random


class QuestionGenerator:
    def __init__(self):
        self.var_a = 0
        self.var_b = 0
        self.question_types = ["add", "sub", "mul"]

    def __set_variables(self) -> None:
        self.var_a = round(random.uniform(-100, 100), 2)
        self.var_b = round(random.uniform(-100, 100), 2)

    def __addition_generation(self) -> tuple[str, float]:
        self.__set_variables()
        answer = round(self.var_a + self.var_b, 2)
        return f"What is {self.var_a} + {self.var_b}?", answer
    
    def __subtraction_generation(self) -> tuple[str, float]:
        self.__set_variables()
        answer = round(self.var_a - self.var_b, 2)
        return f"What is {self.var_a} - {self.var_b}?", answer

    def __multiplication_generation(self) -> tuple[str, float]:
        self.var_a = random.randrange(-100, 101)
        self.var_b = random.randrange(-100, 101)
        answer = self.var_a * self.var_b
        return f"What is {self.var_a} * {self.var_b}?", answer

    def choose_question(self) -> tuple[str, float]:
        question_type = random.choice(self.question_types)
        match question_type:
            case "add":
                return self.__addition_generation()
            case "sub":
                return self.__subtraction_generation()
            case "mul":
                return self.__multiplication_generation()
            case _:
                return self.__addition_generation()
