list1 = input("Enter the elements of the first list sepereated by spaces: ").split()
list2 = input("Enter the elements of the second list sepereated by spaces: ").split()

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)

if common_elements:
    print("the common elements are: ", list(common_elements))
else:
    print("there are no common elements.")