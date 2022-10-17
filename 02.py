############ 文字列 ##############

### ============================ 整数と文字列

####### 文字列の長さを出力
def Integers_And_Strings_01(num):
    
    arr = []
    ### 値取得
    for i in range(num):
        arr.append(input())
    
    ### === 文字列の長さを出力 === 
    for val in arr:
        print(len(val))
        
###========= Integers_And_Strings_01　実行
get_num = int(input())
Integers_And_Strings_01(get_num)
    
### ============================ 整数と文字列 END

### ============================ 部分文字列

### ========= 文字列が含まれているか
def Integers_And_Strings_02(a_str, t_str):
    if a_str in t_str:
        print("YES")
    else:
        print("NO")
        
get_str_02 = input()
get_str_002 = input()

Integers_And_Strings_02(get_str_02, get_str_002)

### ============================ 部分文字列 END

### ============================ 数字の文字列操作

def Integers_And_Strings_03(get_list_03 = []):
    
    a_03 = int(get_list_03[0]) + int(get_list_03[3])
    b_03 = int(get_list_03[1]) + int(get_list_03[2])
    
    print(str(a_03) + str(b_03))
    
### =======　Integers_And_Strings_03　実行

### 1文字ずつ取得
get_list_03 = list(input())

Integers_And_Strings_03(get_list_03)

### ============================ 数字の文字列操作 END

### ============================ 数字の文字列操作（0埋め）

def Integers_And_Strings_04(get_str_04) :
    
    str_num_04 = len(get_str_04)

    if str_num_04 == 1:
        print("00" + str(get_str_04))
    elif str_num_04 == 2:
        print("0" + str(get_str_04))
    else :
        print(str(get_str_04))    
        
### =========== Integers_And_Strings_04 実行

get_str_004 = input()
Integers_And_Strings_04(get_str_004)

### ============================ 数字の文字列操作（0埋め） END


