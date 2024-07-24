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

total_Languge = 0
English = 0
Russian = 0
French = 0
Chinese = 0 
Germary = 0
Janpanese = 0
Korean = 0 
for s in student:
	if s[10] != '':
		total_Languge += 1
	if s[10] == 'N1':
		English += 1	
	if s[10] == 'N2':
		Russian += 1
	if s[10] == 'N3':
		French += 1
	if s[10] == 'N4':
		Chinese += 1
	if s[10] == 'N5':
		Germary += 1
	if s[10] == 'N6':
		Janpanese += 1
	if s[10] == 'N7':
		Korean += 1	

subject_Languge_Name = ['tiếng Nga','tiếng Pháp','tiếng Trung','tiếng Đức','tiếng Nhật','tiếng Hàn']		
subject_Languge = [Russian,French,Chinese,Germary,Janpanese,Korean]						

 
# Creating plot
fig = plt.figure(figsize=(10, 7))
plt.pie(subject_Languge, labels=subject_Languge_Name)
 
# show plot
plt.show()

