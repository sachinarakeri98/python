#dictionary
#x = {'val1':2,'val2':'3','val3':5}
#y = x['val2']
#print(y)
######################################
#my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
#listVar = my_dict['key3'][1].split()
#print(listVar)
#my_dict['key4']=300
#print(my_dict)
# Dictionary nested inside a dictionary nested inside a dictionary
#d = {'key1':{'nestkey':{'subnestkey':'value'}}}
#print(d)
#m = d['key1']['nestkey']
#print(m)
#######################
#from random import randint
import math


#x= 18
#y=18
#if y>x:
#    print('eligible For Voting')
#elif y==x:
#    print('First time Voter')
#else:
#    print('not eligible for Voting')
################
#y = [x for x in range(1,41) if x%2 == 0]
#print(y)
##############
#x = 'Print every word in this sentence that has an even number of letters'
#for y in x.split():
#    if len(y)%2 == 0:
#        print(y+" <-- has an even length!")
##################################
#for num in range(1,101):
#    if num%3 == 0 and num%5==0:
#        print('Fizz Buzz!')
#    elif (num)%3 ==0 :
#        print('fizz')
#    elif (num)%5 ==0:
#        print('Buzz')
#    else:
#        print('NUM')
#############################
#st = 'Create a list of the first letters of every word in this string'
#x = [word[0] for word in st.split()]
#print(x)
############################
#x=[1,2,3,4,5]
#x.reverse()
#print(x)
#############################
#def project_function(Name):
#    print(f'Hello\n{Name}')
#project_function('Ujjuuuu')
###########################
#def add_num(num1,num2):
#    return num1+num2
#result= add_num(33,33)
#print(result)
###########################
# x = [1,2,3,4,5,6,7,8,9,0]
# from random import shuffle
# #######################
# mylist = ['','0','']
# def shuffle_list(mylist):
#     # Take in list, and returned shuffle versioned
#     shuffle(mylist)
#
#     return mylist
# def player_guess():
#     guess = ''
#
#     while guess not in ['0', '1', '2']:
#         Recall input() returns a string
        # guess = input("Pick a number: 0, 1, or 2:  ")

#    return int(guess)

#def check_guess(mylist,guess):
#    if mylist[guess] == 'O':
#        print('Correct Guess!')
#    else:
#        print('Wrong! Better luck next time')
 #       print(mylist)
# ###############################################3
# mylist = ['','0','']
# mixup_list = shuffle(mylist)
# guess = player_guess()
# x = check_guess(mylist,guess)
# print(x)
# #####################################
# def xyz_a(name):
#     print('Hello'+name)
# x = [1,2,3,4,5,6,7,8,9]
# ##################
# x = xyz_a('ujju')
# ###### printing Prime Number -----------
# def count_primes(num):
#     primes = [2]
#     x = 3
#     if num < 2:  # for the case of num = 0 or 1
#         return 0
#     while x <= num:
#         for y in range(3, x, 2):  # test all odd factors up to x-1
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)
#     return len(primes)
# #######################
# count_primes(20)

# def print_big(letter):
#     patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
#     alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
#     for pattern in alphabet[letter.upper()]:
#         print(patterns[pattern])
#
# print_big('d')
#####################
# def square(num):
#     return num ** 2
# y = [1,2,3,4,5,6,7,8,9,10]
# for x in map(square,y):
#     print(x)
############
x = "ujju"

print(y)






