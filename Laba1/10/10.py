import re


def password():
    print('Введите пароль\nПароль должен состоять из 6 - 12 символов.\n')

    while True:
        pswrd = input('Password: ')
        if 6 <= len(pswrd):
            break
        print('The password must be between 6 characters.\n')

    password_scores = {0: 'Horrible', 1: 'Weak', 2: 'Medium', 3: 'Strong'}
    password_strength = dict.fromkeys(['has_upper', 'has_lower', 'has_num'], False)
    if re.search(r'[A-Z]', pswrd):
        password_strength['has_upper'] = True
    if re.search(r'[a-z]', pswrd):
        password_strength['has_lower'] = True
    if re.search(r'[0-9]', pswrd):
        password_strength['has_num'] = True

    score = len([x for x in password_strength.values() if x])

    print('Password is %s' % password_scores[score])


password()
