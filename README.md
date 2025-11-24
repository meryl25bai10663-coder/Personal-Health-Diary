Personal Health Diary
This project is a simple Python program for tracking and reviewing daily health data (weight, steps, calorie intake, sleep hours) over a week.
It uses pandas and numpy for data handling and calculations, and demonstrates the use of control statements (if-else, while, for).
________________________________________
Features
•	Interactive daily entry: Logs weight, steps, calories, and sleep for each day.
•	Daily feedback: Immediate advice based on steps and sleep (using if-else).
•	Weekly summary: Calculates averages and totals using numpy.
•	Calorie intake advice: Checks each day's calories using a for loop.
•	Data export: Saves your diary as a CSV file.
________________________________________
How to Run
1.	Prerequisites
o	Python 3.x installed.
o	pandas and numpy libraries installed:
                                                   pip install pandas numpy
2.	Run the Program
o	Copy the code into a .py file (e.g., health_diary.py)
o	Run in your terminal or IDE:
                                                   python health_diary.py
o	Enter your health data when prompted for each of the 7 days.
3.	Output
o	At the end, view your weekly summary in the console.
o	Find a CSV file named my_health_diary.csv containing your data.

Program Structure
•	while loop: Repeats entry for each day.
•	if-else: Gives personalized feedback after each entry.
•	for loop: Analyses weekly calorie intake.
•	pandas: Stores and saves diary entries.
•	numpy: Calculates averages and totals.
________________________________________
Example Output: 
--- Day 1 ---
Enter your weight (kg): 65
Enter your steps: 8000
Enter your calories intake: 2100
Enter your sleep hours: 7.5
Good effort. Stay active!
Your sleep is adequate.
...
=== Weekly Summary ===
Average Weight: 65.50 kg
Total Steps: 56000
Average Calories Intake: 2200.0
Average Sleep: 7.2 hrs
Day 3: Try to reduce calorie intake.
Your health diary has been saved as 'my_health_diary.csv'.

Customization
•	Change n_days for a different diary duration.
•	Adjust feedback messages or thresholds as needed.

License
This project is free to use and modify for personal or educational purposes.
