from data import data_text_string


def day2():
    def string_split(pw_string):
        return pw_string.split()

    def calculate_path(travel_map, travel_step=[3, 1]):
        trees_encountered = 0
        start_pos_x = 0
        pos_x = start_pos_x

        for row in range(0, len(travel_map), travel_step[1]):
            if(pos_x > len(travel_map[row])-1):
                pos_x -= len(travel_map[row])
            if(travel_map[row][pos_x] == "#"):
                trees_encountered += 1
            pos_x += travel_step[0]
        return trees_encountered

    def all_paths(travel_map):
        trees_encountered = []
        travel_steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
        for path in travel_steps:
            path_result = calculate_path(travel_map, path)
            trees_encountered.append(path_result)
        return trees_encountered

    def init():
        solved_paths = all_paths(string_split(data_text_string))
        part_one = solved_paths[1]
        part_two = 0
        for i, trees in enumerate(solved_paths):
            if(i == 0):
                part_two += trees
            else:
                part_two *= trees

        print(
            f"""\nDay 3\n==============================================\nSolution -- Part One: {part_one}\nSolution -- Part Two: {part_two} """)
    init()


day2()
