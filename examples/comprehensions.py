print([[None for j in range(2)] for i in range(3)])

# 중첩 컴프리헨션 예시
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(pairs) # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

# matrix를 리스트 하나로 펴기
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [col for row in matrix for col in row] # 왼쪽에서 오른쪽 순으로 실행
print(flat)

# 3중첩 컴프리헨션 - 굳이 이렇게까지?
my_lists = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
flat = [aa for sublist1 in my_lists 
                for sublist2 in sublist1 
                    for aa in sublist2]
# flat = []
# for sublist1 in my_lists:
# 	for sublist2 in sublist1:
# 		flat.extend(sublist2)
print(flat)


# 경고: 아래 코드는 이해하기 매우 어려우며, 유지보수가 힘든 안티 패턴 예시임.
cursed_apple = {f"key_{i}": ([[[x if x % 2 == 0 else -x for x in range(j, j + 3)] for j in range(k, k + 2)] for k in range(i, i + 3)] if i % 2 == 0 else {f"subkey_{k}": {f"inner_{n}": n if n % 3 == 0 else n * 2 for n in range(k, k + 3)} for k in range(i, i + 3)}) for i in range(1, 4)}

bad_apple = {
    f"key_{i}": (
        [  # 첫 번째 분기: i가 짝수일 때 (리스트 컴프리헨션 - 3중 중첩)
            [  # 2중 nested comprehension: k 레벨
                [  # 3중 nested comprehension: j 레벨
                    x if x % 2 == 0 else -x  # 조건부 표현식
                    for x in range(j, j + 3)
                ]
                for j in range(k, k + 2)
            ]
            for k in range(i, i + 3)
        ] if i % 2 == 0 else
        {  # 두 번째 분기: i가 홀수일 때 (딕셔너리 컴프리헨션 내부에 중첩 dictionary comprehension)
            f"subkey_{k}": {
                f"inner_{n}": n if n % 3 == 0 else n * 2  # 조건부 표현식
                for n in range(k, k + 3)
            }
            for k in range(i, i + 3)
        }
    )
    for i in range(1, 4)
}


import pprint
pprint.pprint(cursed_apple)
