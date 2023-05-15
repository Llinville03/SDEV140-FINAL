import tkinter as tk

class CalorieTrackerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calorie Tracker")
        self.remaining_calories = 0
        self.daily_calories = None

        # Create input widgets for daily calorie intake and calorie goal
        self.calorie_intake_label = tk.Label(master, text="Daily Calorie Intake:")
        self.calorie_intake_label.grid(row=0, column=0)
        self.calorie_intake_entry = tk.Entry(master)
        self.calorie_intake_entry.grid(row=0, column=1)

        self.calorie_goal_label = tk.Label(master, text="Calorie Goal:")
        self.calorie_goal_label.grid(row=1, column=0)
        self.calorie_goal_entry = tk.Entry(master)
        self.calorie_goal_entry.grid(row=1, column=1)

        # Create a button to submit the daily calorie intake
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_calories)
        self.submit_button.grid(row=2, column=0, columnspan=2)

        # Create a label to display the daily calorie intake and remaining calories
        self.calorie_display_label = tk.Label(master, text="")
        self.calorie_display_label.grid(row=3, column=0, columnspan=2)

        # Create a menu bar with two menu items
        self.menu_bar = tk.Menu(master)
        self.menu_bar.add_command(label="View Progress", command=self.open_progress_chart)
        self.menu_bar.add_command(label="View Recommendations", command=self.open_recommendations)
        master.config(menu=self.menu_bar)

    def submit_calories(self):
        # Get the daily calorie intake and calorie goal from the input widgets
        calorie_intake = self.calorie_intake_entry.get()
        calorie_goal = self.calorie_goal_entry.get()
        self.daily_calories = calorie_intake
        # Check if the input is valid
        if not calorie_intake or not calorie_goal:
            tk.messagebox.showwarning("Invalid Input", "Please enter a value for both calorie intake and goal.")
            return
        try:
            calorie_intake = float(calorie_intake)
            calorie_goal = float(calorie_goal)
        except ValueError:
            tk.messagebox.showwarning("Invalid Input", "Please enter numeric values for calorie intake and goal.")
            return

        # Calculate the remaining calories and update the display label
        self.remaining_calories = calorie_goal - calorie_intake
        self.calorie_display_label.config(text=f"Calories: {calorie_intake} | Remaining: {self.remaining_calories}")
       

    def open_progress_chart(self):
        # Create a new window to display progress information
        progress_window = tk.Toplevel(self.master)
        progress_window.title("Progress Chart")

        # Add a back button to return to the main window
        back_button = tk.Button(progress_window, text="Back", command=progress_window.destroy)
        back_button.pack()

        # Add a label to the progress window
        progress_label = tk.Label(progress_window, text=f"Here is your progress chart!\n\nDaily Calorie Intake: {self.daily_calories}")
        progress_label.pack()

        # Add a label to display the remaining calories
        if self.remaining_calories is not None:
            remaining_label = tk.Label(progress_window, text=f"Remaining Calories: {self.remaining_calories}")
            remaining_label.pack()


    def open_recommendations(self):
        # Create a new window to display recommendations
        recommendations_window = tk.Toplevel(self.master)
        recommendations_window.title("Recommendations")

        # Add a back button to return to the main window
        back_button = tk.Button(recommendations_window, text="Back", command=recommendations_window.destroy)
        back_button.pack()

        # Add a label to the recommendations window
        recommendations_label = tk.Label(recommendations_window, text="Here are some personalized recommendations!")
        recommendations_label.pack()

# Create the main window
root = tk.Tk()

# Create an instance of the CalorieTracker class and start the main loop
app = CalorieTrackerGUI(root)
root.mainloop()
