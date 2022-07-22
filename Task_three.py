#Given Dictionary:
chest = {
            '42': 'It is the Answer to Life the Universe and Everything.',
            '666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
            '8': 'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence.',
            '13': 'The Truth is in the Heart.',
            '0': 'Freedom is secured not by the fulfilling of ones desires, but by the removal of desire.',
            '9': 'The unexamined life is not worth living.',
            '76': 'Life is a series of natural and spontaneous changes.',
            '70': 'God is dead! He remains dead! And we have killed him.'
            }
print(chest.keys())
print(chest.values())

# Sort the dictionary by its keys
print(sorted(chest.items()))

#Get the values of first, second, last and second last keys.
frist=list(chest.values())[0]
print(frist)
second=list(chest.values())[1]
print(second)
last=list(chest.values())[-1]
print(last)
second_last=list(chest.values())[-2]
print(second_last)

# Concatenate the values of obtained keys in a string.
result = ' '.join( y for x, y in chest.items())
print(result)

# Get first and last characters of each word in concatenated string, no spaces in between.
print(result[0] + result[-1])

#Get the number of occurrences of each letter in the resulting string and get top 5 letters without using any python package. The uppercase character should be counted in the lower case. Eg: ‘A’ character should result in an increment of key ‘a.’.
res_lowercase=result.lower()
print(res_lowercase)

all_freq = {}

for i in res_lowercase:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print ("Count of all characters is :\n " +  str(all_freq))
print(all_freq.values())

#On the chest infront of you, there is a list of numbers
print(chest.keys())

#. Sum the number_of_occurrences of the resulting dictionary with values of the key_list you found in the chest.
print(sum(all_freq.values()))

# then, get the ascii character
asciiDict = {i: chr(i) for i in range(128)}
ascii_dict = dict()
ascii_in_number = range(0,256)
for i in ascii_in_number:
    ascii_dict[str(i)] = chr(i)
print(ascii_dict)