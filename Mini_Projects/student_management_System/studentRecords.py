import csv
import datetime

def student(studentList):
         studentname = studentList[0]
         timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
         file_name = f"{studentname}_student_records_{timestamp}.csv"
         with open (file_name, mode='w', newline='' encoding='utf-8') as file:
                  writer = csv.writer()
                  writer.writerow(["Class","Student_name", "Roll_number","MarksObtained"])
                  writer.writerow()