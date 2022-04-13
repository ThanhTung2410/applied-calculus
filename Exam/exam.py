# -*- coding: utf-8 -*-
"""52100943.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17p09TElAOwYKylr7vAo33Sf92ptBkn4Q
"""

from scipy import integrate
from sympy import * 
import numpy as np 
import math
from matplotlib import pyplot as plt

x = symbols('x')
y = symbols('y')
n = symbols('n')

# Câu 1

f = (3*x**3 - 5*x**2 + 7) / (x**2-4)
f_x = lambdify(x,f)
print("Câu 1")
list_x = (-3, -2, -1, 0, 1, 2, 3)
for x_root in list_x:
  try:
    result = f_x(x_root) 
    print(result)
  except ZeroDivisionError:
    result = None
    print(result)

print()

# Câu 2
f = lambda x: x**2 + 5
g = lambda x: 2*x**2 - 3*x + 4
print("Câu 2")
for x_root_f in (-3, -2,-1):
  print("f(g(x)) = {}.".format(f(g(x_root_f))))

for x_root_g in (0, 1, 2, 3):
  print("g(f(x)) = {}.".format(g(f(x_root_g))))

print()

# Câu 3
value = np.arange(-10, 10, 0.05)

f3 = -x**2 + 5*x + 4
g3 = 2 * x**2 + 2

x_root = solve(f3-g3,x)
y_root = f3.subs(x,x_root[0])

f3_x = lambdify(x, f3, "numpy")
g3_x = lambdify(x, g3, "numpy")

print("Câu 3")
plt.plot(value,f3_x(value),color='green')
plt.plot(value,g3_x(value),color='red')
plt.plot(x_root[0], y_root, 'ko')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(linestyle='-')
plt.show()

print()

# Câu 4
f4 = (1 - cos(x)**2) / (sin(x) - cos(x))
lim_f4 = limit(f4, x, math.pi / 2)
lim_right_f4 = limit(f4, x, math.pi / 2, '+')
lim_left_f4 = limit(f4, x, math.pi / 2, '-')
print("Câu 4")
print("Giới hạn của hàm số là {}".format(lim_f4))
print("Giới hạn bên phải của hàm số là {}".format(lim_right_f4))
print("Giới hạn bên trái của hàm số là {}".format(lim_left_f4))

print()

# Câu 5
f5 = (-2) * x**3 + 6 * x**2 + 3*x + 1
x0 = 2
y0 = 15
m = diff(f5,x,1).subs(x,x0) # Tính hệ số góc tại điểm x0
f5_tt = m*(x - x0) + y0 # PTTT y = m(x - x0) + y0
print("Câu 5) PTTT của f(x) = " + str(f5) + " tại điểm x0 = " + str(x0) + " là: ",f5_tt)

# Vẽ đồ thị hs f(x) và PTTT f(x) tại x0
list_x = np.arange(0, 5, 0.05)
f5_p = (-2) * list_x**3 + 6 * list_x**2 + 3*list_x + 1 # p = plot
f5_tt_p = m*(list_x - x0) + y0
plt.plot(list_x,f5_p)
plt.plot(list_x,f5_tt_p)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Câu 5")
plt.show()

print()

print("Câu 6")

# Câu 6
a = ((-1)**(n-1)) / (2**n - 8)
a_n = lambdify(n, a)
for k in (1,2,3,4,5):
  try: 
    result = a_n(k)
    print(result)
  except ZeroDivisionError:
    result = None
    print(result)

print()

# Câu 7
f7 = (2 * x**4 * y + 3 * x**2 * y**3 - 5 * x * y + 8) / (x**2 + 4*y)
df7 = diff(f7,x,2)
print("Câu 7)" + " Kết quả: " + format(df7))

print()

# Câu 8
f8 = 3*x**4 + 16*x**3 - 18*x**2 - 9
f8_x = lambdify(x,f8)
df8 = diff(f8,x,1)
criticalNums = solve(df8,x)
sec_df8 = diff(f8,x,2)
sec_df8_x = lambdify(x, sec_df8)
print("Câu 8")
for x_root in criticalNums:
  if(sec_df8_x(x_root) > 0):
    print("Giá trị cực tiểu = {} at x = {}".format(f8_x(x_root), x_root))
  elif(sec_df8_x(x_root) < 0):
    print("Giá trị cực đại = {} at x = {}".format(f8_x(x_root), x_root))

print()

# Câu 9
f9 = sin(x)**2 + sin(x) * cos(x)**2
val_Sf9 = integrate(f9,(x,-(math.pi / 2),math.pi / 2))
print("Câu 9)" + " Kết quả: " + format(val_Sf9))

print()

# Câu 10
f10 = x**3 * y + 2 * x**2 * y**2 - x * y**2
val_Sf10 = integrate(f10,(x,-1,1),(y,0,2))
print("Câu 10)" + " Kết quả: " + format(val_Sf10))