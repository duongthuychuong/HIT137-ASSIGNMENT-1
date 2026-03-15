"""
Question 3
Group Name: DAN/EXT 55
Group Members:
1. Thuy Chuong Duong - s385201
2. Kar Keat Koh - s394886
3. Joshua Joseph Bargamento - s394292
4. Sihao Cui - s399370
"""
Program on the number of students in a class and their grades
"""

# Ask for number of students
num_students = int(input("How many students? "))
if num_students < 3 or num_students > 10:
  print("Please enter a number between 3 and 10.")
else:

  # Initialize variables for calculations
  student_data = []
  total_score = 0
  highest_score = -1
  lowest_score = 101
  highest_student = ""
  lowest_student = ""

  # Loop to get data for each student
  for i in range(1, num_students + 1):
    name = input(f"Student {i} name: ")
    score = float(input(f"{name}'s score: "))

    # Determined Grade
    if score >= 85: grade = "HD"
    elif score >= 75: grade = "D"
    elif score >= 65: grade = "C"
    elif score >= 50: grade = "P"
    else: grade = "F"

    # Store student data
    student_data.append((name, score, grade))
    total_score += score

    # For Highest
    if score > highest_score:
      highest_score = score
      highest_student = name

    # For Lowest
    if score < lowest_score:
      lowest_score = score
      lowest_student = name

  # Display Results
  print("\nResults:")
  for name, score, grade in student_data:
    print(f"{name}: {score} ({grade})")

  average = total_score / num_students
  print(f"\nAverage Score: {average:.2f}")
  print(f"Highest Score: {highest_student} ({highest_score})")
  print(f"Lowest Score: {lowest_student} ({lowest_score})")
