#deve ser rodado em python 3.10 ou superior
import math

def trapezio(a , b, n):
   if n < 0 or n % 2 != 0:
      raise ValueError("ERROR")
   h = (b - a) / n
   soma = 0
   for k in range(1,n):
      soma += f(a + k * h)
   soma *= 2
   soma += (f(a)+ f(b))
   return (h/2)*soma

def simpson(a,b,n):
   if n < 0 or n % 2 != 0:
      raise ValueError("ERROR")
   h=(b-a)/n
   soma_odd, soma_even = 0 ,0
   for k in range(1,n,2):
      soma_odd += f(a + k * h)
   for k in range(2, n, 2):
      soma_even += f(a + k * h)
   return (h/3) * (f(a) + 4 * soma_odd + 2*soma_even + f(b))

def Euler(x0,y0, h, n):
   for k in range(n):
      y0 += h * g(x0, y0)
      x0 += h
      print("x", k+1,"=",x0," y",k+1,"=",y0)

def g(x,y):
   return x + y

def f(x):
   return math.exp(-x ** 2)

print("""Escolha:
     [1]. Integral utilizando trapezio
     [2]. Integral utilizando simpson
     [3]. EDO com metodo de Euler
     """)
escolha = int(input())
match escolha:
case(1):
   print("digite o primeiro valor do intervalo: ")
   a= float(input())
   print("digite o segundo valor do intervalo: ")
   b= float(input())
   print("digite o número de pontos do intervalo: ")
   n = int(input())

   print("Resultado: ", trapezio(a,b,n))
case(2):

   print("digite o primeiro valor do intervalo: ")
   a = float(input())
   print("digite o segundo valor do intervalo: ")
   b = float(input())
   print("digite o número de pontos do intervalo: ")
   n = int(input())
   print("Resultado ", simpson(a,b,n))
case(3):
   print("y0: ")
   y0 = float(input())
   print("h: ")
   h = float(input())
   print("n: ")
   n = int(input())
Euler(0,y0,h,n)
