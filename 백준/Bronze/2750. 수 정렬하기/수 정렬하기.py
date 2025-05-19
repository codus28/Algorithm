

'''
Stable sort & O(nlogn)
'''
def merge_sort (arr):

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    L_arr = merge_sort(arr[:mid]) # 재귀는 값을 바로 계산하지 말고
                                  # 형태로 가져가며 이해
    R_arr = merge_sort(arr[mid:])

    merge = []
    l = r = 0
    while l < len(L_arr) and r < len(R_arr):
        if L_arr[l] < R_arr[r] :
            merge.append(L_arr[l])
            l += 1

        else:
            merge.append(R_arr[r])
            r += 1
    merge += L_arr[l:]
    merge += R_arr[r:]

    return merge

n = int(input())

test = [int(input()) for j in range(n)]

ans = merge_sort(test)

for i in range(len(ans)):
    print(ans[i])