class fizzbuzz:

    def fizz_buzz_checker(self):
        my_fizz_buzz_list = []
        number = int(input('Enter a number please'))

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

fizzer = fizzbuzz()

fizzer()

