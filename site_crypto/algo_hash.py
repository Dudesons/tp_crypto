import string
from random import randint, choice


def hash_algo(pwd):
    if len(pwd) <= 0:
        return (False, "Password lenght = 0")

    list_ascii = list()
    j = 5
    hash_list = list()
    hash_final = str()
    k = 0


    while j < len(pwd):
        j += 5

    pwd = "{0}{1}".format(pwd, pwd[0:(j - len(pwd))])

    for i in pwd:
        t = int(ord(str(i))) + 3
        if t > 127:
            t = t - 127

        list_ascii.append(t)

    while k < len(list_ascii):
        #coef_chunk = k+5
        coef_chunk = len(pwd)/5
        hash_chunk = 0
        for l in list_ascii[k:k+coef_chunk]:
            if hash_chunk > 127:
                hash_chunk -= l
            else:
                hash_chunk += l

        if hash_chunk > 127:
            hash_chunk = hash_chunk - 127
        hash_list.append(hash_chunk)

        k += coef_chunk

    print "="*20
    print hash_list
    print "="*20

    cc = 0
    while cc < len(hash_list):
        if hash_list[cc] < 48:
            hash_list[cc] = hash_list[cc] + 48

        cc += 1

    for i in hash_list:
        hash_final += unichr(i)

    return (True, hash_final)

if __name__ == "__main__":
    for x in range(20):
        print "="*20
        password = ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(randint(1, 247)))
        r = hash_algo(password)
        print r[1]
        print len(r[1])
