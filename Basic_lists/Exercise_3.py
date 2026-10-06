# Exercise 3: Update and Remove Items 
colors = ["Red", "Green", "Blue", "Yellow", "Black"]
colors[2] = "Purple" # Update "Blue" to "Purple"
colors[4] = "White" # Update "Black" to "White"
colors.remove("Green") # Remove "Green" from the list
colors.pop() # Remove the last item from the list
colors.pop(0) # Remove the first item from the list
colors.clear() # Remove all items from the list
colors.append("Orange") # Add "Orange" to the list


print("Final list:", colors)

