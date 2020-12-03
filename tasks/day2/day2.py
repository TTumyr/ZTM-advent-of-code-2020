from data import password_db_string


def day2():
    def string_split(pw_string):
        return pw_string.split()

    def find_valid_passwords(pw_data):
        passwords = []
        tb_passwords = []
        for idx in range(0, len(pw_data), 3):
            tb_valid = False
            password_letter_count = 0
            pw_policy_letter = ""
            pw_policy_min_pos = int(pw_data[idx].split("-")[0])
            pw_policy_max_pos = int(pw_data[idx].split("-")[1])
            pw_policy_letter = pw_data[idx+1][0]
            for char_pos, entry in enumerate(pw_data[idx+2], start=1):
                if (entry == pw_policy_letter):
                    password_letter_count += 1
                    if(char_pos == pw_policy_min_pos or char_pos == pw_policy_max_pos):
                        tb_valid = not tb_valid
            if(tb_valid):
                tb_passwords.append(
                    [pw_data[idx], pw_data[idx+1], pw_data[idx+2]])
            if(password_letter_count >= pw_policy_min_pos and password_letter_count <= pw_policy_max_pos):
                passwords.append(
                    [pw_data[idx], pw_data[idx+1], pw_data[idx+2]])
        return passwords, tb_passwords

    def init():
        valid_passwords = find_valid_passwords(
            string_split(password_db_string))
        print(
            f"""\nDay 2\n==============================================\nSolution -- Part One: {len(valid_passwords[0])}\nSolution -- Part Two: {len(valid_passwords[1])} """)
    init()


day2()
