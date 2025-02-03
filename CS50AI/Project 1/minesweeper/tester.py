from minesweeper import *

ai = MinesweeperAI()

# ai.add_knowledge((2, 0), 2)
# for sentence in ai.knowledge:
#     print(sentence.cells, ":", sentence.count)
# ai.add_knowledge((2, 1), 2)
# for sentence in ai.knowledge:
#     print(sentence.cells, ":", sentence.count)
# ai.add_knowledge((2, 2), 1)
# for sentence in ai.knowledge:
#     print(sentence.cells, ":", sentence.count)
# ai.add_knowledge((1, 2), 2)
# for sentence in ai.knowledge:
#     print(sentence.cells, ":", sentence.count)
# ai.add_knowledge((0, 2), 2)
# for sentence in ai.knowledge:
#     print(sentence.cells, ":", sentence.count)
# ai.add_knowledge((3, 0), 0)
# ai.add_knowledge((3, 1), 0)
# ai.add_knowledge((3, 2), 0)
# ai.add_knowledge((3, 3), 0)
# ai.add_knowledge((2, 3), 0)
# ai.add_knowledge((1, 3), 0)
# ai.add_knowledge((0, 3), 0)

# print(a := ai.make_safe_move())
# print(a := ai.make_random_move())
# print(ai.mines)
# print(ai.safes)
print("\n")

print("adding (0,1), 1")
ai.add_knowledge((0,1), 1)
for sentence in ai.knowledge:
    print(sentence.cells, sentence.count)
print(ai.safes)
print(ai.mines)
print("\n")

print("adding (1,0), 1")
ai.add_knowledge((1,0), 1)
for sentence in ai.knowledge:
    print(sentence.cells, sentence.count)
print(ai.safes)
print(ai.mines)
print("\n")

print("adding (1,2), 1")
ai.add_knowledge((1,2), 1)
for sentence in ai.knowledge:
    print(sentence.cells, sentence.count)
print(ai.safes)
print(ai.mines)
print("\n")

print("adding (0,4), 0")
ai.add_knowledge((0,4), 0)
for sentence in ai.knowledge:
    print(sentence.cells, sentence.count)
print(ai.safes)
print(ai.mines)
print("\n")

print("adding (3,4), 0")
ai.add_knowledge((3,4), 0)
for sentence in ai.knowledge:
    print(sentence.cells, sentence.count)
print(ai.safes)
print(ai.mines)
print("\n")

print("adding (3,1), 0")
ai.add_knowledge((3,1), 0)
for sentence in ai.knowledge:
    print(sentence.cells, sentence.count)
print(ai.safes)
print(ai.mines)
print("\n")
