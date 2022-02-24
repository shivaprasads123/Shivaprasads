
from itertools import combinations

class StringClass:
    def __init__(self, str_name):
        self.string_test = str(str_name)

    def string_length(self):
        return len(self.string_test)

    def string_convert(self):
        return list(self.string_test)

def main():
    obj_string = StringClass('1222339')
    print("length of the string is: " + str(obj_string.string_length()))
    print("List of characters in the string is:" + str(obj_string.string_convert()))

if __name__ == '__main__':
    main()



