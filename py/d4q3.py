courses = [
    {"name": "Python Basics", "category": "Programming", "skill_level": "Beginner", "rating": 4.8},
    {"name": "Advanced Python", "category": "Programming", "skill_level": "Intermediate", "rating": 4.9},
    {"name": "Machine Learning", "category": "Data Science", "skill_level": "Advanced", "rating": 4.7},
    {"name": "Data Analysis with Python", "category": "Data Science", "skill_level": "Beginner", "rating": 4.6},
    {"name": "Web Development", "category": "Programming", "skill_level": "Intermediate", "rating": 4.5},
    {"name": "AI Fundamentals", "category": "AI", "skill_level": "Advanced", "rating": 4.8}
]

def recommend_course(skill_level, category):
    matching_courses = [course for course in courses if course["category"] == category and course["skill_level"] == skill_level]
   
    if not matching_courses:
        return "No suitable course found."
   
    highest = matching_courses[0]
    for course in matching_courses:
        if course['rating'] > highest['rating']:
            highest = course
   
    return f"Recommended: {highest['name']}"
print("Enter your skill level ")
skill_level = input("Beginner, Intermediate, Advanced: ")
print("Enter your category of interest ")
category = input("Programming, Data Science, AI: ")

print(recommend_course(skill_level, category))
