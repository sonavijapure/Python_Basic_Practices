#Let’s create a function which calculates a dog’s age in dog years! This function will accept the name of the dog 
# and the age in human years. It will calculate the age of the dog in dog years and return a string describing the dog’s age. 

# Write your dog_years function here:
def dog_years(name, age):
  return f"{name}, you are {age*7} year old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"