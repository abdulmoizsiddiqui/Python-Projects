# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(student_heights)
total_height=0
for height in student_heights:
  total_height += height
# print(total_height)
num_of_students = n+1
# print(num_of_students)

avg_height = round(total_height/num_of_students)
print(avg_height)



