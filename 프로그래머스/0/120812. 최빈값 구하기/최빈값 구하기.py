def solution(array):
    cnt = {}
    answer = []
    res = 0
    arr_to_set = set(array)
    if(len(arr_to_set) == 1):
        res = array[0]
    else:
        for i in array:
          try: 
            cnt[i] += 1
          except: 
            cnt[i] = 1
        answer = list(cnt.values())
        max_n = max(answer)

        answer.remove(max(answer))

        for j in answer:
          if len(cnt) != 1 and max_n == j:
            res = -1
            break
          else:
            for key, value in cnt.items():
              if value == max_n:
                res = key

    return res

    
            