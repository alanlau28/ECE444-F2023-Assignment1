class Utils:

    def reversed (number):
        number = int(number)
        newNum = 0
        while number > 0:
            newNum = newNum * 10 + number % 10
            number = number // 10
        return newNum

    def formatter (number):
        number = int(number)
        return bin(number),oct(number)
