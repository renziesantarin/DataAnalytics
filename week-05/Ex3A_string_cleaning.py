name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

name_1_lower = name_1.lower()
name_2_lower = name_2.lower()
name_3_lower = name_3.lower()

print(name_1_lower)
print(name_2_lower)
print(name_3_lower)

name_1_title = name_1.title()
name_2_title = name_2.title()
name_3_title = name_3.title()

print(name_1_title)
print(name_2_title)
print(name_3_title)

salary_1_remove_dollar = salary_1.replace("$", "")
salary_2_remove_dollar = salary_2.replace("$", "")

print(salary_1_remove_dollar)
print(salary_2_remove_dollar)

print(type(salary_1_remove_dollar))
print(type(salary_2_remove_dollar))

salary_1_clean = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_clean)
print(type(salary_1_clean))

salary_2_clean = int(salary_2.replace("$", "").replace(",", ""))

print(salary_2_clean)
print(type(salary_2_clean))

