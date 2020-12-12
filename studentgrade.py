def insertHashData(StudentHashRecords):
    f = open('inputPS18.txt', "r")
    while f.readable():
        rec = f.readline().split('/')
        if rec == ['']:
            break
        insertStudentRec(StudentHashRecords, rec[0], float(rec[1].rstrip("\n")))
    f.close()


# 2
def insertStudentRec(StudentHashRecords, studentId, CGPA):
    StudentHashRecords.insertStudentRec(studentId, CGPA)


# 3
def hallOfFame(StudentHashRecords):
    # Input file will be promptsPS18.txt and tag will be "hallOfFame:"
    # return list of passout students who have topped their department in there grad year, append in outputPS18.txt file
    pass


# 4
def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    # implement year restriction
    stdswithgrade = StudentHashRecords.searchStudentwithCgpa(CGPAFrom, CPGATo)
    for item in stdswithgrade:
        if not (2015 <= int(item[0][0:4]) <= 2019):
            stdswithgrade.remove(item)
    return stdswithgrade


def searchStudentwithStudentId(StudentHashRecords, studentId):
    return StudentHashRecords.searchStudentwithStudentId(studentId)


def searchStudentwithCgpa(StudentHashRecords, CGPAFrom, CPGATo):
    return StudentHashRecords.searchStudentwithCgpa(CGPAFrom, CPGATo)


# 5
def depAvg(StudentHashRecords):
    maxcgpa, avgCgpa = StudentHashRecords.depAvg()
    contentToWrite = '---------- department CGPA ----------\nCSE: max: ' + maxcgpa[0] + ', avg: ' + avgCgpa[0] + '\n' \
                                                                                                                 'ECE: max: ' + \
                     maxcgpa[1] + ', avg: ' + avgCgpa[1] + '\n' \
                                                           'ECE: max: ' + maxcgpa[2] + ', avg: ' + avgCgpa[2] + '\n' \
                                                                                                                'ARC: max: ' + \
                     maxcgpa[3] + ', avg: ' + avgCgpa[3] + '\n' \
                                                           '\n-------------------------------------\n'
    generateoutputPS18(contentToWrite)


def getnewCourseList(StudentHashRecords):
    cgpafrom, cgpato = getCourseListRange()
    eligibleStudents = newCourseList(StudentHashRecords, cgpafrom, cgpato)
    contentToWrite = f'---------- new course candidates ----------\nInput: {cgpafrom}:{cgpato}\nTotal eligible students: {len(eligibleStudents)}' \
                     f'\nQualified students:\n'
    for item in eligibleStudents:
        contentToWrite += item[0] + '/' + str(item[1]) + '\n-------------------------------------\n'
    generateoutputPS18(contentToWrite)


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

    def searchStudentwithStudentId(self, studentId):
        hash_key = self.getHash(studentId)
        eleatIndex = self.hashTable[hash_key]
        if eleatIndex is not None:
            for item in eleatIndex:
                if item[0] == studentId:
                    return item[1]

    def searchStudentwithCgpa(self, CGPAFrom, CPGATo):
        studentColl = []
        for item in self.hashTable:
            if item is not None:
                for student in item:
                    if CGPAFrom <= student[1] <= CPGATo:
                        studentColl.append(student)
        return studentColl

    def destroyHash(self):
        self.hashTable = []

    def depAvg(self):
        studentColl = self.hashTable()
        # depts CSE, MEC, ECE, ARC
        maxcgpa = [0.0, 0.0, 0.0, 0.0]
        avgCgpa = [0.0, 0.0, 0.0, 0.0]
        for item in studentColl:
            if item is None:
                continue
            dept = item[0][5:8]
            cgpa = item[1]
            if dept == 'CSE':
                if cgpa > maxcgpa[0]:
                    maxcgpa[0] = cgpa
                avgCgpa[0] += cgpa
            elif dept == 'MEC':
                if cgpa > maxcgpa[1]:
                    maxcgpa[1] = cgpa
                avgCgpa[1] += cgpa
            elif dept == 'ECE':
                if cgpa > maxcgpa[2]:
                    maxcgpa[2] = cgpa
                avgCgpa[2] += cgpa
            elif dept == 'ARC':
                if cgpa > maxcgpa[3]:
                    maxcgpa[3] = cgpa
                avgCgpa[4] += cgpa
            avgCgpa[:] = [x / len(studentColl) for x in avgCgpa]
            return maxcgpa, avgCgpa

    def getAll(self):
        studentColl = []
        for item in self.hashTable:
            if item is not None:
                for student in item:
                    studentColl.append(student)
        return studentColl

    def display_all(self):
        for item in self.hashTable:
            if item is not None:
                for student in item:
                    print('Student Id: ' + student[0] + ' CGPA: ' + student[1])


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


def generateoutputPS18(content):
    f = open('outputPS18.txt', "a")
    f.write(content + '\n')
    f.close()


if __name__ == "__main__":
    # studentgrade.generateinputPS18()
    StudentHashRecords = HashTable()
    insertHashData(StudentHashRecords)
    getnewCourseList(StudentHashRecords)

    # Unit tests
    grade2019ECE3 = searchStudentwithStudentId(StudentHashRecords, '2019ECE3')
    print('Grade for student Id 2019ECE3 is : ' + str(grade2019ECE3) + ' and it''s a ' + ('match' if grade2019ECE3 == 1.5 else 'not match'))

    grade2010ECE0 = searchStudentwithStudentId(StudentHashRecords, '2010ECE0')
    print('Grade for student Id 2010ECE0 is : ' + str(grade2010ECE0) + ' and it''s a ' + (
        'match' if grade2010ECE0 == 0.0 else 'not match'))

    grade2011ECE7 = searchStudentwithStudentId(StudentHashRecords, '2011ECE7')
    print('Grade for student Id 2011ECE7 is : ' + str(grade2011ECE7) + ' and it''s a ' + (
        'match' if grade2011ECE7 == 3.5 else 'not match'))

    grade2011ARC10 = searchStudentwithStudentId(StudentHashRecords, '2011ARC10')
    print('Grade for student Id 2011ARC10 is : ' + str(grade2011ARC10) + ' and it''s a ' + (
        'match' if grade2011ARC10 == 5.0 else 'not match'))

    grade2019MEC35 = searchStudentwithStudentId(StudentHashRecords, '2019MEC35')
    print('Grade for student Id 2019MEC35 is : ' + str(grade2019MEC35) + ' and it''s a ' + (
        'match' if grade2019MEC35 == 1.0 else 'not match'))

    grade2020ARC55 = searchStudentwithStudentId(StudentHashRecords, '2020ARC55')
    print('Grade for student Id 2020ARC55 is : ' + str(grade2020ARC55) + ' and it''s a ' + (
        'match' if grade2020ARC55 == 0 else 'not match'))



