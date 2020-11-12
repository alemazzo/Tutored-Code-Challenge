
def fun(passwords, verify):
    find = []
    pwd = verify
    for password in passwords:
        if password in verify:
            find.append(password)
            verify = verify.replace(password, '')
    output = "sicuro"

    if len(verify) == 0:
        output = ''
        i = 1
        while i <= len(pwd):
            substr = pwd[0:i]
            for p in passwords:
                if p == substr:
                    output += substr + " "
                    pwd = pwd[i: len(pwd)]
                    i = 0
                    break
            i += 1
    output[0:-1]
    return output


n = int(input())
for i in range(n):
    m = input()
    passwords = input().split()
    verify = input()
    print(fun(passwords, verify))
