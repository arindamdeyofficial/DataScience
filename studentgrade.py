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
    pass


# 4
def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    # implement year restriction
    stdswithgrade = StudentHashRecords.searchStudentwithCgpa(CGPAFrom, CPGATo)
    for item in stdswithgrade:
        if not (2010 <= int(item[0][0:4]) <= 2015):
            stdswithgrade.remove(item)
    return stdswithgrade


def searchStudentwithStudentId(StudentHashRecords, studentId):
    return StudentHashRecords.searchStudentwithStudentId(studentId)


def searchStudentwithCgpa(StudentHashRecords, CGPAFrom, CPGATo):
    return StudentHashRecords.searchStudentwithCgpa(CGPAFrom, CPGATo)


# 5
def depAvg(StudentHashRecords):
    studentColl = StudentHashRecords.getAll()
    # depts CSE, MEC, ECE, ARC
    maxcgpa = [0.0, 0.0, 0.0, 0.0]
    avgCgpa = [0.0, 0.0, 0.0, 0.0]
    for item in studentColl:
        dept = item[0][5:8]
        cgpa = item[1]
        if dept == 'CSE':
            maxcgpa[0] = cgpa if cgpa > maxcgpa[0] else maxcgpa[0]
            avgCgpa[0] += cgpa
        elif dept == 'MEC':
            maxcgpa[1] = cgpa if cgpa > maxcgpa[1] else maxcgpa[1]
            avgCgpa[1] += cgpa
        elif dept == 'ECE':
            maxcgpa[2] = cgpa if cgpa > maxcgpa[2] else maxcgpa[2]
            avgCgpa[2] += cgpa
        elif dept == 'ARC':
            maxcgpa[3] = cgpa if cgpa > maxcgpa[3] else maxcgpa[3]
            avgCgpa[4] += cgpa
        avgCgpa[:] = [x / len(studentColl) for x in studentColl]


def getnewCourseList(StudentHashRecords):
    cgpafrom, cgpato = getCourseListRange()
    eligibleStudents = newCourseList(StudentHashRecords, cgpafrom, cgpato)
    contentToWrite = f'---------- new course candidates ----------\nInput: {cgpafrom}:{cgpato}\nTotal eligible students: {len(eligibleStudents)}' \
                     f'\nQualified students:\n'
    for item in eligibleStudents:
        contentToWrite += item[0] + '/' + str(item[1]) + '\n'
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
        self.hashTable = []

    def getHash(self, studentId):
        # Calculate StudentHashRecords for each record of inputPS18 file
        # YYYYAAADDDD
        # 2010CSE1223
        h = 0
        for char in studentId:
            h += ord(char)
        return h % (len(self.hashTable) + 1)

    def insertStudentRec(self, studentId, CGPA):
        # This function inserts the student id
        hash_key = self.getHash(studentId)
        if len(self.hashTable) < hash_key:
            self.hashTable.append([[] for k in range(hash_key - len(self.hashTable))])
        self.hashTable.append([studentId, CGPA])

    def searchStudentwithStudentId(self, studentId):
        hash_key = self.getHash(studentId)
        return self.hashTable[hash_key]

    def searchStudentwithCgpa(self, CGPAFrom, CPGATo):
        studentColl = []
        for item in self.hashTable:
            if (item[1] is not None) and (CGPAFrom <= item[1] <= CPGATo):
                studentColl.append(item)
        return studentColl

    def destroyHash(self):
        self.hashTable = []

    def getAll(self):
        studentColl = []
        for item in self.hashTable:
            if item[1] is not None:
                studentColl.append(item)
        return studentColl


# Extra methods to generate data
def generateinputPS18():
    f = open('inputPS18.txt', "w+")
    y = 2010
    dept = ['CSE', 'MEC', 'ECE', 'ARC']
    while y <= 2014:
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
