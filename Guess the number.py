#这类型的代码多次输入在jupyter不好使
import random
num = random.randint(1, 500)
count = 0
while True:
    count += 1
    result = input("Enter a number ")
    result = int(result)
    if result == num:
        print("！The number is %d ,you guess %d times"%(result, count))
        exit()
    else:
        if result < num:
            print("too small")
        elif result > num:
            print("too big")
