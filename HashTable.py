class HashTable:

    # This function creates an empty hash table and points to null.
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.max)]

    def getHash(self, studentId):
        # Calculate StudentHashRecords for each record of inputPS18 file 
        h = 0
        for char in studentId:
            h += ord(char)
        return h % self.MAX

    def insertStudentRec(self, studentId, CGPA):
# This function inserts the student id and correspo