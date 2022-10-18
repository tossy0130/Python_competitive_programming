### ================================ 3の倍数のカウント

def Count_Of_Multiples_01(get_num):
    
    ### 値格納
    arr_01 = [int(i) for i in input().split()]
    
    ### 3の倍数カウント
    
    ans_num_01 = 0
    for val in arr_01:
        if val % 3 == 0 :
            ans_num_01 += 1
            
    print(ans_num_01)
    
### ============= Count_Of_Multiples_01 実行
get_num = int(input())

Count_Of_Multiples_01(get_num)


### ================================ 3の倍数のカウント END


### ================================ 7 があれば 
def Count_Of_Multiples_02(get_num_02):
    ### ========== 値取得
    arr_02 = []
    ans_02 = 0
    for i in range(get_num_02):
        arr_02.append(input())
        if '7' in arr_02:
            ans_02 += 1
            
    if ans_02 == 0:
        print("NO")
    else:
        print("YES")
        

### ========= Count_Of_Multiples_02 実行
get_num_02 = int(input())

Count_Of_Multiples_02(get_num_02)
### ================================ 7 があれば  END

### ================================ インデックス取得 
get_num_02 = int(input())

get_arr_02 = []
for i in range(get_num_02):
    get_arr_02.append(input())
    
get_num_002 = input()

ans_num_02 = []
for j in range(get_num_02):
    if get_arr_02[j] == get_num_002:
        ans_num_02.append(str(j + 1))

for val in ans_num_02 :
    print(val)
### ================================ インデックス取得  END

