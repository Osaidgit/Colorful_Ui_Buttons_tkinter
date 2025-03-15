import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Colorful Buttons Example")
root.geometry("300x200")

# Function to handle button clicks
def on_button_click(color):
    print(f"{color} button clicked!")

# Create colorful buttons
button1 = tk.Button(root, text="Red Button", bg="red", fg="white", command=lambda: on_button_click("Red"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Green Button", bg="green", fg="white", command=lambda: on_button_click("Green"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Blue Button", bg="blue", fg="white", command=lambda: on_button_click("Blue"))
button3.pack(pady=10)

button4 = tk.Button(root, text="Yellow Button", bg="yellow", fg="black", command=lambda: on_button_click("Yellow"))
button4.pack(pady=10)

# Run the application
root.mainloop()
