
### ============================ 単純な入出力
def Print_Line_01(str): {
    print(str)
}

#=== Print_Line_01 実行
input = input()
Print_Line_01(input)
#=== Print_Line_01 実行　END

### ============================ 単純な入出力 END

### ============================ 複数行にわたる出力
def Print_Line_02(p, num):
    i = 0
    while (i < num):
        print(p)
        i = i + 1
        
input = int(input())

Print_Line_02("paiza", input)
### ============================ 複数行にわたる出力 END