from classes import course
from non_member_methods import generate_early_schedule
from non_member_methods import generate_late_schedule
def main():
    possible_courses = []
    course_code = "not empty"

    num_courses = int(input("How many courses would you like in the final schedule?: "))

    while course_code != "":
        course_code = input("Enter course code, or enter to finish: ")

        if course_code == "":
            break

        start_time = int(input("Enter this sections start time: "))
        end_time = int(input("Enter this section's end time: "))
        new_course = course(course_code, end_time = end_time, start_time = start_time)
        possible_courses.append(new_course)

    completed_schedule = generate_late_schedule(possible_courses, num_courses)

    for course_instance in completed_schedule:
        print(course_instance)

if __name__ == "__main__":
    main()