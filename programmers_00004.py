# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for start, end, position in commands:
        answer.append(sorted(array[start-1:end])[position-1])
    return answer

