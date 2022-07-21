print('__________________')
print('Escape sequences') 
print('------------------\n')

weather = '1. it\'s \"kind of\" sunny'
# back slash give command to the programe to recognise any letter come after that is a SyntaxWarning
print (weather)
print ('2. \t tab')
print ('3. start \n line break \n')

print('__________________')
print('Formatted String')  
print('------------------\n')

name = 'Gihan'
age = '55'

print (f'1. Hi {name}. you are {age} years old ')
print ('2. Hi {}. you are {} years old '.format(name , age))
print ('3. Hi {1}. you are {0} years old '.format(name , age))

print('__________________')
print('String Index or lising')  
print('------------------\n')

index = '123456789'
        #012345678
print ('*[start:stop]\n') 
print ('index 2-5 ~ '+ index[2:5])
print ('index 0-all the way to end ~ '+ index[0:])
print ('index start from 0 to index 5 ~ '+ index[:5])

print ('\n*[start:stop:stepover]\n')
print ('index 0 - 9 with default stepover which is 1 ~ '+ index[0:9])#defult is 1
print ('index 0 - 9 with stepover 2 ~ ' + index[0:9:2])
print ('revers the order with stepover -1 ~ ' + index[::-1])# (-) reverse the order 

print('__________________')
print('String Immutability')  
print('------------------\n')

print('we can\'t reassing part of the string (index[0]=3) but we can reassing all to another value(index=\'9876543\') \n ex:')
index = '9876543'
print(index)

print('_____________________________')
print('Built in Functions + Methods')  
print('-----------------------------\n')

greet = 'heyyyyyy'
name = 'gihan'

print(greet[0:len(greet)]) #because lenth of the string is there
#method own by some thing (ex:string , numbers...etc) it start with (.)(ex:.format)
print('{} {} How are you' .format(greet,name))

quote = 'to be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
print(quote.replace('be', 'me'))

