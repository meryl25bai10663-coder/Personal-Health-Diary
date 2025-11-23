import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from getpass import getpass

DATA_FILE = 'health_diary.csv'
USER_FILE = 'users.csv'

# --------------------- User Management ---------------------
def register():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    try:
        users = pd.read_csv(USER_FILE)
        if username in users.username.values:
            print("Username already exists!")
            return None
    except FileNotFoundError:
        users = pd.DataFrame(columns=['username', 'password'])
    users.loc[len(users)] = [username, password]
    users.to_csv(USER_FILE, index=False)
    print("Registration successful!")
    return username

def login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    try:
        users = pd.read_csv(USER_FILE)
        if ((users.username == username) & (users.password == password)).any():
            print(f"Welcome, {username}!")
            return username
        else:
            print("Login failed!")
            return None
    except FileNotFoundError:
        print("No users registered yet!")
        return None

# --------------------- Data Entry ---------------------
def add_entry(username):
    date = input("Date (YYYY-MM-DD) [default: today]: ") or pd.Timestamp.today().strftime('%Y-%m-%d')
    diet = input("Diet (summary): ")
    calories = input("Calories: ")
    exercise = input("Exercise (activity/duration): ")
    sleep = input("Sleep (hours): ")
    mood = input("Mood: ")

    row = {
        "username": username,
        "date": date,
        "diet": diet,
        "calories": calories,
        "exercise": exercise,
        "sleep": sleep,
        "mood": mood
    }
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=row.keys())
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    print("Entry added!")

# --------------------- Analytics and Report ---------------------
def show_report(username):
    try:
        df = pd.read_csv(DATA_FILE)
        user_df = df[df.username == username]
    except FileNotFoundError:
        print("No diary entries found!")
        return
    if user_df.empty:
        print("No entries for user!")
        return

    print("\nRecent Entries:")
    print(user_df.tail(7)[['date', 'diet', 'calories', 'exercise', 'sleep', 'mood']])
    
    sleep_data = pd.to_numeric(user_df['sleep'], errors='coerce').dropna()
    if not sleep_data.empty:
        avg_sleep = sleep_data.mean()
        print(f"\nAverage Sleep (last {len(sleep_data)} entries): {avg_sleep:.2f} hours/night")
        if avg_sleep < 7:
            print("Tip: Try to increase your sleep for better health!")
        else:
            print("Great job maintaining healthy sleep!")

# --------------------- Visualization ---------------------
def plot_sleep(username):
    try:
        df = pd.read_csv(DATA_FILE)
        user_df = df[df.username == username]
    except FileNotFoundError:
        print("No diary entries found!")
        return
    if user_df.empty:
        print("No entries for user!")
        return

    user_df = user_df.copy()
    user_df['sleep'] = pd.to_numeric(user_df['sleep'], errors='coerce')
    user_df = user_df.dropna(subset=['sleep'])
    
    plt.figure(figsize=(8,4))
    plt.plot(pd.to_datetime(user_df['date']), user_df['sleep'], marker='o')
    plt.title('Sleep Trends')
    plt.xlabel('Date')
    plt.ylabel('Sleep Hours')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --------------------- Predictive Tool ---------------------
def predict_sleep_quality(username):
    try:
        df = pd.read_csv(DATA_FILE)
        user_df = df[df.username == username]
    except FileNotFoundError:
        print("No diary entries found!")
        return
    if user_df.empty:
        print("No entries for user!")
        return

    sleep_data = pd.to_numeric(user_df['sleep'], errors='coerce').dropna()
    if len(sleep_data) < 3:
        print("Not enough data for prediction!")
        return
    avg = np.mean(sleep_data[-7:])  # last 7 entries
    print(f"Predicted sleep quality (last week): {'Poor' if avg < 7 else 'Good'}")
    if avg < 7:
        print("Motivation: Prioritize your rest this coming week!")

# --------------------- Main Application ---------------------
def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            username = register()
        elif choice == '2':
            username = login()
            if username:
                while True:
                    print("\n1. Add entry\n2. View report\n3. Visualize sleep\n4. Predict sleep quality\n5. Logout")
                    c = input("Choice: ")
                    if c == '1':
                        add_entry(username)
                    elif c == '2':
                        show_report(username)
                    elif c == '3':
                        plot_sleep(username)
                    elif c == '4':
                        predict_sleep_quality(username)
                    elif c == '5':
                        break
        elif choice == '3':
            break

if __name__ == '__main__':
    main()
