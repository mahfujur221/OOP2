marks = float(input("Enter your marks in Computer Science: "))

if marks > 80:
    print("Grade: A+")
elif marks >= 75 and marks < 80:
    print("Grade: A")
elif marks >= 70 and marks < 75:
    print("Grade: A-")
elif marks >= 65 and marks < 70:
    print("Grade: B+")
elif marks >= 60 and marks < 65:
    print("Grade: B")
elif marks >= 55 and marks < 60:
    print("Grade: B-")
elif marks >= 50 and marks < 55:
    print("Grade: C+")
elif marks >= 45 and marks < 50:
    print("Grade: c")
elif marks >= 40 and marks < 55:
    print("Grade: D")
else:
    print("Grade: F")