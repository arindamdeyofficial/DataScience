class HashTable:

    # This function creates an empty hash table and points to null.
    def __init__(self):
        # creating Hashtable - nested list.
        self.hashTable = []

    def getHash(self, studentId):
        # Calculate StudentHashRecords for each record of inputPS18 file
        #YYYYAAADDDD
        #2010CSE1223
        h = 0
        for char in studentId:
            h += ord(char)
        return h % (len(self.hashTable)+1)

    def insertStudentRec(self, studentId, CGPA):
        # This function inserts the student id and correspo
        hash_key = self.getHash(studentId)
        if(len(self.hashTable) < hash_key):
            data = [[] for k in range(hash_key - len(self.hashTable))]
            self.hashTable.append(data)

        self.hashTable.append(CGPA)

    def searchStudent(self, studentId):
        hash_key = self.getHash(studentId)
        return self.hashTable[hash_key]

    def inputRead(self, filename):
        hashtbl = HashTable.HashTable()
        f = open(filename, "r")
        for i in range(10):
            hashtbl.insertStudentRec('2010MSE15', 8)
        print('CGPA for student id 2010MSE15: ' + str(v.searchStudent('2010MSE15')))

