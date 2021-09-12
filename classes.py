#Object heirarchy for schedulizer

from non_member_methods import stringify_time

class schedule:

    #TODO should schedule contain a set of courses, a list of courses or both

    #initialize a empty schedule
    def __init__(self):
        self.courses = set()

    #initialize a schedule from a set of courses
    def __init__(self, course_set):
        self.courses = course_set

    #initialize a schedule from a set of courses
    def __init__(self, course_list):
        self.courses = set(course_list)

    def add_course(self, course):
        #TODO complete based on self.courses data structure
        pass

class course:

    def __init__(self, code = "0000", days = set(), start_time = 0, end_time = 0):
            self.code = code
            self.days = days
            self.start_time = start_time
            self.end_time = end_time

    def __str__(self):
        start_time_string = stringify_time(self.start_time)
        end_time_string = stringify_time(self.end_time)
        day_string = ""
        for day in ["M", "T", "W", "Th", "F"]:
            if day in self.days:
                day_string += (" " + day)

        return (self.code + " from " + start_time_string + " to " + end_time_string + " on" + day_string)

    def is_compatable(self, course_list):
        for course in course_list:
            if self.days.intersection(course.days):
                if not((self.end_time < course.start_time) or (self.start_time > course.end_time)):  #checks that there is overlap between the two time frames
                    return False
        return True
