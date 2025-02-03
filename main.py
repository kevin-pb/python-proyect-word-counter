import collections

data_enter = input("Introduce a phrase: ").lower()

def count_words(counting):
    counting = collections.Counter(data_enter.split(" "))
    return counting

try:
    print(count_words(data_enter))

except ValueError:
    print("You have not entered a correct value")
    data_enter = input("Introduce a phrase: ").lower()
    print(count_words(data_enter))