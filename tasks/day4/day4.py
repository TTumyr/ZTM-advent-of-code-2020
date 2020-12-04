import re
with open('data.txt') as file:
    data_txt = file.read()


def day4():
    def convert_txt_to_data(data_txt):
        passports = []
        for p_port in data_txt.split("\n\n"):
            passports.append(p_port.split())
        return passports

    def simple_validity_check(passports):
        simple_passports = []
        simple_passports_count = 0
        for p_port in passports:
            check_list = []
            for field in p_port:
                check_list.append(field.split(":")[0])
            if(len(check_list) >= 8 or (len(check_list) >= 7 and not any("cid" in check for check in check_list))):
                simple_passports.append(p_port)
                simple_passports_count += 1
        return simple_passports, simple_passports_count

    def improved_validity_check(passports):
        validity_rules = {
            "byr": "^(19[2-9][0-9]|20[0][0-2])$",
            "iyr": "^(20[1][0-9]|20[2][0])$",
            "eyr": "^(20[2][0-9]|20[3][0])$",
            "hgt": "^(1[5-8][0-9]|19[0-3])cm$|^(59|6[0-9]|7[0-6])in$",
            "hcl": "^\#([0-9a-f]){6}$",
            "ecl": "^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$",
            "pid": "^[0-9]{9}$"
        }
        improved_passports = []
        improved_passports_count = 0
        for p_port in passports[0]:
            check_list = []
            for field in p_port:
                if(field.split(":")[0] in validity_rules and re.search(validity_rules[field.split(":")[0]], field.split(":")[1])):
                    check_list.append(field.split(":")[0])
            if(len(check_list) >= 8 or (len(check_list) >= 7 and not any("cid" in check for check in check_list))):
                improved_passports.append(p_port)
                improved_passports_count += 1
        return improved_passports, improved_passports_count, passports[1]

    def init():
        result = improved_validity_check(
            simple_validity_check(convert_txt_to_data(data_txt)))
        part_one = result[2]
        part_two = result[1]
        print(
            f"\nDay 4\n======\nSolution -- Part One: {part_one}\nSolution -- Part Two: {part_two}")
    init()


day4()
