import random


class FreqencyDistribution:

#     @staticmethod
#     def calculate_frequencies(self):
#         pass
#     def display_frequency_table(self):
#         pass
#
#     @staticmethod
#     def get_most_frequent(self):
#         pass
#
# mylist = [random.randint(-5 , 5) for in range(10)]
# FreqencyDistribution.calculate_frequencies(mylist)

# 2

@staticmethod
def calculate_frequencies(self, mylist):
    mydict = {1 : 0 for i in set (mylist)}
    print("Вывод до подсчета: {mydict}")
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            if mylist[1] == mylist[j]:
                mydict[1] += 1
    print(f"После подсчета: {mydict}")
@staticmethod
def display_frequency_table(self, mydict):
    print("*" * 17)
    self.get_most_frequest(mydict)
    @staticmethod
    def get_most_frequent(self, mydict):
        max = -10
        for i in mydict.values():
            if i > max:
                max = i
        print(f"Наибольшее число вхождений по таблице : {max}")

mylist = [random.randint(-5, 5) for i in range(10)]
FreqencyDistribution.calculate_frequencies(mylist)



