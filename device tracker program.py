# Simple Digital Device Tracker

def run_tracker():
    print("Welcome to the Digital Device Usage Tracker!")
    print("Track your daily usage for better digital wellness.\n")
    print("👉 Tip: You can type 'q' anytime to quit.\n")

    devices = ["iPhone", "iPad", "Mac", "Apple Watch"]
    usage = {}

    # Usage inputs hours for each device
    for device in devices:
        user_input = input(f"How many hours did you use your {device} today (0 - 24, or 'q' to quit): ").strip().lower()
        if user_input in ["q", "quit"]:
            print("\n❌ Program stopped by user. Goodbye!")
            exit()
        try:
            hours = float(user_input)
            if hours < 0:
                print("❌ Negative hours are not allowed. Program ending.")
                exit()
            elif hours > 24:
                print("❌ Hours cannot exceed 24 in a day. Program ending.")
                exit()
            else:
                usage[device] = hours
        except ValueError:
            print("❌ Invalid input. Please enter a number (e.g., 3 or 2.5). Program ending.")
            exit()

    total_hours = sum(usage.values())

    # Display result in table
    print("\nYour Daily Report:")
    print("=" * 30)
    print(f"{'Device':<15}{'Hours Used':>10}")
    print("-" * 30)
    for device, hours in usage.items():
        print(f"{device:<15}{hours:>10.2f}")
    print("-" * 30)
    print(f"{'Total':<15}{total_hours:>10.2f}")
    print("=" * 30)

    # Provide feedback
    print()
    if total_hours > 8:
        print("⚠️ You spent more than 8 hours on devices today. Consider taking breaks!\n")
    elif 4 <= total_hours <= 8:
        print("✅ Your usage is moderate. Keep a healthy balance!\n")
    else:
        print("🌿 Great job! You had low screen time today.\n")


def main():
    while True:
        run_tracker()

        # Ask user if they want to run again
        choice = input("Do you want to track again? (yes/y/no/n): ").strip().lower()
        
        if choice in ["yes", "y"]:
            continue
        elif choice in ["no", "n"]:
            print("\n🙏 Thank you for using me! Goodbye.")
            break
        else:
            print("Invalid input. Please type yes, y, no, or n.\n")


if __name__ == "__main__":
    main()
