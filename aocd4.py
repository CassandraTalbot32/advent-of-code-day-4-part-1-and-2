fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
good_passports = []

def is_valid_passport(pp):
    for field in fields:
        if field not in pp:
            return False
    return True

with open('day4data2.txt') as file:
    data = file.readlines()
    data = [ line.strip() for line in data ]

validCount = 0

currentPassport = ''
for line in data:
    if line != '':
        currentPassport += ' ' + line 

    else:
        if is_valid_passport(currentPassport):
            good_passports.append(currentPassport)
            validCount += 1

        currentPassport = ''

if is_valid_passport(currentPassport):
    validCount += 1

print(validCount)


def is_valid_byr(byr):
    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return False
    
    return True
#if issue year in range then valid 
def is_valid_iyr(iyr):
    iyr = int(iyr)

    if iyr < 2010 or iyr > 2020:
        return False
    
    return True
#if expiration year in range then valid
def is_valid_eyr(eyr):
    eyr = int(eyr)

    if eyr < 2020 or eyr > 2030:
        return False
    
    return True
    
#height must be in range for both cm and in other unit of measurement not valid, checking integer parameters
def is_valid_hgt(hgt):
    units = hgt[-2:]

    if units not in ['in', 'cm']:
        return False

    hgt = int(hgt[:-2])

    if units == 'in':
        if hgt < 59 or hgt > 76:
            return False 

    elif units == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    return True 
    
#if the first value for hair colour doesn't contain # then return false value
def is_valid_hcl(hcl):
    letters = ['a', 'b', 'c', 'd', 'e', 'f']

    if hcl not in letters:
        return False

    elif hcl[1] != '#': 
        return False 
    
#if the length of the str is not equal to 6 then return false value
    elif len(hcl[1:]) != 6:
        return False 
    
    return True
    
#if eye color different from those in list then not valid
def is_valid_ecl(ecl):
    colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    
    if ecl not in colours:
        return False
    
    return True 
#passport id must be nine digit number, can include leading 0's
def is_valid_pid(pid):
    pid = int(pid)
    
    if len(pid) != 9:
        return False
    
    return True    

def has_valid_data(passport):
    passport = passport.split()
    data = {}

    for item in passport:
        key = item[:3]
        value = item[4:]
        data[key] = value

    if not is_valid_byr(data['byr']):
        return False
    return True
    if not is_valid_iyr(data['iyr']):
        return False 
    return True
    if not is_valid_eyr(data['eyr']):
        return False 
    return True
    if not is_valid_hgt(data['hgt']):
        return False 
    return True
    if not is_valid_hcl(data['hcl']):
        return False 
    return True
    if not is_valid_ecl(data['ecl']):
        return False 
    return True
    if not is_valid_pid(data['pid']):
        return False 
    return True

validCount = 0

for pp in good_passports:
    if has_valid_data(pp):
       validCount += 1


print(validCount)


