hight1=(input("请输入你的身高（m）："))
weight1=(input("请输入你的体重（kg）："))
sex1=input("请输入你的性别(男=1，女=0)：")
age1=input("请输入你的年龄：")
hight=float(hight1)
weight=float(weight1)
sex=float(sex1)
age=float(age1)
bmi=weight/(hight*hight)
tizhilv=bmi*1.2+0.23*age-5.4-10.8*sex
minimun=0.15+0.10*(1-sex)
maximun=0.18+0.10*(1-sex)
result=minimun<tizhilv<maximun
print("你的体脂率是否符合标准：",result)
print("你的体脂率为：",tizhilv)

