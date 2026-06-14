import tkinter as tk
# Step 9: Connected Backend Imports
from hash_identifier import identify_hash
from hash_generator import generate_hashes

# Step 1 & 2: Base Window Setup
root = tk.Tk()
root.title("Hash Identifier Tool")
root.geometry("820x680") # Slightly modified window bounds for optimal padding
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Step 19: Statistics Counters
identify_count = 0
generate_count = 0


# =====================================================================
# BACKEND LOGIC & UTILITY FUNCTIONS
# =====================================================================

# Step 7, 19 & Enhancement 2: Identify Function with Read-Only Lock
def identify():
    global identify_count
    
    hash_value = hash_entry.get().strip()
    
    # Temporarily enable state to modify contents
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)

    possible_types, security = identify_hash(hash_value)

    if possible_types is None:
        result_box.insert(tk.END, "Invalid Hash Format")
        result_box.config(state="disabled")
        status_label.config(text="Error: Invalid Hash Format")
        return

    if not possible_types:
        result_box.insert(tk.END, "Unknown Hash Type")
        result_box.config(state="disabled")
        status_label.config(text="Error: Unknown Hash Type")
        return

    # Increment counter and update stats label
    identify_count += 1
    stats_label.config(text=f"Identified: {identify_count} | Generated: {generate_count}")

    # Populating the result box with Bold Formatting
    result_box.insert(tk.END, "==================================================\n")
    result_box.insert(tk.END, "               HASH ANALYSIS REPORT               \n")
    result_box.insert(tk.END, "==================================================\n\n")
    result_box.insert(tk.END, f"Hash Length : {len(hash_value)}\n\n")
    result_box.insert(tk.END, "Possible Hash Types:\n")

    for h in possible_types:
        result_box.insert(tk.END, f"• {h}\n")

    result_box.insert(tk.END, "\nSecurity Analysis:\n")

    for h, level in security:
        result_box.insert(tk.END, f"• {h} → {level}\n")
        
    # Lock widget state to Read-Only
    result_box.config(state="disabled")
    status_label.config(text="Hash Identified Successfully")


# Step 11, 19 & Enhancement 2: Generate Function with Read-Only Lock
def generate():
    global generate_count
    
    text = text_entry.get().strip()
    
    # Temporarily enable state to modify contents
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)

    if not text:
        result_box.insert(tk.END, "Please Enter Some Text")
        result_box.config(state="disabled")
        status_label.config(text="Error: Please Enter Some Text")
        return

    # Increment counter and update stats label
    generate_count += 1
    stats_label.config(text=f"Identified: {identify_count} | Generated: {generate_count}")

    hashes = generate_hashes(text)

    result_box.insert(tk.END, "==================================================\n")
    result_box.insert(tk.END, "                GENERATED HASHES                  \n")
    result_box.insert(tk.END, "==================================================\n\n")

    for algo, value in hashes.items():
        result_box.insert(tk.END, f"{algo}:\n{value}\n\n")
        
    # Lock widget state to Read-Only
    result_box.config(state="disabled")
    status_label.config(text="Hashes Generated Successfully")


# Step 13 & Enhancement 2: Clear Function with Read-Only State Management
def clear_output():
    result_box.config(state="normal")
    result_box.delete("1.0", tk.END)
    result_box.config(state="disabled")
    status_label.config(text="Output Cleared")


# Step 20 & Enhancement 2: Save Result Function
def save_result():
    # Fetch content even when disabled
    content = result_box.get("1.0", tk.END).strip()
    
    if not content:
        status_label.config(text="Error: Nothing to save!")
        return

    with open("saved_report.txt", "a") as file:
        file.write(content)
        file.write("\n\n" + "="*50 + "\n\n")

    status_label.config(text="Report Saved")


# Enhancement 5: Copy Output Functionality
def copy_output():
    root.clipboard_clear()
    root.clipboard_append(result_box.get("1.0", tk.END).strip())
    status_label.config(text="Copied to Clipboard!")


# =====================================================================
# UI COMPONENTS & LAYOUT SYSTEM
# =====================================================================

