# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    # pattern of each students
    a_ans = [[1,2,3,4,5][i%5] for i in range(len(answers))]
    b_ans = [[2,1,2,3,2,4,2,5][j%8] for j in range(len(answers))]
    c_ans = [[3,3,1,1,2,2,4,4,5,5][k%10] for k in range(len(answers))]
    
    # to check their answers
    print('a_ans is ', a_ans)
    print('b_ans is ', b_ans)
    print('c_ans is ', c_ans)
    
    # comparing to origin answers and then scoring
    a_score = 0
    b_score = 0
    c_score = 0
    
    for a_, ans_ in zip(a_ans, answers):
        if a_ == ans_:
            a_score += 1
    for b_, ans_ in zip(b_ans, answers):
        if b_ == ans_:
            b_score += 1
    for c_, ans_ in zip(c_ans, answers):
        if c_ == ans_:
            c_score += 1
    
    # add students who get max score to the list
    score_list = [a_score, b_score, c_score]
    print(score_list)
    max_score = max(score_list)
    answer = sorted([i for i in range(1,4) if score_list[i-1] == max_score])
    return answer


solution([1,2,3,4,5])
