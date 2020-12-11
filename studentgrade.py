def insertHashData(StudentHashRecords):
    f = open('inputPS18.txt', "r")
    while f.readable():
        rec = f.readline().split('/')
        if rec == ['']:
            break
        insertStudentRec(StudentHashRecords, rec[0], rec[1])
    f.close()


# 2
def insertStudentRec(StudentHashRecords, studentId, CGPA):
    StudentHashRecords.insertStudentRec(studentId, CGPA)


def searchStudent(StudentHashRecords, studentId):
    hash_key = HashTable.getHash(studentId)
    return HashTable.hashTable[hash_key]


# 3
def hallOfFame(StudentHashRecords):
    pass


def depAvg(self):
    pass


def newCourseList(StudentHashRecords, CGPAFrom, CPGATo):
    pass


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
        self.hashTable.append(CGPA)

    def destroyHash(self):
        self.hashTable = []


# Extra methods to generate data
def inputRead(filename):
    hashtbl = HashTable()
    f = open(filename, "r")
    f.readline()
    while f.readable():
        rec = f.readline().split(',')
        hashtbl.insertStudentRec(rec[0], rec[1])
    print('CGPA for student id 2010MSE15: ' + str(hashtbl.searchStudent('2010MSE15')))
    f.close()


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


def generateoutputPS18(eligiblestudents):
    f = open('outputPS18.txt', "w+")
    f.write('---------- hall of fame ----------\n')
    f.write('Total eligible students:' + len(eligiblestudents) + '\n')
    f.write('Qualified students:\n')
    for s in eligiblestudents:
        f.write(eligiblestudents[0] + '/' + eligiblestudents[1])
    f.write('-------------------------------------\n---------- new course candidates ----------\n')
    f.close()


def generatepromptsPS18():
    f = open('promptsPS18.txt', "w+")
    f.write('hallOfFame:\n')
    f.write('courseOffer:\n')
    f.close()
