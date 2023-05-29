# The purpose of this program is to simulate a simple password strength checker
import re

# BEGIN FUNCTIONS
def checkPassword(password, requirements):
    result = False

    checks = {}

    # check password length
    if len(password) >= requirements["minPWDLen"]:
        checks["length"] = True;
    else:
        checks["length"] = False;

    # check number of upper case characters
    upCaseCharCount = 0

    for character in password:
        if (re.match('[A-Z]', character)):
            upCaseCharCount = upCaseCharCount + 1;

    if upCaseCharCount >= requirements["minUpperCaseLetters"]:
        checks["minUpper"] = True;
    else:
        checks["minUpper"] = False;

    # check number of numeric characters
    numCharCount = 0

    for character in password:
        if character.isnumeric():
            numCharCount = numCharCount + 1;

    if numCharCount >= requirements["minNumericChars"]:
        checks["minNumeric"] = True;
    else:
        checks["minNumeric"] = False;

    # check number of special characters
    specCharCount = 0

    for character in password:
        if re.match('[|^&+\-%*/=!>\.]', character):
           specCharCount = specCharCount + 1;

    if specCharCount >= requirements["minSpecialChars"]:
        checks["minSpecial"] = True;
    else:
        checks["minSpecial"] = False;

    print(f"Criteria: {requirements}")
    print(f"Check   : {checks}")

    # make sure all checks are "True". If so, then set strong to True
    if all(checks.values()):
        result = True;

    return result
### END FUNCTIONS

### request password
myPWD = input('enter a password: ').strip()

while len(myPWD) == 0:
    myPWD = input('enter a password: ').strip();

requirements = {}

# Requirements for a "strong" password
requirements["minPWDLen"] = 8
requirements["minUpperCaseLetters"] = 1
requirements["minNumericChars"] = 2
requirements["minSpecialChars"] = 1

print("Chack for strong password")
strongPWD = checkPassword(myPWD, requirements)

if strongPWD:
    print('\nStrong Password');
else:
    requirements.clear()

    # Requirements for a "weak" password
    requirements["minPWDLen"] = 6
    requirements["minUpperCaseLetters"] = 1
    requirements["minNumericChars"] = 1
    requirements["minSpecialChars"] = 0

    print("\nCheck for weak password")
    weakPWD = checkPassword(myPWD, requirements)

    if weakPWD:
        print('\nWeak Password');
    else:
        print('\nUnacceptable Password');
