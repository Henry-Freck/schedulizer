#Original code by Henry Clay Freck
import re

def generate_early_schedule(possible_courses, num_courses): #todo make work for days of the week/overlap
    possible_courses.sort(key = lambda course: course.end_time)

    chosen_courses = []
    course_set = set()
    num_chosen = 0

    for course in possible_courses:
        if num_chosen < num_courses:
            if course.code not in course_set:
                if course.is_compatable(chosen_courses):
                    chosen_courses.append(course)
                    num_chosen += 1
                    course_set.add(course.code)
        else:
            break

    if len(chosen_courses) == num_courses:
        return chosen_courses

    else:
        return ["It is impossible to generate a valid schedule of " + str(num_courses) + " courses with the inputs you have given"]

def generate_late_schedule(possible_courses, num_courses):
    possible_courses.sort(key = lambda course: course.start_time, reverse = True)

    chosen_courses = []
    course_set = set()
    num_chosen = 0

    for course in possible_courses:
        if num_chosen < num_courses:
            if course.code not in course_set:
                if course.is_compatable(chosen_courses):
                    chosen_courses.append(course)
                    num_chosen += 1
                    course_set.add(course.code)
        else:
            break

    if len(chosen_courses) == num_courses:
        return chosen_courses

    else:
        return ["It is impossible to generate a valid schedule of " + str(num_courses) + " courses with the inputs you have given"]

def convert_time(string_time):
    time_regex = re.compile(r'(\d{1,2}):(\d{2}) *(AM|PM)', re.IGNORECASE)  #TODO make 10 am valid and 13:69 invalid
    time_data = time_regex.search(string_time)

#throws error if incorrect time value is inputted
    hour = time_data.group(1)
    minutes = time_data.group(2)
    am_pm = time_data.group(3)

    #this will make modding of time possible
    if hour == "12":
        hour = "00"

    #accumulate minutes
    num_minutes = 0
    if am_pm.lower() == "pm":
        num_minutes += 720
    num_minutes += int(hour)*60
    num_minutes += int(minutes)

    return num_minutes



def is_valid_time(string_time):
    time_regex = re.compile(r'(\d{1,2}):(\d{2}) *(AM|PM)', re.IGNORECASE)
    return bool(re.match(time_regex, string_time))



def stringify_time(time):
    am_pm = "AM"

    if time>=720:
        am_pm = "PM"
        time -= 720

    minutes = str(time % 60)

    if (len(minutes) == 1):
        minutes = "0" + minutes

    hours = str(time // 60)

    if hours  == "0":
        hours = "12"
    return (hours + ":" + minutes + " " + am_pm)
