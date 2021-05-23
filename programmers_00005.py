# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    
    uid_list = [i.split(" ")[1] for i in record]
    uid_set = set(uid_list)
    uid_dict = {}

    for i in range(len(record)):
        try:
            uid_dict[uid_list[i]] = record[i].split(" ")[2]
        except IndexError as e:
            continue
    result = []
    
    for i in range(len(record)):
        if (record[i][0] == 'E') :
            result.append(uid_dict.get(uid_list[i])+"님이 들어왔습니다.")
        elif (record[i][0] == 'L') :
            result.append(uid_dict.get(uid_list[i])+"님이 나갔습니다.")
        
 
    answer = result
    
    return answer
        