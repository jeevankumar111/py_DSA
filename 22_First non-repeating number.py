def firstNonRepeatingg(string):
    freq = {}
    for x in string:
        freq[x] = freq.get(x,0) +1

    for i in string:
        if freq[i] ==1:
            return i

    return -1

if __name__ == "__main__":
    string = [2,2,3,3,4,4,5,5]
    print(firstNonRepeatingg(string))
