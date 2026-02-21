# firstVerse function defines variable with string "99Bottles"
# parameters define the count and wether bottle or bottles
# display variable
def firstVerse(count, bottleTense):
    firstVerse = "%s %s of beer on the wall, %s %s of beer." % (count, bottleTense, count, bottleTense)
    print(firstVerse)

# secondVerse function defines the second line to "99Bottles" song
# same parameters count and bottleTense define wether bottle or bottles and 1,2,3 etc.
# display variable
def secondVerse(count, bottleTense):
    secondVerse = "Take one down and pass it around, %s %s of beer on the wall!\n" % (count, bottleTense)
    print(secondVerse)

# lyrics function defines 2 variables as well as a while loop
# while loop has if elif statement nested.
def lyrics():
    count = 99                      # count is defined as 99 integer
    bottleTense = "bottles"         # bottleTense is defined as bottles string

    while count > 1:                # while count (starts at 99) is greater than 1
                                    # run firstVerse parameters count, bottleTense = bottles
        firstVerse(count, bottleTense)
        count -= 1                  # count is subtracted by 1 each iteration

        if count > 1:               # if count greater than 1 run secondVerse
            secondVerse(count, bottleTense)
        elif count == 1:            # else if count is equal to 1 bottleTense is
            bottleTense = "bottle"  # now equal to "bottle" run secondVerse
            secondVerse(count, bottleTense)

    firstVerse(count, bottleTense)  # exit while loop run firstVerse function

    count = "no more"               # last loop defines count as "no more"
    bottleTense = "bottles"         # firstVerse is now "no more bottles"
    secondVerse(count, bottleTense) # secondVerse is also "no more bottles"

    count = "No more"
    firstVerse(count, bottleTense)
    print("Go to the store and buy some more, 99 bottles of beer on the wall!\n")

# Run program : lyrics function
if __name__ == "__main__":
    lyrics()