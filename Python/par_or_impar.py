num = [1,2,3,4,5,6,7,8,9]

def is_par(num):
    if(num%2==0):
        return True
    
#numbers_par = filter(is_par,num)

numbers_par = filter(lambda num: num%2==0,num)

print(list(numbers_par))
    