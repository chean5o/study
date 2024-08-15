def count_blurays(lectures, size):
    count = 1  # 블루레이 개수
    current_sum = 0  # 현재 블루레이에 녹화된 강의 시간 합

    for i in lectures:
        if current_sum + i > size:
            # 현재 블루레이에 더 이상 강의를 넣을 수 없으므로 새로운 블루레이 사용
            count += 1
            current_sum = i
        else:
            # 현재 블루레이에 강의를 추가
            current_sum += i

    return count

def binary_search(n, m, lectures):
    start = max(lectures)
    end = sum(lectures)
    result = end

    while start <= end:
        mid = (start + end) // 2
        required_blurays = count_blurays(lectures, mid)

        if required_blurays <= m:
            result = mid  # 가능한 최소 크기를 찾은 경우
            end = mid - 1
        else:
            start = mid + 1

    return result

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# 결과 출력
print(binary_search(n, m, lectures))