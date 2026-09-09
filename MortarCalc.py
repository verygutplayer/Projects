```python
import tkinter as tk
from tkinter import messagebox
import math


def valid_coordinate(value):
    """
    Checks whether a coordinate is a valid number
    with no more than 2 decimal places.
    """

    # Empty input
    if not value:
        return False

    # Try converting to a float
    try:
        float(value)
    except ValueError:
        return False

    # Check decimal places
    if "." in value:
        decimal_part = value.split(".")[1]

        if len(decimal_part) > 2:
            return False

    return True


def calculate_distance():
    """
    Gets the four coordinates, validates them,
    calculates the mortar distance, and displays it.
    """

    # Get values from the input boxes
    mortar_x_value = mortar_x.get().strip()
    mortar_y_value = mortar_y.get().strip()
    target_x_value = target_x.get().strip()
    target_y_value = target_y.get().strip()

    # Validate all four inputs
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

    # Convert strings to floating point numbers
    x1 = float(mortar_x_value)
    y1 = float(mortar_y_value)

    x2 = float(target_x_value)
    y2 = float(target_y_value)

    # Calculate the difference between the coordinates
    #
    # Multiplying by 100 converts the coordinate
    # difference into the desired rangefinder units.
    x_result = (x1 - x2) * 100
    y_result = (y1 - y2) * 100

    # Calculate the distance using the Pythagorean theorem
    #
    # Squaring the values automatically removes
    # any negative sign.
    distance = math.sqrt(
        x_result ** 2 + y_result ** 2
    )

    # Display the result
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


# ---------------------------------------------------------
# Main window
# ---------------------------------------------------------

root = tk.Tk()

root.title("Mortar Rangefinder")
root.geometry("430x420")
root.resizable(False, False)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

title = tk.Label(
    root,
    text="MORTAR RANGEFINDER",
    font=("Arial", 18, "bold")
)

title.pack(pady=(20, 5))


subtitle = tk.Label(
    root,
    text="Calculate the distance between two map coordinates",
    font=("Arial", 9)
)

subtitle.pack(pady=(0, 20))


# ---------------------------------------------------------
# Coordinate input frame
# ---------------------------------------------------------

coordinate_frame = tk.Frame(root)

coordinate_frame.pack(padx=30, fill="x")


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


# Mortar X

mortar_x_label = tk.Label(
    coordinate_frame,
    text="X:"
)

mortar_x_label.grid(
    row=1,
    column=0,
    sticky="w",
    padx=(0, 5)
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


# Mortar Y

mortar_y_label = tk.Label(
    coordinate_frame,
    text="Y:"
)

mortar_y_label.grid(
    row=2,
    column=0,
    sticky="w",
    padx=(0, 5)
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


# Target X

target_x_label = tk.Label(
    coordinate_frame,
    text="X:"
)

target_x_label.grid(
    row=4,
    column=0,
    sticky="w",
    padx=(0, 5)
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


# Target Y

target_y_label = tk.Label(
    coordinate_frame,
    text="Y:"
)

target_y_label.grid(
    row=5,
    column=0,
    sticky="w",
    padx=(0, 5)
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


# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------

button_frame = tk.Frame(root)

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


# ---------------------------------------------------------
# Result
# ---------------------------------------------------------

result_label = tk.Label(
    root,
    text="Distance",
    font=("Arial", 11, "bold")
)

result_label.pack(pady=(0, 5))


result = tk.Entry(
    root,
    width=20,
    font=("Arial", 14, "bold"),
    justify="center",
    state="readonly"
)

result.pack()


# ---------------------------------------------------------
# Keyboard shortcuts
# ---------------------------------------------------------

# Enter = Calculate
root.bind("<Return>", lambda event: calculate_distance())

# Escape = Clear
root.bind("<Escape>", lambda event: clear_fields())


# Put cursor in the first input when application starts
mortar_x.focus()


# ---------------------------------------------------------
# Start application
# ---------------------------------------------------------

root.mainloop()
```
