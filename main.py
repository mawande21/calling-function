
# Filter the grades to only display everyone above (and including) 70%
grade = [20, 10, 90, 85, 40, 75, 65, 64, 12, 74, 71, 98, 50]

new_grades = list(filter(lambda x:x>=70, grade)) #using list lambda
print("Old listof grades is :",grade,"\nNew list of grades:",new_grades)

#Convert the ages into "dog years" (x7)
dog_ages = [12, 8, 4, 1, 2, 6, 4, 4, 5]

dog_yrs = list(map(lambda x:x*7, dog_ages))
print("Dog list ages",dog_ages,"\nDog in human years:", dog_yrs)

# Convert the transactions to a single total
transactions = [51.0, 49.99, 80.99, 67.99, 120.52, 23.49]

sngle_total = sum(transactions)
print(sngle_total)

