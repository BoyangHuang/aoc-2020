import re

valid_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid",]# "cid"]
passports = []
hcl_regex = r"^#[0-9a-f]{6}$"
valid_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
pid_regex = r"^[0-9]{9}$"

def check_passport(pp):
    passport_attributes = pp.keys()
    if not all(item in passport_attributes for item in valid_keys):
        return False

    byr = int(pp["byr"])
    if byr < 1920 or byr > 2002:
        print("invalid BYR", byr)
        return False

    iyr = int(pp["iyr"])
    if iyr < 2010 or iyr > 2020:
        print("invalid iyr", iyr)
        return False

    eyr = int(pp["eyr"])
    if eyr < 2020 or eyr > 2030:
        print("invalid EYR", eyr)
        return False

    hgt = pp["hgt"]
    hgt_unit = hgt[-2:]
    hgt_value = int(hgt[:-2])
    if hgt_unit not in ["in", "cm"]:
        print("INVALID HGT UNIT", hgt_unit)
        return False
    if hgt_unit == "in" and (hgt_value < 56 or hgt_value > 76):
        print("INVALID HGT IN", hgt_value)
        return False
    if hgt_unit == "cm" and (hgt_value < 150 or hgt_value > 193):
        print("INVALID HGT CM", hgt_value)
        return False

    hcl = pp["hcl"]
    if not re.match(hcl_regex, hcl):
        print("INVALID HCL", hcl)
        return False

    ecl = pp["ecl"]
    if ecl not in valid_ecl:
        print("INVALID ECL", ecl)
        return False

    pid = pp["pid"]
    if not re.match(pid_regex, pid):
        print("INVALID PID", pid)
        return False

    return True

with open("passports.txt", mode="r", newline="\n") as f:
    passport = {}
    for line in f.readlines():
        if len(line) <= 2:
            passports.append(passport)
            print("PASSPORT", passport)
            passport = {}
        fields = line.split()
        for field in fields:
            k, v = field.split(":")
            passport[k] = v

    passports.append(passport)


valid_passports = 0
for passport in passports:
    try:
        if check_passport(passport):
            valid_passports+=1
    except Exception as e:
        print(e)
print("VALID PASSPORTS", valid_passports)