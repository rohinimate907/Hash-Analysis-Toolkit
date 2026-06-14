from datetime import datetime


def save_to_history(action, data):
    with open(
    "scan_results.txt",
    "r",
    encoding="utf-8"
) as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write(f"Date: {datetime.now()}\n")
        file.write(f"Action: {action}\n")
        file.write(f"Data: {data}\n")


def view_history():
    try:
        with open("scan_results.txt", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("No History Found")


def clear_history():
    open("scan_results.txt", "w").close()