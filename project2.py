import pandas as pd
import numpy as np

# Initialize empty diary DataFrame
diary_df = pd.DataFrame(columns=['Day', 'Weight (kg)', 'Steps', 'Calories', 'Sleep (hrs)'])

# Number of days to record (e.g., a week)
n_days = 7
day = 1

while day <= n_days:
    print(f"--- Day {day} ---")
    weight = float(input("Enter your weight (kg): "))
    steps = int(input("Enter your steps: "))
    calories = int(input("Enter your calories intake: "))
    sleep = float(input("Enter your sleep hours: "))
    
    diary_df = pd.concat([diary_df, pd.DataFrame({
        'Day': [day],
        'Weight (kg)': [weight],
        'Steps': [steps],
        'Calories': [calories],
        'Sleep (hrs)': [sleep]
    })], ignore_index=True)
    
    # Give daily feedback using if-else
    if steps < 5000:
        print("Try to walk more for better health.")
    elif steps >= 10000:
        print("Great job on your steps!")
    else:
        print("Good effort. Stay active!")
    
    if sleep < 6:
        print("Consider getting more sleep.")
    elif sleep >= 8:
        print("Excellent sleep routine!")
    else:
        print("Your sleep is adequate.")
        
    day += 1

# Use numpy to calculate and print weekly statistics
weights = np.array(diary_df['Weight (kg)'], dtype=float)
avg_weight = np.mean(weights)
steps = np.array(diary_df['Steps'], dtype=int)
total_steps = np.sum(steps)
avg_calories = np.mean(np.array(diary_df['Calories'], dtype=int))
avg_sleep = np.mean(np.array(diary_df['Sleep (hrs)'], dtype=float))

print(f"\n=== Weekly Summary ===")
print(f"Average Weight: {avg_weight:.2f} kg")
print(f"Total Steps: {total_steps}")
print(f"Average Calories Intake: {avg_calories:.1f}")
print(f"Average Sleep: {avg_sleep:.1f} hrs")

# For loop to give personalized weekly health tip
for i in range(n_days):
    if diary_df.iloc[i]['Calories'] > 2500:
        print(f"Day {int(diary_df.iloc[i]['Day'])}: Try to reduce calorie intake.")

# Save diary to CSV
diary_df.to_csv('my_health_diary.csv', index=False)
print("\nYour health diary has been saved as 'my_health_diary.csv'.")
