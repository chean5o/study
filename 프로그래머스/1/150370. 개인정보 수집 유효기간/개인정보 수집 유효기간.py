def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:])

    for i in range(0, len(privacies)):
        privacy_date = privacies[i][:10]
        privacy_term = privacies[i][11:]

        privacy_year = int(privacy_date[:4])
        privacy_month = int(privacy_date[5:7])
        privacy_day = int(privacy_date[8:10])

        # 해당 개인정보의 만료 기간 찾기
        for term in terms:
            if privacy_term == term[:1]:
                term_months = int(term[2:])

                # 만료일 계산
                expire_year = privacy_year
                expire_month = privacy_month + term_months
                expire_day = privacy_day

                if expire_month > 12:
                    expire_year += expire_month // 12
                    expire_month = expire_month % 12
                    if expire_month == 0:
                        expire_month = 12
                        expire_year -= 1

                # 만료일과 현재 날짜 비교
                if (expire_year < today_year or
                    (expire_year == today_year and expire_month < today_month) or
                    (expire_year == today_year and expire_month == today_month and expire_day <= today_day)):
                    answer.append(i + 1)  # 인덱스를 1부터 시작하도록 수정
                break
    return answer