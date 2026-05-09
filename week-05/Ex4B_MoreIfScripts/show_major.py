# Student information
student_name = "MaoMao Kan"
student_major = "BIOL"

# Inside each condition, the major name and office location are assigned to variables.
if student_major == "BIOL":

    major_name = "Biology"

    office_location = "Science Bldg, Room 310"

elif student_major == "CSCI":

    major_name = "Computer Science"

    office_location = "Sheppard Hall, Room 314"

elif student_major == "ENG":

    major_name = "English"

    office_location = "Kerr Hall, Room 201"

elif student_major == "HIST":

    major_name = "History"

    office_location = "Kerr Hall, Room 114"

elif student_major == "MKT":

    major_name = "Marketing"

    office_location = "Westly Hall, Room 310"

# This is the alternative condition if the major code does not match any of the above.
else:

    major_name = "Unknown Major"

    office_location = "Office Not Found"

# Print results
print(f"Student Name: {student_name}")
print(f"Major Code: {student_major}")
print(f"Major Name: {major_name}")
print(f"Department Office: {office_location}")
