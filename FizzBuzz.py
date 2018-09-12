for i in range(100):
 j=i+1
 if (0==j%15):
  print('FizzBuzz')
 elif (j%3==0):
  print('Fizz')
 elif (0==j%5):
  print('Buzz')
 else:
  print(j)
