import Constants


def fizzBuzz(input_num):
    if input_num % 3 == 0 and input_num % 5 == 0:
        return Constants.FIZZBUZZ
    elif (input_num % 3) == 0:
        return Constants.FIZZ
    elif (input_num % 5) == 0:
        return Constants.BUZZ
    else:
        return input_num

