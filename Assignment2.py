university_data = {
"S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}


# Q1: Print all student names and their majors

for student_id, student_info in university_data.items():
    name = student_info['name']
    major = student_info['major']
    print(f'{name} - {major}')


# Q2: Average score per course per student 


for student_id, student_info in university_data.items():
    name = student_info['name']
    print(f"\n{name}'s Course Averages:")
    for course, scores in student_info['courses'].items():
        avg_score = sum(scores.values()) / len(scores)
        print(f" {course}: {avg_score:.2f}")

# Q3: Find students who scored >90 in final of Python101 

for student_id, student_info in university_data.items():
    courses = student_info['courses']
    if 'Python101' in courses:
        if courses['Python101']['final'] > 90:
            print(f"{student_info['name']} scored {courses['Python101']['final']}")


# Q4: Add new course AI101 for student S101

university_data["S101"]["courses"]["AI101"] = {"midterm": 85, "final": 90, "project": 88}
print(university_data['S101']['courses'])

# Q5: Print average for each course

course_scores = {}
for student_info in university_data.values():
    for course, scores in student_info['courses'].items():
        avg = sum(scores.values()) / 3
        if course not in course_scores:
            course_scores[course] = [avg]
        else:
            course_scores[course].append(avg)

print("Average score per course across all students:\n")
for course in course_scores:
    scores_list = course_scores[course]
    avg_score = sum(scores_list) / len(scores_list)
    print(f"{course}: {avg_score:.2f}")