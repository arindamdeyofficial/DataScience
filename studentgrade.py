# 2
def insertHashData(StudentHashRecords):
    f = open('inputPS18.txt', "r")
    while f.readable():
        rec = f.readline().split('/')
        if rec == ['']:
            break
        StudentHashRecords.insertStudentRec(rec[0], float(rec[1].rstrip("\n")))
    f.close()

# 3
def hallOfFame(StudentHashRecords):
    # Input file will be promptsPS18.txt and tag will be "hallOfFame:"
    # return list of passout students who have topped their department
    # in there grad year, append in outputPS18.txt file
    if gethalloffametrigger() == 1:
        # dept number can be dynamic
        maxcgpa = []
        depts = []  # list of all dept
        contentToWrite = ''
        count = 0
        # liner data form of students
        allstudents = \
            [[st[0][4:7], int(st[0][0:4]), st[0], st[1]] # [dept, year, studentId, Cgpa]
                       for item in StudentHashRecords.hashTable
                       if item is not None
                       for st in item
                       if 2010 <= int(st[0][0:4]) <= 2016]
        yrs = []
        for st in allstudents:
            if st[0] not in depts:
                depts.append(st[0])
        # depts = list(set(st[0] for st in allstudents))
        for st in allstudents:
            if st[1] not in yrs:
                yrs.append(st[1])
        # yrs = list(set(st[1] for st in allstudents))
        for dept in depts:
            for y in yrs:
                for st in allstudents:
                    if st[0] == dept and st[1] == y:
                        contentToWrite += (st[2] + '/' + str(st[3]) + '\n')
                        ++count
        contentToWrite = '---------- hall of fame ----------\nTotal eligible students: ' + str(count) + \
                         '\nQualified students:\n' + contentToWrite + \
                         '\n-------------------------------------\n'
        generateoutputPS18(contentToWrite)


def gethalloffametrigger():
    f = open('promptsPS18.txt', "r")
    while f.readable():
        cont = f.readline()
        if cont == '':
            break
        if 'hallOfFame' in cont:
            return 1


# 4
def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    # implement year restriction
    contenttowrite = ''
    counter = 0
    for item in StudentHashRecords.hashTable:
        if item is not None:
            for student in item:
                if (CGPAFrom <= student[1] <= CPGATo) and (2015 <= int(student[0][0:4]) <= 2019):
                    contenttowrite += student[0] + '/' + str(student[1]) + '\n'
                    ++counter
    contenttowrite = f'---------- new course candidates ----------\nInput: {cgpafrom}:{cgpato}\nTotal eligible students: {counter}' \
                     f'\nQualified students:\n' + contenttowrite
    contenttowrite += '\n-------------------------------------\n'
    generateoutputPS18(contenttowrite)


def getCourseListRange():
    f = open('promptsPS18.txt', "r")
    while f.readable():
        cont = f.readline()
        if cont == '':
            break
        if 'courseOffer' in cont:
            contlst = cont.split(':')
            f.close()
            return float(contlst[1]), float(contlst[2].rstrip('\n'))


# 5
def depAvg(StudentHashRecords):
    # depts CSE, MEC, ECE, ARC
    # dept number can be dynamic
    contentToWrite = ''
    depts = []
    # liner data form of students
    allstudents = [[st[0][4:7], st[1]]  # [dept, year, studentId, Cgpa]
                   for item in StudentHashRecords.hashTable
                   if item is not None
                   for st in item]
    for st in allstudents:
        if st[0] not in depts:
            depts.append(st[0])
    # depts = list(set(st[0] for st in allstudents))
    for dept in depts:
        stofdept = [st[1] for st in allstudents]
        contentToWrite += str(dept) + ': max: ' + \
                        str(max(stofdept)) + ', avg: ' + str(round(sum(stofdept) / len(stofdept), 1)) + '\n'
    contentToWrite = '---------- department CGPA ----------\n' \
                     + contentToWrite + '\n-------------------------------------\n'
    generateoutputPS18(contentToWrite)


def generateoutputPS18(content):
    f = open('outputPS18.txt', "a")
    f.write(content + '\n')
    f.close()

