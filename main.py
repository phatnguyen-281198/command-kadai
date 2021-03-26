import calc_bmi
h = float(input("身長："))
w = float(input("体重："))
print(calc_bmi.bmi(h,w))
print(calc_bmi.bmi(h,w))
if calc_bmi.bmi(h,w)<18.5:
    print("食生活")
elif calc_bmi.bmi(h,w)>30:
    print("運動不足")


