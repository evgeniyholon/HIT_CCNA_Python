student1_math = int(input('Enter math score for student 1: '))
student1_comp = int(input('Enter comp score for student 1: '))
student2_math = int(input('Enter math score for student 2: '))
student2_comp = int(input('Enter comp score for student 2: '))
gpa1 = (student1_comp + student1_math) / 2
gpa2 = (student2_comp + student2_math) / 2
print(f'GPA student-1: {gpa1}')
print(f'GPA student-2: {gpa2}')
print(f'GPA students: {(gpa1 + gpa2) / 2}')
