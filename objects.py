#Object heirarchy for schedulizer

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

    #initialize empty course
    def __init__(self):
        self.code = ""
        #todo uncomment theses fields once basic algorithms are working, also add to other constructor
        #self.section = ""
        #self.name = ""
        #self.instructor = ""
        #self.room  = ""
        self.days = []
        self.start_time = 0  #TODO find a better way to declare this with no value
        self.end_time = 0  #TODO same here

    def __init__(self, code, days, start_time, end_time):
            self.code = code
            self.days = days
            self.start_time = start_time
            self.end_time = end_time
