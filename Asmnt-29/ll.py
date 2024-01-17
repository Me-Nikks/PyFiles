# nums = [1, 2, 3, 4, 5]
 
# for num in nums:
#   print(num )


# teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
# for team in teams:
#   for name in team:
#     print(name)

# i = 0
# while i == i:
#   print(i)
#   i +=1

# names = ['joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
# for name in names:
#    if 'J' in name.upper():
#        pass
#    else:
#        print(name)

# names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
# for name in names:
#   if 'h' in name.lower():
#       break
#   else:
#       print(name)


# names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']
 
# for name in names:
#   if 'm' in name.lower():
#       continue
#   else:
#       print(name)

# nums = [0, 1, 2, 3]
 
# try:
#    print(sum(nums))
 
# except:
#    print('Cannot print the sum! Your variables are not numbers.')


# nums = ['x', 'y', 'z']
 
# try:
#    print(sum(nums))
 
# except:
#    print('Cannot print the sum! Your variables are not numbers.')

# nums = ['x', 'y', 'z']
 
# try:
#    print(sum(nums))
 
# except:
#    print('Cannot print the sum! Your variables are not numbers.')
 
# finally:
#    print('Hope you got the result you want!')


# nums = [5, 2, 3, 10]
 
# try:
#    avg = sum(nums) / len(nums)
#    print('The average of the list is: ', avg)
 
# except:
#    print('Cannot compute average - make sure you enter a list of integers!')
 
# finally:
#    print('Feel free to rerun the code with another list of integers!')


# def greetings(language):
#    if language == 'Spanish':
#        greeting = 'Hola'
 
#    elif language == 'English':
#        greeting = 'Hello'
 
#    elif language == 'French':
#        greeting = 'Bonjour'
 
#    print(greeting)
# greetings('French')
# # print(hi)

def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
 
factorial(5)