arr = []
for _ in range(2):
    arr.append(list(map(int, input().split())))

row1 = arr[0]
row2 = arr[1]
    
# 가로 평균 계산
row1_avg = sum(row1) / len(row1)
row2_avg = sum(row2) / len(row2)
print(f"{row1_avg:.1f} {row2_avg:.1f}")
    
# 세로 평균 계산
column_avgs = []
for i in range(len(row1)):
    column_avg = (row1[i] + row2[i]) / 2
    column_avgs.append(column_avg)
print(" ".join(f"{avg:.1f}" for avg in column_avgs))
    
# 전체 평균 계산
total_avg = (sum(row1) + sum(row2)) / (len(row1) + len(row2))
print(f"{total_avg:.1f}")