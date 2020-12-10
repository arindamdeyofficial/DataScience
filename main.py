import FibonacciSeries
import powerofnumber
import recursivearraysearch
import HashTable

print('Fibonacci: ' + str(FibonacciSeries.fibonacci(7)))
print('power: ' + str(powerofnumber.pow(2, 3)))
print('recursivearraysearch: ' + str(recursivearraysearch.arraysearch([8, 7, 0, 20, 9, 4], 4, 20)))
v = HashTable.HashTable()
v.insertStudentRec('2010CSE12', 4.5)
v.insertStudentRec('2010CSE15', 4)
v.insertStudentRec('2010ARC12', 4.5)
v.insertStudentRec('2010ARC15', 4)
v.insertStudentRec('2010MSE12', 4.5)
v.insertStudentRec('2010MSE15', 4)
v.insertStudentRec('2010MSE15', 8)
print('CGPA for student id 2010MSE15: ' + str(v.searchStudent('2010MSE15')))