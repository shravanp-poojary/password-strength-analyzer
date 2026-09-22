import tkinter as tk
from tkinter import messagebox
import string


def analyze_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        length_result.config(text="✓ Length: Good")
        score += 1
    else:
        length_result.config(text="✗ Length: Too short")
        suggestions.append("Use at least 8 characters.")

    # Lowercase check
    if any(c.islower() for c in password):
        lowercase_result.config(text="✓ Lowercase: Yes")
        score += 1
    else:
        lowercase_result.config(text="✗ Lowercase: No")
        suggestions.append("Add lowercase letters.")

    # Uppercase check
    if any(c.isupper() for c in password):
        uppercase_result.config(text="✓ Uppercase: Yes")
        score += 1
    else:
        uppercase_result.config(text="✗ Uppercase: No")
        suggestions.append("Add uppercase letters.")

    # Number check
    if any(c.isdigit() for c in password):
        number_result.config(text="✓ Number: Yes")
        score += 1
    else:
        number_result.config(text="✗ Number: No")
        suggestions.append("Add numbers.")

    # Special character check
    if any(c in string.punctuation for c in password):
        special_result.config(text="✓ Special Character: Yes")
        score += 1
    else:
        special_result.config(text="✗ Special Character: No")
        suggestions.append("Add special characters.")

    # Strength calculation
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    strength_result.config(
        text="Password Strength: " + strength
    )

    # Suggestions
    if suggestions:
        suggestion_text = "\n".join(
            "• " + suggestion for suggestion in suggestions
        )
    else:
        suggestion_text = "✓ Password satisfies all basic checks."

    suggestions_result.config(text=suggestion_text)


def clear_password():
    password_entry.delete(0, tk.END)

    length_result.config(text="")
    lowercase_result.config(text="")
    uppercase_result.config(text="")
    number_result.config(text="")
    special_result.config(text="")
    strength_result.config(text="")
    suggestions_result.config(text="")


# Main window
window = tk.Tk()

window.title("Password Strength Analyzer")
window.geometry("600x650")
window.resizable(False, False)


# Title
title = tk.Label(
    window,
    text="Password Strength Analyzer",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)


description = tk.Label(
    window,
    text="Check the strength of your password",
    font=("Arial", 11)
)

description.pack()


# Password label
password_label = tk.Label(
    window,
    text="Enter Password:",
    font=("Arial", 12, "bold")
)

password_label.pack(pady=(25, 5))


# Password input
password_entry = tk.Entry(
    window,
    width=40,
    show="*",
    font=("Arial", 14)
)

password_entry.pack()


# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)


check_button = tk.Button(
    button_frame,
    text="Check Password",
    command=analyze_password,
    font=("Arial", 11, "bold")
)

check_button.grid(row=0, column=0, padx=5)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_password,
    font=("Arial", 11)
)

clear_button.grid(row=0, column=1, padx=5)


# Security checks
results_label = tk.Label(
    window,
    text="Security Checks",
    font=("Arial", 16, "bold")
)

results_label.pack(pady=15)


length_result = tk.Label(window, font=("Arial", 11))
length_result.pack(anchor="w", padx=150)

lowercase_result = tk.Label(window, font=("Arial", 11))
lowercase_result.pack(anchor="w", padx=150)

uppercase_result = tk.Label(window, font=("Arial", 11))
uppercase_result.pack(anchor="w", padx=150)

number_result = tk.Label(window, font=("Arial", 11))
number_result.pack(anchor="w", padx=150)

special_result = tk.Label(window, font=("Arial", 11))
special_result.pack(anchor="w", padx=150)


# Strength result
strength_result = tk.Label(
    window,
    text="",
    font=("Arial", 16, "bold")
)

strength_result.pack(pady=20)


# Suggestions
suggestions_title = tk.Label(
    window,
    text="Suggestions",
    font=("Arial", 14, "bold")
)

suggestions_title.pack()


suggestions_result = tk.Label(
    window,
    text="",
    font=("Arial", 10),
    justify="left",
    wraplength=450
)

suggestions_result.pack(pady=10)


window.mainloop()