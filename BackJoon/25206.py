scoreList = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

totalScore = 0.0
totalGrade = 0.0

for i in range(20):
    s = input()
    data = s.split()
    if data[2] == "P":
        continue
    grade = float(data[1])
    totalScore += (scoreList.get(data[2]) * grade)
    totalGrade += grade

print(totalScore / totalGrade)