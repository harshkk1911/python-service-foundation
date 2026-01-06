def sum_of_2_numbers(num1,num2):
  print('SUM OF ',num1,' and ',num2,' is ',num1+num2)

def main():
  try:
    num1=int(input('Enter number 1:'))
    num2=int(input('Enter number 2:'))
    sum_of_2_numbers(num1,num2)
  except ValueError:
    print('INVALID INPUT')

if __name__=="__main__":
  main()
