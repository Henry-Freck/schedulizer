from classes import course
from non_member_methods import generate_early_schedule
def main():
    possible_courses = []
    course_code = "not empty"

    while course_code != "":
        course_code = input("Enter course code, or enter to finish: ")

        if course_code == "":
            break

        end_time = int(input("Enter this section's end time: "))
        new_course = course(course_code, end_time = end_time)
        possible_courses.append(new_course)

    completed_schedule = generate_early_schedule(possible_courses, 1) #TODO dont hardcode this
    for course_instance in completed_schedule:
        print(course_instance)
if __name__ == "__main__":
    main()