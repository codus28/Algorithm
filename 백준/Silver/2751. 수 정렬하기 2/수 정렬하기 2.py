
import sys # 시간 최적화

n = int(input())
nums = [int(sys.stdin.readline()) for i in range(n)]

nums.sort() # Tim sort

sys.stdout.write('\n'.join(map(str,nums)))

'''
1. sys.stdin.readline()은 훨씬 가볍고 빠름
개행 문자(\n)가 그대로 포함됨 → 직접 처리 필요 -> 여기서는 int()로 감싸주면서 '1\n' 이었던 애들이 '1'로 바뀜. 

2. sys.stdout.write()는 문자열만 출력합니다.
하지만 속도는 매우 빠르기 때문에, 반복 입력을 받을 때 유리합니다.
oin() 함수는 문자열을 연결할 때 아주 자주 쓰이는 파이썬의 문자열 메서드입니다. 특히 리스트나 튜플에 있는 문자열들을 하나의 문자열로 합칠 때 유용합니다.

3. join 문법 : '구분자'.join(문자열_리스트)
'''