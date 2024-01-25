
avgGrade = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

gradeSum = 0
totalGradeSum = 0

for _ in range(20):
    gradeInfo = list(map(str, input().split(' ')))
    course = gradeInfo[0]
    grade = float(gradeInfo[1])
    courseAvg = gradeInfo[2]

    if courseAvg != 'P':
        gradeSum += grade * avgGrade[courseAvg]
        totalGradeSum += grade
    
print(round(gradeSum / totalGradeSum, 6))