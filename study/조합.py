# 전체 배열에서 컬럼별로 combination을 해야하는 문제에서
배열 = [["홍길동", "A", "201928"],
      ["김철수", "AB", "281839"],
      ["김영희", "B", "321002"]]
comb = (1, 2)

# 배열에서 comb의 요소만 가져와서 list를 만들 때
# 아래처럼 tuple을 선언하면 쉬움
for item in 배열:
    print(tuple(item[key] for key in comb))

# 최종
tmp = [tuple(item[key] for key in comb) for item in 배열]
print(tmp)