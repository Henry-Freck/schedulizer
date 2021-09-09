#Original code by Henry Clay Freck

def generate_early_schedule(possible_courses, num_courses):
    possible_courses.sort(key = lambda course: course.end_time)
    chosen_courses = possible_courses[0:num_courses]
    return chosen_courses
