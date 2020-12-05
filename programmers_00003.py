# https://programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s)%2 == 1 :
        answer = s[len(s)//2]
    else :
        answer = s[len(s)//2-1:len(s)//2+1]
    return answer

solution("abcde")

# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution2(arr):
    answer = [arr[0]]
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution3(a, b):
    nums = abs(a - b) + 1
    answer = (a+b) * nums / 2
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/62048

import math
def solution4(w,h):
    wh_gcd = math.gcd(w,h)
    x_mark, y_mark = (w/wh_gcd, h/wh_gcd)
    return w*h - int((x_mark + y_mark - 1) * (w/x_mark))