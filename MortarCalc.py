
import tkinter as tk
from tkinter import messagebox
import math


def valid_coordinate(value):
    """
    Checks whether a coordinate is a valid number
    with no more than 2 decimal places.
    """

    if not value:
        return False

    try:
        float(value)
    except ValueError:
        return False

    if "." in value:
        decimal_part = value.split(".")[1]

        if len(decimal_part) > 2:
            return False

    return True


def calculate_distance():
    """
    Gets the four coordinates, validates them,
    calculates the distance, and displays it.
    """

    mortar_x_value = mortar_x.get().strip()
    mortar_y_value = mortar_y.get().strip()
    target_x_value = target_x.get().strip()
    target_y_value = target_y.get().strip()

    coordinates = [
        ("Mortar X", mortar_x_value),
        ("Mortar Y", mortar_y_value),
        ("Target X", target_x_value),
        ("Target Y", target_y_value)
    ]

    for name, value in coordinates:
        if not valid_coordinate(value):
            messagebox.showerror(
                "Invalid Input",
                f"{name} must be a valid number "
                "with no more than 2 decimal places."
            )
            return

    # Convert input strings to floating-point numbers
    x1 = float(mortar_x_value)
    y1 = float(mortar_y_value)

    x2 = float(target_x_value)
    y2 = float(target_y_value)

    # Calculate coordinate differences
    x_result = (x1 - x2) * 100
    y_result = (y1 - y2) * 100

    # Calculate final distance
    distance = math.sqrt(
        x_result ** 2 + y_result ** 2
    )

    # Display result
    result.config(state="normal")
    result.delete(0, tk.END)
    result.insert(0, f"{distance:.2f}")
    result.config(state="readonly")


def clear_fields():
    """
    Clears all coordinate inputs and the result.
    """

    mortar_x.delete(0, tk.END)
    mortar_y.delete(0, tk.END)

    target_x.delete(0, tk.END)
    target_y.delete(0, tk.END)

    result.config(state="normal")
    result.delete(0, tk.END)
    result.config(state="readonly")

    mortar_x.focus()


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Mortar Rangefinder")
root.geometry("900x500")
root.minsize(800, 450)


# =========================================================
# MAIN LAYOUT
# =========================================================

# Left side = controls
# Right side = map

left_frame = tk.Frame(root)
left_frame.pack(
    side="left",
    fill="y",
    padx=25,
    pady=20
)


right_frame = tk.Frame(root)
right_frame.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(0, 25),
    pady=20
)


# =========================================================
# LEFT SIDE - TITLE
# =========================================================

title = tk.Label(
    left_frame,
    text="MORTAR RANGEFINDER",
    font=("Arial", 18, "bold")
)

title.pack(pady=(5, 5))


subtitle = tk.Label(
    left_frame,
    text="Calculate the distance between\n"
         "two map coordinates",
    font=("Arial", 9)
)

subtitle.pack(pady=(0, 25))


# =========================================================
# COORDINATE INPUTS
# =========================================================

coordinate_frame = tk.Frame(left_frame)

coordinate_frame.pack(fill="x")


# ---------------------------------------------------------
# Mortar position
# ---------------------------------------------------------

mortar_label = tk.Label(
    coordinate_frame,
    text="Mortar Position",
    font=("Arial", 11, "bold")
)

mortar_label.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(0, 5)
)


mortar_x_label = tk.Label(
    coordinate_frame,
    text="X:"
)

mortar_x_label.grid(
    row=1,
    column=0,
    sticky="w",
    padx=(0, 10)
)


mortar_x = tk.Entry(
    coordinate_frame,
    width=15,
    font=("Arial", 11)
)

mortar_x.grid(
    row=1,
    column=1,
    sticky="w",
    pady=3
)


mortar_y_label = tk.Label(
    coordinate_frame,
    text="Y:"
)

mortar_y_label.grid(
    row=2,
    column=0,
    sticky="w",
    padx=(0, 10)
)


mortar_y = tk.Entry(
    coordinate_frame,
    width=15,
    font=("Arial", 11)
)

mortar_y.grid(
    row=2,
    column=1,
    sticky="w",
    pady=3
)


# ---------------------------------------------------------
# Target position
# ---------------------------------------------------------

target_label = tk.Label(
    coordinate_frame,
    text="Target Position",
    font=("Arial", 11, "bold")
)

target_label.grid(
    row=3,
    column=0,
    columnspan=2,
    sticky="w",
    pady=(20, 5)
)


target_x_label = tk.Label(
    coordinate_frame,
    text="X:"
)

target_x_label.grid(
    row=4,
    column=0,
    sticky="w",
    padx=(0, 10)
)


target_x = tk.Entry(
    coordinate_frame,
    width=15,
    font=("Arial", 11)
)

target_x.grid(
    row=4,
    column=1,
    sticky="w",
    pady=3
)


target_y_label = tk.Label(
    coordinate_frame,
    text="Y:"
)

target_y_label.grid(
    row=5,
    column=0,
    sticky="w",
    padx=(0, 10)
)


target_y = tk.Entry(
    coordinate_frame,
    width=15,
    font=("Arial", 11)
)

target_y.grid(
    row=5,
    column=1,
    sticky="w",
    pady=3
)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(left_frame)

button_frame.pack(pady=25)


calculate_button = tk.Button(
    button_frame,
    text="CALCULATE",
    width=14,
    command=calculate_distance
)

calculate_button.grid(
    row=0,
    column=0,
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    width=14,
    command=clear_fields
)

clear_button.grid(
    row=0,
    column=1,
    padx=5
)


# =========================================================
# RESULT
# =========================================================

result_label = tk.Label(
    left_frame,
    text="Distance",
    font=("Arial", 11, "bold")
)

result_label.pack(pady=(0, 5))


result = tk.Entry(
    left_frame,
    width=20,
    font=("Arial", 14, "bold"),
    justify="center",
    state="readonly"
)

result.pack()



#==========================================================
# RIGHT SIDE - MAP
# =========================================================

map_frame = tk.Frame(
    right_frame,
    borderwidth=2,
    relief="groove"
)

map_frame.pack(
    fill="both",
    expand=True
)


map_label = tk.Label(
    map_frame,
    text="MAP OFFLINE",
    font=("Arial", 18, "bold")
)

map_label.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


# =========================================================
# KEYBOARD SHORTCUTS
# =========================================================

# Enter = Calculate
root.bind(
    "<Return>",
    lambda event: calculate_distance()
)

# Escape = Clear
root.bind(
    "<Escape>",
    lambda event: clear_fields()
)


# Start with Mortar X selected
mortar_x.focus()


# =========================================================
# START APPLICATION
# =========================================================

root.mainloop()

