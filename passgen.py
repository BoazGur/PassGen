def main():
    password_length = 6
    password_seq = []
    floating_point_pos = 2
    for i in range(password_length):
        password_seq.append(ord('a'))

    while password_seq[0] != ord('z') + 1 or password_seq[1] != ord('z') + 1:
        for i in range(25):
            print_password_seq(password_seq)
            password_seq[-1] += 1
        
        print_password_seq(password_seq)

        if password_seq[1 - floating_point_pos] == ord('a'):
            password_seq[1 - floating_point_pos] = ord('z')

        if floating_point_pos > 6:
            return

        if password_seq[-floating_point_pos] == ord('z'):
            if floating_point_pos != 6:
                password_seq[-floating_point_pos] = ord('a')
            try:
                password_seq[-floating_point_pos - 1] += 1
            except:
                pass
            floating_point_pos += 1
        else:
            password_seq[-floating_point_pos] += 1
        
        password_seq[-1] = ord('a')

def print_password_seq(password_seq):
    temp = ""
    for letter in password_seq:
        temp += chr(letter)

    print(temp)

if __name__ == '__main__':
    main()