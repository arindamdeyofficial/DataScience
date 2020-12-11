import FibonacciSeries
import powerofnumber
import recursivearraysearch
import studentgrade

print('Fibonacci: ' + str(FibonacciSeries.fibonacci(7)))
print('power: ' + str(powerofnumber.pow(2, 3)))
print('recursivearraysearch: ' + str(recursivearraysearch.arraysearch([8, 7, 0, 20, 9, 4], 4, 20)))

#HashTable.generateinputPS18()
StudentHashRecords = studentgrade.HashTable()
studentgrade.insertHashData(StudentHashRecords)
#HashTable.HashTable.searchStudent('2010CSE01')
