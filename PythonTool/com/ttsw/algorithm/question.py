#!/usr/bin/python
# Filename: question.py

from math import sqrt


def q1():
    s = (1, 2, 3, 4)
    for a in s:
        for b in s:
            for c in s:
                if a != b and b != c and c != a:
                    print"%d%d%d" % (a, b, c)


def q2():
    i = 1
    while i < 100000:
        a = int(sqrt(i + 100))
        b = int(sqrt(i + 268))
        if a ** 2 == (i + 100) and b ** 2 == (i + 268):
            print i
        i += 1


def q3():
    days = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
            7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}
    year, month, day = input("year:"), input("month:"), input("day:")
    if not days.has_key(month):
        print"error input"
    sum = days[month] + day
    if month >= 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            sum += 1
    print"it is the %dth day of the year." % sum


def q4(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
        print"small to big: %d,%d,%d" % (a, b, c)
    s = [a, b, c]
    s.sort()
    print"small to big: %s" % s


def q5():
    count = 0
    flag = 1
    for a in range(101, 201):
        s = int(sqrt(a))
        for i in range(2, s + 1):
            if a % i == 0:
                flag = 0
                break
        if flag == 1:
            count += 1
            print a
        else:
            flag = 1
    print "the total num is %d" % count


def q6(a, b):
    s = [a, b]
    s.sort()
    a, b = s[0], s[1]
    while b != 0:
        t = a % b
        a = b
        b = t
    print "common divisor:%d" % a
    print "common multiple:%d" % int(s[0] * s[1] / a)


def q7():
    s1 = 1
    for day in range(10, 1, -1):
        s2 = (s1 + 1) * 2
        s1 = s2
    print"the total number is %d" % s1


def q8():
    a, s = 1, 1
    for n in range(2, 21):
        for i in range(1, n + 1):
            a *= i
        s += a
        a = 1
    print"sum = %d" % s


def fact(j):
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum

#print "Fact:",fact(5)

if __name__ == "__main__": 
    myParams = {"server":"mpilgrim",\
                "database":"master",\
                "pwd":"secret"\
                }
    print "question:",q7()