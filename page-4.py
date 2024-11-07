import array as arr

myArr = arr.array('i',[1,2,3])
print(type(myArr))
print(myArr)
print(myArr[1])

# myCharArr= arr.array('u',['a','b','c'])
# print(type(myCharArr))
# print(myCharArr)

# List
print('\nmyFruitList:')
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList[0] = "orange"
myFruitList[1] = "kiwi"
myFruitList[2] = "strawberry"
print(myFruitList)

# 2D List
group = [
    ["Siraz", "Tri", "Denira"],
    ["Jdoe", "Mmajor", "LJuan"]
]
print(group[1])
print(group[1][2])

# Tupple
print('\nTupple:')
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
print(myFinalAnswerTuple)


# Dictionary
print('\nDictionary:')
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "cherry"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

# Set: tidak mengijinkan duplicate, tdk seperti list bisa modify
# List: mutable (elemennya bisa diedit)
# Tuple: immutable (elemennya gabisa diubah)
print("\nSet")
mySet = {1,2,2,4}
print(mySet)
# print(mySet[0]) tidak bisa
# print(mySet[1])
# print(mySet[2])
# print(mySet[3])
# print(mySet[4])