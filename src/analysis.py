import pandas as pd
import matplotlib.pyplot as plt
from db import get_connection

QUERY_COURSE_AVG = """
SELECT
    c.CourseCode,
    c.CourseName,
    AVG(g.NumericGrade) AS AvgGrade
FROM Enrollments e
JOIN Courses c ON e.CourseID = c.CourseID
JOIN Grades g ON e.EnrollmentID = g.EnrollmentID
GROUP BY c.CourseCode, c.CourseName
ORDER BY AvgGrade ASC;
"""

QUERY_DEPT_AVG = """
SELECT
    s.Department,
    AVG(g.NumericGrade) AS DepartmentAvg
FROM Enrollments e
JOIN Students s ON e.StudentID = s.StudentID
JOIN Grades g ON e.EnrollmentID = g.EnrollmentID
GROUP BY s.Department
ORDER BY DepartmentAvg DESC;
"""

def main():
    conn = get_connection()

    df_course = pd.read_sql(QUERY_COURSE_AVG, conn)
    df_dept = pd.read_sql(QUERY_DEPT_AVG, conn)

    print("\n--- Course Average ---")
    print(df_course)

    print("\n--- Department Average ---")
    print(df_dept)

    # Chart 1
    plt.figure()
    plt.bar(df_course["CourseCode"], df_course["AvgGrade"])
    plt.title("Average Grade by Course")
    plt.xlabel("Course")
    plt.ylabel("Avg Grade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("course_avg.png")
    plt.show()

    # Chart 2
    plt.figure()
    plt.bar(df_dept["Department"], df_dept["DepartmentAvg"])
    plt.title("Average Grade by Department")
    plt.xlabel("Department")
    plt.ylabel("Avg Grade")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("dept_avg.png")
    plt.show()

    conn.close()

if __name__ == "__main__":
    main()
