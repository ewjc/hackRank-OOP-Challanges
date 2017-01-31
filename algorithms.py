ALGORITHMS

(FROM WARMUP)
1. PLUS MINUS - 98.10%
import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

negative_count = 0.0
pos_count = 0.0
zero_count = 0.0

for index in arr:
    if index < 0:
        negative_count += 1
    elif index == 0:
        zero_count += 1
    elif index > 0:
        pos_count += 1

print(pos_count / n)
print(negative_count / n)
print(zero_count / n)

--------------------------------------------------------------

(FROM IMPLEMENTATION)
2. ANGRY PROFESSOR - 94.62%

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    students_ontime = 0

    for time in a:
        if time <= 0:
            students_ontime += 1

    if students_ontime >= k:
        print('NO')
    else:
        print('YES')

--------------------------------------------------------------

(FROM IMPLEMENTATION)
3. BETWEEN TWO SETS - 87.43%

import sys

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

total_x_numbers = 0

def loop_a(x):
    for a_number in a:
        if x % a_number == 0:
            continue
        else:
            return False
    return True

def loop_b(x):
    for b_number in b:
        if b_number % x == 0:
            continue
        else:
            return False
    return True

for x in range(a[0], b[-1] + 1):
    if loop_a(x):
        if loop_b(x):
            total_x_numbers += 1

print(total_x_numbers)

--------------------------------------------------------------
(FROM IMPLEMENTATION)
4. Save the Prisoner! - 75%
test_cases = int(raw_input())
arr = map(int,raw_input().strip().split(' '))

number_of_prisoners = arr[0]
number_of_sweets = arr[1]
prisoner_id = arr[2]


for i in range(prisoner_id, (number_of_sweets + number_of_prisoners - (number_of_prisoners - prisoner_id))):
    if i > number_of_prisoners:
        print(i - number_of_prisoners)
    else:
        print(i)
