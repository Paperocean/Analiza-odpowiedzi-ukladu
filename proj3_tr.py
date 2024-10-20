import numpy as np
import matplotlib.pyplot as plt

def def_response():
    # Analitycznie
    y1 = np.zeros(N)
    for n in range(N):
        if n == 0:
            y1[n] = 0
        else:
            y1[n] = (5/13)*((1/2)**(n-1)) + (-272/65)*((-4/5)**(n-1)) + 6*delta[n]

    # Symulacja 
    y2 = np.zeros(N)
    for n in range(N):
        if n == 0:
            y2[n] = a*(d)**n
        else:
            y2[n] = a*(d)**n + b*(d)**(n-1) - c*y2[n-1]
            
    plt.figure(1)
    plt.title("Odpowiedź na pobudzenie u[n]=(1/2)**n")
    plt.scatter(t, y1, label="Analitycznie", marker='o', s=10)
    plt.scatter(t, y2, label="Symulacyjnie", marker='o', s=10)
    plt.grid()
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('y')
    plt.show()

def imp_response():
    # Analitycznie
    y3 = np.zeros(N)
    for n in range(N):
        if n == 0:
            y3[n] = 0
        else:
            y3[n] = (-34/5)*((-4/5)**(n-1)) + 6*delta[n]

    # Symulacyjnie
    y4 = np.zeros(N)
    for n in range(N):
        if n == 0:
            y4[n] = a*delta[n]
        else:
            y4[n] = a*delta[n] + b*delta[n-1] - c*y4[n-1]
            
    plt.figure(2)
    plt.title("Odpowiedź impulsowa")
    plt.scatter(t, y3, label="OI Analitycznie", marker='o', s=10)
    plt.scatter(t, y4, label="OI Symulacyjnie", marker='o', s=10)
    plt.grid()
    plt.legend()
    plt.xlabel('t')
    plt.ylabel('y')
    plt.show() 

def step_response():
    # Analitycznie
    for i in range(len(y_minus_1)):
        plt.figure(f"For y[-1] = {y_minus_1[i]}")
        plt.title(f"Odpowiedź skokowa dla y[-1]={y_minus_1[i]}")
        y5 = np.zeros(N)
        for n in range(N):
            if n == 0:
                y5[n] = y_minus_1[i]
            else:
                y5[n] = 20/(9*(y_minus_1[i] + 1)) + ( 16/9 - (24/5)*( y_minus_1[i] + 1 ) )*(( (-4/5) * (y_minus_1[i] + 1) )**(n-1)) + 6*delta[n]
                # y5[n] = (100/45) + (-136/45)*((-4/5)**(n-1)) + 6*delta[n]
        
        plt.scatter(t, y5, label=f"OS Analitycznie{y_minus_1[i]}", marker='o', s=10)
        
        # Symulacyjnie
        y6 = np.zeros(N)
        u = np.ones(N)
        for n in range(N):
            if n == 0:
                y6[n] = a * u[n] + b * u[n-1] - c * y_minus_1[i]
            else:
                y6[n] = a * u[n] + b * u[n-1] - c * y6[n-1]
        plt.scatter(t, y6, label=f"OS Symulacyjnie{y_minus_1[i]}", marker='o', s=10)
        plt.grid()
        plt.legend()
        plt.xlabel('t')
        plt.ylabel('y')
        plt.show()


# Parametry
N = 100
t = np.arange(N)

delta = np.zeros(N)
delta[0] = 1

a = 6
b = -2
c = 4/5
d = 1/2

y_minus_1 = [0, 1]

# Odpowiedz na pobudzenie
# def_response()

# Odpowiedz impulsowa
# imp_response()

# Odpowiedz skokowa
step_response()
    
        
