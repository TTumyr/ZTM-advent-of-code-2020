with open('data.txt') as file:
    data_txt = file.read().split()


def day5():

    def convert_boarding_pass(data):
        boarding_pass = []
        for b_pass in data:
            row = 127 - int(b_pass[0:7].replace("F", "1").replace("B", "0"), 2)
            column = int(b_pass[7:10].replace("R", "1").replace("L", "0"), 2)
            seat_ID = row * 8 + column
            boarding_pass.append([row, column, seat_ID])
        return boarding_pass

    def calculate_seat_ID(data):
        seat_ID = []
        your_seat = 0
        for b_pass in data:
            seat_ID.append(b_pass[2])
        seat_ID.sort()
        for i, seat in enumerate(seat_ID):
            if(i < len(seat_ID)-1 and seat_ID[i+1] - seat != 1):
                your_seat = int(seat)+1
        return data, max(seat_ID), your_seat

    def init():
        result = calculate_seat_ID(
            convert_boarding_pass(data_txt))
        part_one = result[1]
        part_two = result[2]
        print(
            f"\nDay 5\n======\nSolution -- Part One: {part_one}\nSolution -- Part Two: {part_two}")
    init()


day5()