class HashTable:

    def __init__(self):
        # creating Hashtable - nested list.
        self.initializeHash()

    # 1
    # This function creates an empty hash table and points to null.
    def initializeHash(self):
        # creating Hashtable - nested list.
        self.hashTable = [None]

    def getHash(self, studentId):
        # Calculate StudentHashRecords for each record of inputPS18 file
        # YYYYAAADDDD
        # 2010CSE1223
        h = 0
        for char in studentId:
            h += ord(char)
        return h % 9 + h % 10

    def insertStudentRec(self, studentId, CGPA):
        # This function inserts the student id
        hash_key = self.getHash(studentId)
        if (len(self.hashTable) - 1) < hash_key:
            for k in range(hash_key - len(self.hashTable) + 2):
                if k == 0:
                    self.hashTable[k] = []
                else:
                    self.hashTable.append([])
        data = self.hashTable[hash_key]
        if data is None:
            self.hashTable[hash_key] = [[studentId, CGPA]]
        else:
            self.hashTable[hash_key].append([studentId, CGPA])

    # def searchStudentwithStudentId(self, studentId):
    #     hash_key = self.getHash(studentId)
    #     eleatIndex = self.hashTable[hash_key]
    #     if eleatIndex is not None:
    #         for item in eleatIndex:
    #             if item[0] == studentId:
    #                 return item[1]

    # def searchStudentwithCgpa(self, CGPAFrom, CPGATo):
    #     studentColl = []
    #     for item in self.hashTable:
    #         if item is not None:
    #             for student in item:
    #                 if CGPAFrom <= student[1] <= CPGATo:
    #                     studentColl.append(student)
    #     return studentColl

    def destroyHash(self):
        self.hashTable = []

    # def getAll(self):
    #     studentColl = []
    #     for item in self.hashTable:
    #         if item is not None:
    #             for student in item:
    #                 studentColl.append(student)
    #     return studentColl
    #
    # def display_all(self):
    #     for item in self.hashTable:
    #         if item is not None:
    #             for student in item:
    #                 print('Student Id: ' + student[0] + ' CGPA: ' + student[1])

if __name__ == "__main__":
    # data generation
    # studentgrade.generateinputPS18()

    # object creation
    StudentHashRecords = HashTable()

    # 2
    # reads from file inputPS18.txt and insert into the Hash table in a loop inside this function
    # insertStudentRec(StudentHashRecords, rec[0], float(rec[1].rstrip("\n")))
    insertHashData(StudentHashRecords)

    # 3
    hallOfFame(StudentHashRecords)

    # 4
    cgpafrom, cgpato = getCourseListRange()
    newCourseList(StudentHashRecords, cgpafrom, cgpato)

    # 5
    depAvg(StudentHashRecords)

    # 6
    StudentHashRecords.destroyHash()

    # Unit tests
    # grade2019ECE3 = StudentHashRecords.searchStudentwithStudentId('2019ECE3')
    # print('Grade for student Id 2019ECE3 is : ' + str(grade2019ECE3) + ' and it''s a ' + (
    #     'match' if grade2019ECE3 == 1.5 else 'not match'))
    #
    # grade2010ECE0 = StudentHashRecords.searchStudentwithStudentId('2010ECE0')
    # print('Grade for student Id 2010ECE0 is : ' + str(grade2010ECE0) + ' and it''s a ' + (
    #     'match' if grade2010ECE0 == 0.0 else 'not match'))
    #
    # grade2011ECE7 = StudentHashRecords.searchStudentwithStudentId('2011ECE7')
    # print('Grade for student Id 2011ECE7 is : ' + str(grade2011ECE7) + ' and it''s a ' + (
    #     'match' if grade2011ECE7 == 3.5 else 'not match'))
    #
    # grade2011ARC10 = StudentHashRecords.searchStudentwithStudentId('2011ARC10')
    # print('Grade for student Id 2011ARC10 is : ' + str(grade2011ARC10) + ' and it''s a ' + (
    #     'match' if grade2011ARC10 == 5.0 else 'not match'))
    #
    # grade2019MEC35 = StudentHashRecords.searchStudentwithStudentId('2019MEC35')
    # print('Grade for student Id 2019MEC35 is : ' + str(grade2019MEC35) + ' and it''s a ' + (
    #     'match' if grade2019MEC35 == 1.0 else 'not match'))
    #
    # grade2020ARC55 = StudentHashRecords.searchStudentwithStudentId('2020ARC55')
    # print('Grade for student Id 2020ARC55 is : ' + str(grade2020ARC55) + ' and it''s a ' + (
    #     'match' if grade2020ARC55 == 0 else 'not match'))


# Extra methods to generate data
def generateinputPS18():
    f = open('inputPS18.txt', "w+")
    y = 2010
    dept = ['CSE', 'MEC', 'ECE', 'ARC']
    while y <= 2020:
        for d in dept:
            k = 0
            cgpa = 0.0
            while k <= (20 * (y - 2010 + 1) / len(dept)):
                f.write(str(y) + str(d) + str(k) + '/' + str(cgpa) + '\n')
                k = k + 1
                cgpa = 0 if cgpa == 5 else (cgpa + 0.5)
        y = y + 1
    f.close()
