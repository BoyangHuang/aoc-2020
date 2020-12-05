valid_count = 0
with open("passwords.txt", mode="r", newline="\n") as f:
    lines = f.readlines()
    for line in lines:
        line_components = line.split()
        indx_1, indx_2 = line_components[0].split("-")
        letter = line_components[1].replace(":", "")
        password = line_components[2]
        try:

            indx_1_bool = password[int(indx_1)-1] == letter
            indx_2_bool = password[int(indx_2)-1] == letter
        except:
            print(line)
            continue
        if indx_1_bool != indx_2_bool:
            valid_count += 1
            print(line, password[int(indx_1)-1], password[int(indx_2)-1])

    # for line in lines:
    #     line_components = line.split()
    #     min_num, max_num = line_components[0].split("-")
    #     letter = line_components[1].replace(":", "")
    #     password = line_components[2]
    #     letter_count = password.count(letter)
    #     if int(min_num) <= letter_count <= int(max_num):
    #         print(line, letter_count, min_num, max_num)
    #         valid_count += 1

print("VALID COUNT: ", valid_count)

