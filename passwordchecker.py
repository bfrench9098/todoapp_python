# The purpose of this program is to simulate a simple password strength checker
import re

# BEGIN FUNCTIONS
def checkForStrongPassword(password):
    ### Requirements for a "strong" password
    minPWDLenStrong = 8
    minUpperCaseLettersStrong = 1
    minNumericCharsStrong = 2
    minSpecialCharsStrong = 1

    strong = False
    count = 0

    # check password length
    if len(password) >= minPWDLenStrong:
        count = count + 1;

    # check number of upper case characters
    upCaseCharCount = 0

    for character in password:
        if (re.match('[A-Z]', character)):
            upCaseCharCount = upCaseCharCount + 1;

    if upCaseCharCount >= minUpperCaseLettersStrong:
        count = count + 1;

    # check number of numeric characters
    numCharCount = 0

    for character in password:
        if character.isnumeric():
            numCharCount = numCharCount + 1;

    if numCharCount >= minNumericCharsStrong:
        count = count + 1;

    # check number of special characters
    specCharCount = 0

    for character in password:
        if (re.match('[|^&+\-%*/=!>\.]', character)):
           specCharCount = specCharCount + 1;

    if specCharCount >= minSpecialCharsStrong:
        count = count + 1;

    if count == 4:
        strong = True;

    return strong

def checkForWeakPassword(password):
    ### Requirements for a "weak" password
    minPWDLenWeak = 6
    minUpperCaseLettersWeak = 1
    minNumericCharsWeak = 1
    minSpecialCharsWeak = 0

    weak = False;
    count = 0

    # check password length
    if len(password) >= minPWDLenWeak:
        count = count + 1;

    # check number of upper case characters
    upCaseCharCount = 0

    for character in password:
        if (re.match('[A-Z]', character)):
            upCaseCharCount = upCaseCharCount + 1;

    if upCaseCharCount >= minUpperCaseLettersWeak:
        count = count + 1;

    # check number of numeric characters
    numCharCount = 0

    for character in password:
        if character.isnumeric():
            numCharCount = numCharCount + 1;

    if numCharCount >= minNumericCharsWeak:
        count = count + 1;

    # check number of special characters
    specCharCount = 0

    for character in password:
        if (re.match('[|^&+\-%*/=!>\.]', character)):
           specCharCount = specCharCount + 1;

    if specCharCount >= minSpecialCharsWeak:
        count = count + 1;

    if count == 4:
        weak = True;

    return weak
### END FUNCTIONS

### request password
myPWD = input('enter a password: ').strip()

while len(myPWD) == 0:
    myPWD = input('enter a password: ').strip();

strongPWD = checkForStrongPassword(myPWD)
weakPWD = checkForWeakPassword(myPWD)

if strongPWD:
    print('Strong Password');
elif weakPWD:
    print('Weak Password');
else:
    print('Unacceptable Password');

