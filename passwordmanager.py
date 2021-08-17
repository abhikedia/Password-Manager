class BasePasswordManager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        if len(self.old_passwords):
            return self.old_passwords[len(self.old_passwords)-1]
        else:
            return "Password list empty"

    def is_correct(self, password):
        if len(self.old_passwords):
            if self.old_passwords[len(self.old_passwords)-1] == password:
                return 'Passwords match!'
            else:
                return 'Passwords don\'t match!'
        else:
            return "Password list empty"


class PasswordManager(BasePasswordManager):
    def __init__(self):
        self.level = 0
        BasePasswordManager.__init__(self)

    def set_password(self, password):
        if len(password) >= 6:
            alpha = 0
            numbers = 0
            special = 0
            for _ in range(len(password)):
                if(password[_].isalpha()):
                    alpha = alpha+1
                elif (password[_].isnumeric()):
                    numbers = numbers+1
                else:
                    special = special+1
            if(special > 0):
                level = 3
            elif (alpha > 0 and numbers > 0):
                level = 2
            else:
                level = 1

            if(level == 3 or level > self.level):
                self.old_passwords.append(password)
                self.level = level
                print('Password change successful!')
            else:
                print('Password change failed!')
        else:
            print('Password change failed!')

    def get_level(self):
        return self.level


p = PasswordManager()
while True:
    print('Choose one of the following options:\n')
    print('1. Set new password\n2. Get current password\n3. Get password level\n4. Check Password\n5.Exit')
    option = int(input())
    if option == 1:
        p.set_password(input('Enter new password:'))
    elif option == 2:
        print(p.get_password())
    elif option == 3:
        print(p.get_level())
    elif option == 4:
        x=input('Enter current password:')
        print(p.is_correct(x))
    else:
        break
