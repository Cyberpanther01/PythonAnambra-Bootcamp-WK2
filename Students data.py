"""5. Write a wimple python code , in the code, 
create a dictionary of students data with the following keys: names, REG_NO, gender.
 Each will have a minimum of 5 entries. The student data in this format: ___ with REG_NO ___is a ___"""

student_data = { 
    
    "student_01" : { "Name": "Chinaza", "Gender": "Female", "REG_NO": "15790" },
    "student_02" : { "Name": "Maxwell", "Gender": "Male", "REG_NO": "76850" },
    "student_03" : { "Name": "Blessing", "Gender": "Female", "REG_NO": "09314"},
    "student_04" : { "Name": "Precious", "Gender": "Female", "REG_NO": "09425"},
    "student_05" : { "Name": "Benjamin", "Gender": "Male", "REG_NO": "96740"}

}

for student_id, data in student_data.items():
    print(f"{data['Name']} with REG NO. {data['REG_NO']} is a {data['Gender']}")


    
