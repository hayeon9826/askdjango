val = '01039329826'
# val = '01411111111'

# pattern = "01[016789][1-9][0-9]"

# '^01[0-9]\d{6,7}'

# if val.startswith("010") and len(val) == 11:
#     if val[:3] in ("010", "011", "016", "017", "018")
#         print("OK")

import re
if re.match('^01[016789][1-9]\d{7,8}$', val):
    print('match')
else:
    print('Wrong')

def validate_phone_number(number):
    if not re.match('^01[016789][1-9]\d{7,8}$', val):
        return False #후에 Form Validator에서 forms.ValidationError 예외처리
    return True