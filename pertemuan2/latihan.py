def hitung_nilai(tugas,uts,uas):

    score =(tugas * 0.3 ) + (uts * 0.3) + (uas * 0.4)
    print ("Nilai:", score)

    if score >= 85:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 55:
        print("Grade: C")
    elif score >= 40:
        print("Grade: D")
    elif score <= 40:
        print("Grade: E")
    
hitung_nilai(80,75,90)