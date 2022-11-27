def factorial(n):
    f = 1
    if n==0:
        1
    else:
        for i in range(1,n+1):
            f*=i
    return f
def J(alpha,x):
    s = 0
    sum = 0
    coef = 1
    while(1.0e-8 <= coef):
        coef = pow(x/2, (2*s+alpha))/(factorial(s)*factorial(s+alpha))
        sum += pow(-1, s)*coef
        s += 1
    return sum
