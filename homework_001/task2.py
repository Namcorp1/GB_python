# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# (расшифровка этого выражения not (x[0] or x[1] or x[2]) = not x[0] and not x[1] and not x[2])
# для всех значений предикат.
check1 = True
check2 = True
check3 = True
checking = [True,True,True,True,True,False,True,False,True,False,True,True,
            True,False,False,False,True,False,False,False,True,False,False,False]
leftCheck = not(check1 or check2 or check3)
rightCheck = not check1 and not check2 and not check3
for i in range(0,8):
    check1 = checking[i*3]
    check2 = checking[i*3+1]
    check3 = checking[i*3+2]
    if leftCheck == rightCheck:
        print(f"Предикаты {i+1} прошли проверку!")
    else:
        print(f"Предикаты {i+1} не прошли проверку!")


