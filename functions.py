from Test import Test

def read_txt_file(directory: str) -> list[str]: # Reads txt files line by lines and retuns content
    with open(directory, "r") as file:
        contents = file.readlines()
        for i, content in enumerate(contents):
            contents[i] = content.rstrip("\n")

        return contents

def write_scores(directory: str, tests: list[Test], class_average: int) -> None: # Writes final scores to specified txt file
    with open(directory, "w") as file:
        #file.write(f"Class Average - {class_average}%\n")
        file.write("Name    Score\n")
        for test in tests:
            file.write(f"{test.return_name()}   {test.return_score()}%\n")
        file.write(f"\nClass Average - {class_average}%")

    return None
    
def class_average_calc(scores: list[int]) -> int: # Calculates class average score
    sum_scores = 0
    for i in scores:
        sum_scores += i
    
    average_percent = round((sum_scores / len(scores)))
    return average_percent
