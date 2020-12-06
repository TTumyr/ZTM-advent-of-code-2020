with open('data.txt') as file:
    data_txt = file.read().split("\n\n")


def day6():
    def calculate_count_combined(data):
        total_groups = list(group.split() for group in data)
        num_any_group_answers = 0
        num_shared_answers = 0
        for group in total_groups:
            answers = {}
            for person in group:
                for answer in person:
                    if(answer in answers):
                        answers[answer] = answers[answer] + 1
                    else:
                        answers[answer] = 1
            num_any_group_answers += len(answers)
            num_shared_answers += len([i for i,
                                       j in answers.items() if j == len(group)])
        return num_any_group_answers, num_shared_answers

    def init():
        result = calculate_count_combined(data_txt)
        part_one = result[0]
        part_two = result[1]
        print(
            f"\nDay 6\n======\nSolution -- Part One: {part_one}\nSolution -- Part Two: {part_two}")
    init()


day6()
