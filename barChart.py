import matplotlib.pyplot as plt
import numpy as np

with open("diem_thi_thpt_2024.csv", encoding="utf8") as file:
	data = file.read().split("\n")

header = data[0]
student = data[1:]

# remove last student
student.pop()
totalStudent = len(student)

# split header
header = header.split(",")
subject = header[1:10]

# split each student in list
for i in range(totalStudent):
	student[i] = student[i].split(",")

not_take_score = [0,0,0,0,0,0,0,0,0]

# loop through all students
for s in student:
	for i in range(1,10): # 1 -> 9
		if s[i] == '' or s[i] is None:
			not_take_score[i-1] += 1

not_take_score_percent = [0,0,0,0,0,0,0,0,0]
for i in range(0,9):
	not_take_score_percent[i] = round((not_take_score[i]*100) /totalStudent,2)

# print(not_take_score_percent)
# print(subject)
# print(not_take_score)	

fig ,ax = plt.subplots()

y_pos = np.arange(len(subject))

plt.bar(y_pos, not_take_score_percent)
plt.xticks(y_pos, subject)

ax.set_ylim(0,100)

plt.ylabel('Percenage')
plt.title('Danh sách học sinh không đi kí thi hoặc không đi thi')

rects = ax.patches
for rect,label in zip(rects, not_take_score):
	heigth = rect.get_height()
	ax.text(rect.get_x() + rect.get_width() / 2, heigth + 5 , label, ha='center',va='bottom')
plt.show()