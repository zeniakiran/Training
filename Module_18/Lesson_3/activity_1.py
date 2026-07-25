# My Daily Chore Tracker

# PART 1: Set the total chores for today
chores_total = 4
starting_chores = chores_total
print(f"You have {starting_chores} chores to complete today!\n")

# PART 2: Keep track of completed chores and the current task
finished_chores = 0
current_chore = 1

# PART 3: Continue until every chore is completed
while current_chore <= chores_total:

    # PART 4: Decide which chore to show
    if current_chore == 1:
        chore_name = "Make your bed"
    elif current_chore == 2:
        chore_name = "Feed the pet"
    elif current_chore == 3:
        chore_name = "Take out the trash"
    else:
        chore_name = "Wash the dishes"

    response = input(f"Did you finish '{chore_name}'? (yes/no): ")

    # PART 5: Move to the next chore only after finishing this one
    if response == "yes":
        finished_chores += 1
        current_chore += 1
        print("Nice work! That chore is done.")
    else:
        print("No worries! Finish it first, then try again.")

    # PART 6: Display how many chores are left
    print("Chores left:", chores_total - finished_chores)
    print()

# PART 7: This message appears after all chores are complete
print("===== CHECKLIST FINISHED! =====")
print("Awesome! You completed all your chores today!\n")

# PART 8: A safe example of an infinite loop
print("Let's look at an infinite loop example...")
number = 0
loop_counter = 0

while number <= 0:
    print("Since the condition never changes, this loop would continue forever!")
    loop_counter += 1

    if loop_counter == 3:
        print("(Stopping after 3 rounds for safety. A real infinite loop would never stop!)")
        break

# PART 9: Show the final summary
print("\n===== DAILY CHORE SUMMARY =====")
print("Total Chores:", starting_chores)
print("Completed:", finished_chores)
print("Remaining:", chores_total - finished_chores)
print("================================")