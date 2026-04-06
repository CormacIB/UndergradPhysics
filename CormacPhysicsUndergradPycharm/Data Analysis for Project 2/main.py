import json
import time
from datetime import datetime, timedelta
import os

DATA_FILE = "study_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    else:
        return {"sessions": [], "total_points": 0}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def start_session():
    print("Study session started. Press ENTER to stop.")
    start_time = time.time()
    input()
    end_time = time.time()

    duration = end_time - start_time
    minutes = int(duration // 60)
    seconds = int(duration % 60)
    points = int(duration // 60)  # 1 point per full minute

    session = {
        "start": datetime.fromtimestamp(start_time).isoformat(),
        "end": datetime.fromtimestamp(end_time).isoformat(),
        "duration_seconds": int(duration),
        "points_earned": points
    }

    data = load_data()
    data["sessions"].append(session)
    data["total_points"] += points
    save_data(data)

    print(f"\nSession ended. Duration: {minutes}m {seconds}s")
    print(f"Points earned: {points}")
    print(f"Total points: {data['total_points']}\n")


def view_history():
    data = load_data()
    if not data["sessions"]:
        print("No study sessions recorded yet.\n")
        return

    print("\nStudy History:")
    for i, s in enumerate(data["sessions"], start=1):
        start = datetime.fromisoformat(s["start"]).strftime('%Y-%m-%d %H:%M:%S')
        end = datetime.fromisoformat(s["end"]).strftime('%Y-%m-%d %H:%M:%S')
        mins = s["duration_seconds"] // 60
        print(f"{i}. {start} → {end} | {mins} min | {s['points_earned']} pts")

    print(f"\nTotal Points: {data['total_points']}\n")


def main():
    while True:
        print("=== Homework Tracker ===")
        print("1. Start study session")
        print("2. View history")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_session()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()
