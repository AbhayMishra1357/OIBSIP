#Develop a graphical BMI calculator with a user-friendly interface (GUI) using libraries like Tkinter or PyQt.
#Allow users to input weight and height, calculate BMI, and visualize the result.
#Enable data storage for multiple users, historical data viewing, and BMI trend analysis through statistics and graphs.
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Store user data (this would ideally be in a database, but for simplicity, we'll use a dictionary)
user_data = {}

def calculate_bmi():
    try:
        # Get user input
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        # Calculate BMI
        bmi = weight / (height * height)

        # Display BMI
        label_result.config(text=f"Your BMI: {bmi:.2f}")

        # Store the result for the user
        username = entry_name.get()
        if username in user_data:
            user_data[username].append(bmi)
        else:
            user_data[username] = [bmi]

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

def view_history():
    username = entry_name.get()
    if username in user_data:
        bmi_values = user_data[username]
        messagebox.showinfo("BMI History", f"BMI History for {username}: {bmi_values}")
    else:
        messagebox.showwarning("No Data", f"No data found for user: {username}")

def show_trend():
    username = entry_name.get()
    if username in user_data:
        plt.plot(user_data[username], marker='o')
        plt.title(f"BMI Trend for {username}")
        plt.xlabel("Record Number")
        plt.ylabel("BMI")
        plt.show()
    else:
        messagebox.showwarning("No Data", f"No data found for user: {username}")

# Set up the main window
root = tk.Tk()
root.title("BMI Calculator")

# User Name
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

# Weight
tk.Label(root, text="Weight (kg):").grid(row=1, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1)

# Height
tk.Label(root, text="Height (m):").grid(row=2, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1)

# Calculate Button
btn_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
btn_calculate.grid(row=3, column=1)

# Result Label
label_result = tk.Label(root, text="Your BMI: ")
label_result.grid(row=4, column=1)

# View History Button
btn_history = tk.Button(root, text="View History", command=view_history)
btn_history.grid(row=5, column=0)

# Show Trend Button
btn_trend = tk.Button(root, text="Show Trend", command=show_trend)
btn_trend.grid(row=5, column=1)

# Start the main event loop
root.mainloop()