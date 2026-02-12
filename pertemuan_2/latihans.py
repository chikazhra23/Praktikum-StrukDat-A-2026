keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
A = keahlian_A.difference_update(keahlian_B)
keahlian_A = {"Python", "Java", "SQL", "Git"}

keahlian_c = keahlian_A & keahlian_B
print(keahlian_A)
print(keahlian_B)

print(keahlian_c)

