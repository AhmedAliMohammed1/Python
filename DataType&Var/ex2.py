f_name = str(input('Enter first name: '))
f_id = int(input('Enter first id: '))
f_grade = float(input('Enter first grade: '))


s_name = str(input('Enter second name: '))
s_id = int(input('Enter second id: '))
s_grade = float(input('Enter second grade: '))

print("Information for the students grades : ")
print(f_name + "(ID:"+str(f_id)+")" + "got grade : "+ str(f_grade))
print(s_name + "(ID:"+str(s_id)+")" + "got grade : "+ str(s_grade))
print("Avrage grade : " + str((f_grade + s_grade) / 2))