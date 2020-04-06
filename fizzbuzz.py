class fizzbuzz:


    def fizz_buzz(number):
        my_fizz_buzz_list = []
        for i in range(number):

            if i % 3 == 0:
                my_fizz_buzz_list.append("fizz")

            elif i % 5 == 0:
                my_fizz_buzz_list.append("buzz")

            elif i % 3 == 0 and i % 5 == 0:
                my_fizz_buzz_list.append("fizzbuzz")

            elif i % 3 != 0 and i % 5 != 0:
                my_fizz_buzz_list.append(str(i))

                for x in my_fizz_buzz_list:
                    print(x)

    fizz_buzz(3)

class Solution(object):
   def fizzBuzz(self, n):
         """
      :type n: int
      :rtype: List[str]
      """
      result = []
      for i in range(1,n+1):
         if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
         elif i %3==0:
            result.append("Fizz")
         elif i% 5 == 0:
            result.append("Buzz")
         else:
            result.append(str(i))
      return result
