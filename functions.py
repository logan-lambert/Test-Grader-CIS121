def read_txt_file(directory: str) -> list[str]:
    with open(directory, "r") as file:
        contents = file.readlines()
        for i, content in enumerate(contents):
            contents[i] = content.rstrip("\n")

        return contents

def grader(student_response: list[str], answers: list[str]) -> tuple[str, int]:
    name = student_response[0]
    correct_answers = 0
    for i, choice in enumerate(student_response[1::]):
        if choice == answers[i]:
            correct_answers += 1

    score = round((correct_answers / len(answers)) * 100)
    return (name, score)

def write_scores(directory: str, scores: list[tuple[str, int]], class_average: int) -> None:
    with open(directory, "w") as file:
        file.write(f"Class Average - {class_average}%\n")
        for i in scores:
            file.write(f"{i[0]} - {i[1]}%\n")

    return None
    
def class_average_calc(scores: list[tuple[str, int]]) -> int:
    sum_scores = 0
    for i in scores:
        sum_scores += i[1]
    
    average_percent = round((sum_scores / len(scores)))
    return average_percent
