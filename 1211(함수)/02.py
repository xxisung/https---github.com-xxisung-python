def func(x):
    y = x * 2 + 1
    return y
result = func(2)
print("첫 번째:" ,result)
result = func(3)
print("두 번째:",result)

def avg(a,b):
    result=(a+b)/2
    return result
print("평균1:",avg(20,30))
print("평균2:",avg(3,17))
print("평균3:",avg(4,7))

def mul(a,b):
    result = a*b
    return result
print("곱셈1 : ",mul(5,5))
print("곱셈2 : ",mul(3,9))
print("곱셈3 : ",mul(2,7))

#def 함수명(매개변수):
    #수행할 문장1
    # ...
    #return 반환값
#print(함수호출(인자값))
#변수 = 함수호출(인자값)