students = []
num_students = int(input("Enter the number of students: "))# get the number of students from the user
    
for i in range(num_students):# loop through the input and add each name and score to the list
  print(f"Enter the name and score for student #{i+1}: ")
  name = input("Name: ")
  score = float(input("Score: "))
  students.append([name, score])
    
second_lowest_grade = sorted(list(set([score for name, score in students])))[1]# find the second lowest grade
    
second_lowest_students = [name for name, score in students if score == second_lowest_grade] # create a list of students with the second lowest grade
    
second_lowest_students.sort()# sort the list of students alphabetically
    
print("Students with the second lowest score:")# print the names of the second lowest students
for name in second_lowest_students:
  print(name)