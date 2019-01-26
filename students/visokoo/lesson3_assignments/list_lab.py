#!/usr/bin/env python3
'''
----------------------------------------------------
Assignment: list_lab.py
Author: visokoo | Created: 1/25/2019
ChangeLog: 1/25/2019, Created file

Fun with lists, complete four series.
----------------------------------------------------
'''

# Series 1
print("Series 1")
lstfruits = ["Apples", "Pears", "Oranges", "Peaches"]
print("Current fruits: ", lstfruits, sep="\n")

# Add a to the fruit the list
fruit = input("Enter in another fruit to add to the list: ")
lstfruits.append(fruit.capitalize())
print(lstfruits)

# Print the fruit at the given index number
number = input(f"Give me a number, 1 - {len(lstfruits)}: ")
print(f"The fruit at index {number} is {lstfruits[int(number)-1]}.")

# Add a fruit to the beginning of the list using the + operator
fruit2 = input("Enter another fruit to add to the front of the list: ")
lstfruits = [fruit2.capitalize()] + lstfruits
print(lstfruits)

# Add a fruit to the beginning of the list using .insert()
fruit3 = input("Enter another fruit to add to the front of the list: ")
lstfruits.insert(0, fruit3.capitalize())
print(lstfruits)

# Display all fruits that begin with the letter 'P'
print("Fruits that begin with the letter 'P':")
for fruit in lstfruits:
  if "P" in fruit:
    print(fruit)
  else: continue

# Series 2
print("Series 2")
print("Displaying the list:", lstfruits)
# removing the last item
lstfruits.pop()
print("Removed the last item.", lstfruits)

# Keep asking user to delete a fruit until a match is found and delete all occurrences
lstdupe = lstfruits * 2
print("Duplicated list:", lstdupe)
while True:
  fruit_to_delete = input("Which fruit do you want to delete? Type the name: ").capitalize()
  if fruit_to_delete in lstdupe:
    occurrence = lstdupe.count(fruit_to_delete)
    while occurrence > 0:
      lstdupe.remove(fruit_to_delete)
      occurrence -= 1
    print(f"Any occurrence of {fruit_to_delete} has been deleted.")
    print(lstdupe)
    break
  else:
    print("Given fruit not in list. Enter another fruit.")
    continue

# Series 3
print("Series 3")
while True:
  lst_of_fruits_to_remove = []
  for fruit in lstfruits:
    prompt = input(f"Do you like {fruit.lower()}? ").lower()
    if prompt == "yes":
      continue
    elif prompt == "no":
      lst_of_fruits_to_remove += [fruit]
    else:
      confirm = input("Please answer with 'yes' or 'no': ").lower()
      if confirm == "yes":
        continue
      else:
        lst_of_fruits_to_remove += [fruit]
        # had to remove them at the end of the loop because fruits were getting
        # skipped over if I removed them in the middle of the for loop
  for fruit in lst_of_fruits_to_remove:
    lstfruits.remove(fruit)
  break
print(lstfruits)

# Series 4
print("Series 4")
# Create a new empty list
newlstfruits = []
for fruit in lstfruits:
  # For each item in the old list, flip the letters and add the new item into the new list
  flipped = fruit[::-1]
  newlstfruits += [flipped]
print("Original list:", lstfruits)
print("Copied list:", newlstfruits)
