# This object hold test variables and respective methods
class Test:
    def __init__(self, name: str, answers: list[str]) -> None:
        self.name = name
        self.answers = answers
        self.score = 0

    def grade(self, key: list[str]) -> None: # Compares student answer to answer key
        for i in range(len(self.answers)):
            if self.answers[i] == key[i]:
                self.score += 1
        
        self.score = round((self.score / len(key)) * 100)

    def return_score(self) -> int:
        return self.score
    
    def return_name(self) -> str:
        return self.name
    