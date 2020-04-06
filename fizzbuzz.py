Class fizzbuzz:

  def fizz_buzz(number):
    my_fizz_buzz_list = []
    for i in range(number):

      if i % 3 == 0:
        my_fizz_buzz_list.append("fizz")

      elif i % 5 == 0:
        my_fizz_buzz_list.append("buzz")

      elif i % 3 == 0 and i % 5 == 0:
        my_fizz_buzz_list.append("fizzbuzz")

     else:
      my_fizz_buzz_list.append(i)

      for x in my_fizz_buzz_list:
        print(x)
