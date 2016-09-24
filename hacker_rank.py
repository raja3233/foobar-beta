#
# def compute_reversibles(n):
#     count = 0
#     for i in range(1, n + 1):
#         str_i = str(i)
#         rev_i = int(str_i[::-1])
#         sum_i_r = i + rev_i
#         if len(str(rev_i)) != len(str_i):
#            continue
#         import re
#         even_digit=re.compile('[02468]')
#         y_n = 0 if even_digit.search(str(sum_i_r)) else 1
#         if y_n:
#             print("value are " , i, rev_i, sum_i_r,y_n)
#         count = count + y_n
#     return count
#
# if __name__ == "__main__":
#     tests = int(input())
#     for i in range(tests):
#         n = int(input())
#         print(compute_reversibles(n))
import re
buffer_value =[]
def compute_reversibles(n):
    count = 0

    for i in range(1, n):
        y_n = 0
        if i in buffer_value:
            count = count + 1
        else:
            print(i)
            str_i = str(i)
            rev_i = int(str_i[::-1])
            sum_i_r = i + rev_i
            if len(str(rev_i)) == len(str_i):
                even_digit=re.compile('[02468]')
                if even_digit.search(str(sum_i_r)) is None:
                    y_n = 1
                    buffer_value.append(i)
            print("value are " , i, rev_i, sum_i_r,y_n)
            count = count + y_n
    return count

if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        n = int(input())
        print(compute_reversibles(n))
