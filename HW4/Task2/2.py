# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N


def Simple (list_nums):
    s=[2]
    for i in list_nums:
        k=0
        q=int(list_nums[len(list_nums)-1]**0.5)
        for j in s:
            if j>q:
                break
            if i%j==0:
                k=1
                break
        if k==0:
            s.append(i)
    return s


def Decompose(num):
    nums = [i for i in range (3,num+1,2)]
    simple_nums = Simple(nums)
    result=[]
    i=0
    while num>1:
        while num%simple_nums[i]==0:
            result.append(simple_nums[i])
            num/=simple_nums[i]
        i+=1
    return result


number = int(input('Введите число: '))
simps = Decompose(number)
print (number,'->',simps)