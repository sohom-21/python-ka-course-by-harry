# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

subject1, subject2, subject3 = list(
    map(int, input("Enter marks of three subjects separated with a comma: ").split(",")))
total_percentage = (subject1 + subject2 + subject3) / 3
percentage_subject1 = (subject1 / 100) * 100
percentage_subject2 = (subject2 / 100) * 100
percentage_subject3 = (subject3 / 100) * 100
if ((total_percentage > 40) and (percentage_subject1 > 33) and (percentage_subject2 > 33) and (
        percentage_subject3 > 33)):
    print(
        f"you have passed with a total percentage {total_percentage} and {subject1} in subject1 and {subject2} in subject2 and {subject3} in subject3")
else:
    print("sorry you weren't able to pass")
print("the program has ended")
