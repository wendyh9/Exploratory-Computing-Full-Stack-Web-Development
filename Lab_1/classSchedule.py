class classInfo :
    def __init__(self, num, courseDept, courseNum, courseName, credits, lectureDays, startTime, endTime, avgGrade):
        self.num = num
        self.courseDept = courseDept
        self.courseNum = courseNum
        self.courseName = courseName
        self.credits = credits
        self.lectureDays = lectureDays
        self.startTime = startTime
        self.endTime = endTime
        self.avgGrade = avgGrade 

    def printClassInfo(self):
        print(f'COURSE {self.num}: {(self.courseDept).strip()}{(self.courseNum).strip()}: {self.courseName}', end = '') 
        print(f'Number of Credits: {self.credits}', end='') 
        print(f'Days of Lectures: {self.lectureDays}', end='')
        print(f'Lecture Time: {(self.startTime).strip()} - {self.endTime}', end='')
        print(f'Stat: an average, students get {(self.avgGrade).strip()}% in this course', end='')
        print('\n')
    
# Number of Credits: {self.credits}Days of Lectures: {self.lectureDays}Lecture Time: {self.startTime} - {self.endTime}Stat: an average, students get {self.avgGrade}% in this course
with open('classesInput.txt', 'r') as file:
    info_arr = file.readlines()
    index = 0
    numClass = int(info_arr[index])
    index += 1

    for i in range(numClass):
        temp = classInfo(i + 1,
            info_arr[index], info_arr[index + 1], info_arr[index + 2], 
            info_arr[index + 3], info_arr[index + 4], info_arr[index + 5], 
            info_arr[index + 6], info_arr[index + 7])
        temp.printClassInfo()
        index += 8

# plan:
    # just use temp
    # input info
    # print info
    # repeat
        