# (a) Employee list operations

employees = [
    "Amina Rahman", "John Carter", "Sara Ahmed", "Liam Bennett", "Noah Khan",
    "Emily Stone", "David Miller", "Sophia Ali", "Mason Park", "Olivia Chen"
]

print("Original employees:", employees)

# 1) Split into two sublists of 5 names each
subList1 = employees[:5]
subList2 = employees[5:]

print("\nsubList1:", subList1)
print("subList2:", subList2)

# 2) Add new employee "Kriti Brown" into subList2
subList2.append("Kriti Brown")
print("\nAfter adding Kriti Brown to subList2:", subList2)

# 3) Remove the second employee from subList1 (index 1)
removed_employee = subList1.pop(1)
print("\nRemoved from subList1 (2nd employee):", removed_employee)
print("subList1 after removal:", subList1)

# 4) Merge both lists
mergedList = subList1 + subList2
print("\nMerged employee list:", mergedList)

# 5) Salary list corresponding to mergedList (assumed values)
salaryList = [52000, 61000, 48000, 75000, 69000, 54000, 82000, 59000, 66000, 88000]
print("\nOriginal salaryList:", salaryList)

# Give a 4% raise to every employee
for i in range(len(salaryList)):
    salaryList[i] = round(salaryList[i] * 1.04, 2)

print("\nUpdated salaryList after 4% raise:", salaryList)

# 6) Sort salaryList and show top 3 salaries
sortedSalaryList = sorted(salaryList)   # ascending
top3 = sortedSalaryList[-3:]            # last 3 elements are the highest
top3_desc = sorted(top3, reverse=True)  # show top 3 in descending order

print("\nSorted salaryList (ascending):", sortedSalaryList)
print("Top 3 salaries:", top3_desc)



# (b) Sentence to word list and reverse it

sentence = "Learning Python lists makes data processing easier"
print("Original sentence:", sentence)

wordList = sentence.split()       # converts sentence into a list of words
reversedWordList = wordList[::-1] # reverses the list using slicing

print("\nWord list:", wordList)
print("Reversed word list:", reversedWordList)
