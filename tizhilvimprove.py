#输入数据
hight1=(input("请输入你的身高（m）："))
weight1=(input("请输入你的体重（kg）："))
sex1=input("请输入你的性别(男=1，女=0)：")
age1=input("请输入你的年龄：")
hight=float(hight1)
weight=float(weight1)
sex=float(sex1)
age=float(age1)
if not (0 < hight < 300 and 0 < weight < 500 and 0 < age < 200 and (sex == 1 or sex == 0)):
    print("你的数据不符合标准，程序退出")
    exit()

bmi=weight/(hight*hight)
tizhilv=bmi*1.2+0.23*age-5.4-10.8*sex
tizhilv/=100
if sex==1:
    result=0.15<tizhilv<0.18
    minimum=0.15
    maximun=0.18
elif sex==0:
    result=0.25<tizhilv<0.28
    minimum=0.25
    maximun=0.28


if sex==1:
    hao="先生您好："
elif sex==0:
    hao="女士您好："


if result:
    notice="身体不错"
else:
    if tizhilv<minimum:
        notice="你不健康呀,小瘦瘦"
    else:
        notice="你不健康呀,小胖胖"
print("你的体脂率为：",tizhilv)
print(hao,notice)

