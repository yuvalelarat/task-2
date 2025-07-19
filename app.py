import json
import os
from classify_script import classify_iam_policy

def get_json_from_input():
    print("Paste your IAM JSON policy below. End your input with an empty line:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return json.loads("\n".join(lines))

def get_json_from_file():
    files = [f for f in os.listdir('.') if f.endswith('.json')]
    if not files:
        print("No JSON files found in the current directory.")
        return None

    print("Select a JSON file from the list below:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

    while True:
        choice = input("Enter the number of the file to load: ")
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            with open(files[int(choice) - 1], 'r') as f:
                return json.load(f)
        else:
            print("Invalid choice. Try again.")

def main():
    print("Choose how to provide the IAM policy:")
    print("1. Paste JSON")
    print("2. Choose JSON file from current folder")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        policy_json = get_json_from_input()
    elif choice == '2':
        policy_json = get_json_from_file()
        if policy_json is None:
            return
    else:
        print("Invalid choice.")
        return

    result = classify_iam_policy(policy_json)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
