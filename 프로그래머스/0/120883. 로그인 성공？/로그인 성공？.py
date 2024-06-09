def solution(id_pw, db):
    answer = ''
    for i in range(0, len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                print("login",db[i])
                answer = 'login'
            else:
                print("wrong",db[i])
                answer ='wrong pw'
                break
        else:
            print(db[i])
            answer = 'fail'
                
    return answer