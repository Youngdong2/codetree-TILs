def season_of_date(Y, M, D):
    # 윤년 확인 함수
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    # 각 월의 마지막 날짜
    days_in_month = [31, 29 if is_leap_year(Y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 날짜 유효성 검사
    if M < 1 or M > 12 or D < 1 or D > days_in_month[M-1]:
        return -1

    # 계절 판별
    if 3 <= M <= 5:
        return "Spring"
    elif 6 <= M <= 8:
        return "Summer"
    elif 9 <= M <= 11:
        return "Fall"
    else:
        return "Winter"

Y, M, D = map(int, input().split())

print(season_of_date(Y, M, D))