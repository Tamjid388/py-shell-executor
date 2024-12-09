import os
import subprocess
import pyautogui

def save_history(command, output):
    """Save command history to a file."""
    with open("command_history.txt", "a") as file:
        file.write(f"Command: {command}\n")
        file.write(f"Output:\n{output}\n")
        file.write("-" * 50 + "\n")

def view_history():
    """Display command history."""
    if os.path.exists("command_history.txt"):
        with open("command_history.txt", "r") as file:
            history = file.read()
        if history.strip():
            pyautogui.alert(f"Command History:\n{history}")
        else:
            pyautogui.alert("No command history found.")
    else:
        pyautogui.alert("Command history file does not exist.")

def clear_history():
    """Clear command history."""
    if os.path.exists("command_history.txt"):
        os.remove("command_history.txt")
        pyautogui.alert("Command history cleared!")
    else:
        pyautogui.alert("No command history to clear.")

def execute_predefined_commands():
    """Let the user choose and execute predefined shell commands."""
    options = "1. List files in current directory\n" \
              "2. Show current directory path\n" \
              "3. Show current user\n" \
              "4. Check disk usage\n" \
              "5. Return to main menu"
    
    choice = pyautogui.prompt(f"Choose a predefined command:\n{options}")
    if choice == "1":
        command = "ls" if os.name != "nt" else "dir"
    elif choice == "2":
        command = "pwd" if os.name != "nt" else "cd"
    elif choice == "3":
        command = "whoami"
    elif choice == "4":
        command = "df -h" if os.name != "nt" else "wmic logicaldisk get size,freespace,caption"
    elif choice == "5":
        return
    else:
        pyautogui.alert("Invalid choice!")
        return

    # Execute the predefined command
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        pyautogui.alert(f"Predefined Command Output:\n{output}")
        save_history(command, output)
    except Exception as e:
        pyautogui.alert(f"Error executing command: {e}")

def execute_shell_command(command):
    """Execute a shell command and display the output in a GUI."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        pyautogui.alert(f"Command Output:\n{output}")
        save_history(command, output)
    except Exception as e:
        pyautogui.alert(f"Error executing command: {e}")

# Main program loop
while True:
    menu = "Choose an option:\n" \
           "1. Enter a shell command\n" \
           "2. View command history\n" \
           "3. Clear command history\n" \
           "4. Execute predefined commands\n" \
           "5. Exit"
    choice = pyautogui.prompt(menu)

    if not choice:
        pyautogui.alert("No option selected. Exiting...")
        break

    if choice == "1":
        # Enter a shell command
        command = pyautogui.prompt("Enter a Shell Command:")
        if not command:
            pyautogui.alert("No command entered.")
            continue
        execute_shell_command(command)

    elif choice == "2":
        # View command history
        view_history()

    elif choice == "3":
        # Clear command history
        clear_history()

    elif choice == "4":
        # Execute predefined commands
        execute_predefined_commands()

    elif choice == "5":
        # Exit program
        pyautogui.alert("Goodbye!")
        break

    else:
        pyautogui.alert("Invalid choice! Please try again.")
