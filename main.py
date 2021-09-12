from classes import course
from non_member_methods import generate_early_schedule
from non_member_methods import generate_late_schedule
from non_member_methods import convert_time
from non_member_methods import is_valid_time
from classes import schedule

def course_input():
    possible_courses = []
    course_code = "not empty"
    #get course code, then loop thru day/time input
    while course_code != "":
        course_code = input("Enter course code, or enter to finish: ")

        if course_code == "":
            break

        #get day/time data for first section
        meeting_days_string = input("Enter the days the first section meets (M T W Th F): ")
        meeting_days_set = set()
        for i, char in enumerate(meeting_days_string):
            if char.upper() in {'M', 'T', 'W', 'F'}:
                if char.upper() == "T":
                    if i<len(meeting_days_string)-1:
                        if meeting_days_string[i+1].lower() == "h":
                            char = "Th"
                meeting_days_set.add(char)



        start_time = input("Enter start time of first section: ")

        while(not is_valid_time(start_time)):
            start_time = input("Enter a valid start time (ex: 10:30 am): ")

        start_time = convert_time(start_time)

        end_time = input("Enter end time of first section: ")
        end_time_set = False

        while(not end_time_set):
            if(is_valid_time(end_time)):
                if (convert_time(end_time)>start_time):
                    end_time = convert_time(end_time)
                    end_time_set = True
                else:
                    end_time = input("The end time must come after the start time: ")
            else:
                end_time = input("Please enter a valid time (ex: 11:30 AM): ")


        new_course = course(course_code, start_time = start_time, end_time = end_time, days = meeting_days_set)
        possible_courses.append(new_course)


        #get day/time data for next sections
        while meeting_days_string != "":

            meeting_days_string = input("Enter the days the next section meets (M T W Th F), or nothing to enter next course: ")

            if meeting_days_string == "":   #break on no entry
                break

            meeting_days_set = set()
            for i, char in enumerate(meeting_days_string):
                if char.upper() in {'M', 'T', 'W', 'F'}:
                    if char.upper() == "T":
                        if i < len(meeting_days_string) - 1:
                            if meeting_days_string[i + 1].lower() == "h":
                                char = "Th"
                    meeting_days_set.add(char)

            start_time = input("Enter start time of this section: ")

            while (not is_valid_time(start_time)):
                start_time = input("Enter a valid start time (ex: 10:30 am): ")

            start_time = convert_time(start_time)
            end_time = input("Enter end time of this section: ")

            end_time_set = False

            while (not end_time_set):
                if (is_valid_time(end_time)):
                    if (convert_time(end_time) > start_time):
                        end_time = convert_time(end_time)
                        end_time_set = True
                    else:
                        end_time = input("The end time must come after the start time: ")
                else:
                    end_time = input("Please enter a valid time (ex: 11:30 AM): ")

            new_course = course(course_code, start_time=start_time, end_time=end_time, days = meeting_days_set)
            possible_courses.append(new_course)
    return possible_courses


def main():
    schedule_timing = input("Enter the optimal timing of your schedule (early/late), defaults to early: ")
    num_courses = int(input("How many courses would you like in the final schedule?: "))

    possible_courses = course_input()

    if schedule_timing.lower() == "late" or schedule_timing.lower() == "l":
        completed_course_list = generate_late_schedule(possible_courses, num_courses)
    else:
        completed_course_list = generate_early_schedule(possible_courses, num_courses)

    completed_schedule = schedule(completed_course_list)
    print(completed_schedule)

if __name__ == "__main__":
    main()