# Step 18: Professional Title
title_label = tk.Label(
    root,
    text="🔐 HASH ANALYSIS TOOLKIT",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="#00ffff"
)
title_label.pack(pady=(15, 5))

# Step 19: Statistics Section Label
stats_label = tk.Label(
    root,
    text="Identified: 0 | Generated: 0",
    bg="#1e1e1e",
    fg="yellow",
    font=("Arial", 11)
)
stats_label.pack(pady=(0, 10))


# Enhancement 1: Consolidated Input Container Card Frame
input_frame = tk.Frame(
    root,
    bg="#252526",
    bd=2,
    relief="ridge"
)
input_frame.pack(pady=10, padx=25, fill="x")

# Inside Frame: Hash Input Components
hash_label = tk.Label(
    input_frame,
    text="Enter Hash For Identification:",
    font=("Arial", 11, "bold"),
    bg="#252526",
    fg="white"
)
hash_label.pack(pady=(10, 2))

hash_entry = tk.Entry(
    input_frame,
    width=75,
    font=("Arial", 11),
    bg="#3e3e42",
    fg="white",
    insertbackground="white",
    bd=1
)
hash_entry.pack(pady=(0, 12))

# Inside Frame: Text Generator Components
text_label = tk.Label(
    input_frame,
    text="Enter Plain Text To Generate Hashes:",
    font=("Arial", 11, "bold"),
    bg="#252526",
    fg="white"
)
text_label.pack(pady=(2, 2))

text_entry = tk.Entry(
    input_frame,
    width=75,
    font=("Arial", 11),
    bg="#3e3e42",
    fg="white",
    insertbackground="white",
    bd=1
)
text_entry.pack(pady=(0, 15))


# Step 14: Actions Grid Frame Container
button_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)
button_frame.pack(pady=10)

# Operational Action Buttons
identify_btn = tk.Button(
    button_frame,
    text="Identify Hash",
    command=identify,
    bg="cyan",
    fg="black",
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
identify_btn.pack(side="left", padx=8)

generate_btn = tk.Button(
    button_frame,
    text="Generate Hashes",
    command=generate,
    bg="lightgreen",
    fg="black",
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
generate_btn.pack(side="left", padx=8)

# Enhancement 5: Copy Result Button
copy_btn = tk.Button(
    button_frame,
    text="Copy Result",
    command=copy_output,
    bg="#b57edc",  # Beautiful soft purple shade
    fg="black",
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
copy_btn.pack(side="left", padx=8)

save_btn = tk.Button(
    button_frame,
    text="Save Report",
    command=save_result,
    bg="lightblue",
    fg="black",
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
save_btn.pack(side="left", padx=8)

clear_btn = tk.Button(
    button_frame,
    text="Clear Output",
    command=clear_output,
    bg="orange",
    fg="black",
    font=("Arial", 11, "bold"),
    width=14,
    cursor="hand2"
)
clear_btn.pack(side="left", padx=8)


# Step 5 Layout Updated: Scrollable Output Monitor Frame
result_frame = tk.Frame(root, bg="#1e1e1e")
result_frame.pack(pady=(10, 5))

scrollbar = tk.Scrollbar(result_frame)

# Enhancement 2: Instantiated with state="disabled" (Read-Only)
result_box = tk.Text(
    result_frame,
    height=12,
    width=88,
    bg="#2d2d2d",
    fg="#e3e3e3",
    font=("Consolas", 11),
    yscrollcommand=scrollbar.set,
    state="disabled" 
)

scrollbar.config(command=result_box.yview)
scrollbar.pack(side="right", fill="y")
result_box.pack(side="left")


# Enhancement 3: Branding Footer Placement
footer = tk.Label(
    root,
    text="Developed by Rohini Mate",
    font=("Arial", 9, "italic"),
    fg="gray",
    bg="#1e1e1e"
)
footer.pack(side="bottom", pady=(0, 2))

# Step 16: Operational Live Status Bar
status_label = tk.Label(
    root,
    text="Ready",
    bg="#111111",
    fg="lightgreen",
    anchor="w",
    font=("Arial", 10),
    padx=12,
    pady=4
)
status_label.pack(
    side="bottom",
    fill="x"
)

# Start Application Loop
root.mainloop()