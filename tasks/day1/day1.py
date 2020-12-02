from .data import number_txt_string


def day1():
    def string_split(numstr):
        return numstr.split()

    def convert_to_number(numstr):
        numbers = []
        for entry in numstr:
            numbers.append(int(entry))
        return numbers

    def return_numbers(numbers):
        two_numbers = []
        three_numbers = []
        for i, num in enumerate(numbers, start=0):
            for j, num2 in enumerate(numbers, start=i+1):
                if num + num2 == 2020:
                    two_numbers = [num, num2]
                for k, num3 in enumerate(numbers, start=j+1):
                    if num + num2 + num3 == 2020:
                        three_numbers = [num, num2, num3]
        return two_numbers, three_numbers

    def calculate_answer(numbers):
        answer_two_num = numbers[0][0] * numbers[0][1]
        answer_three_num = numbers[1][0] * numbers[1][1] * numbers[1][2]
        return numbers, answer_two_num, answer_three_num

    def init():
        numbers = calculate_answer(return_numbers(
            convert_to_number(string_split(number_txt_string))))
        print("\nDay 1 solution")
        print("==============================================")
        print("The numbers -- ", numbers[0])
        print("Solution -- Part One: ", numbers[1])
        print("Solution -- Part Two: ",
              numbers[2])

    init()


day1()
