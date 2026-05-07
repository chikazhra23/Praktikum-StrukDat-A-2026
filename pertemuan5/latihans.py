ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}

A = ukm_coding.difference(ukm_robotik)

ukm=ukm_coding.union(ukm_robotik)

print(ukm)
print(A)
print("Andi" in ukm_robotik )