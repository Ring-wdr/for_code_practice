# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    weekday = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    week = sum(days[:a-1]) + b
    
    answer = weekday[(week+4)%7]
    return answer

solution(5,24)


# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution2(numbers):
    number_len = len(numbers)
    list1 = []
    for i in range(number_len-1):
        list2 = [numbers[i] + j for j in set(numbers[i+1:])]
        list1.extend(list2)
        
    answer = set(list1)
    return sorted(list(answer))

solution2([2,1,3,4,1])



# bonus
a = [[1,2,3],['가','나','다'],[11,22,33],['가가','나나','다다']]

[[i,j,k,l] for i,j,k,l in zip(a[0],a[1],a[2],a[3])]




