import tkinter as tk

def on_yes_click():
    change_text_prompt("Yes")

def on_no_click():
    global no_click_count
    no_click_count += 1
    
    if no_click_count >= 9:
        # If the "No" button is pressed 5 times, destroy the button and change the prompt
        no_button.destroy()
        change_text_prompt("No_Destroyed")
    else:
        increase_button_size()
        change_text_prompt("No")

def change_text_prompt(button_clicked):
    global yes_text_index, no_text_index
    
    if button_clicked == "Yes":
        yes_text_index = (yes_text_index + 1) % len(yes_prompts)
        label.config(text=yes_prompts[yes_text_index])
    elif button_clicked == "No":
        no_text_index = (no_text_index + 1) % len(no_prompts)
        label.config(text=no_prompts[no_text_index])
    elif button_clicked == "No_Destroyed":
        label.config(text="uh oh looks like you have no choice now LMAO")

def increase_button_size():
    current_width = yes_button['width']
    current_height = yes_button['height']
    
    # Increase button size
    yes_button.config(width=current_width + 1, height=current_height + 1)

# Create main window
root = tk.Tk()
root.title("Button Resizer")

# Initialize text prompts for Yes and No buttons
yes_prompts = ["That's all <3", "YAY (keep pressing yes pls)", "You're amazing", "You're cute :)", "Keep working hard doing amazing things Stephanie", "I enjoy the memories we share so far"]
no_prompts = ["Last chance", "Really?", "Alexa play Marvin's room by Drake", "I KNOW YOU STILL THINK ABOUT THE TIMES WE HAD", "You play too much LMAO", "you're a feesh", "YEE", "you don't like sneaker candy you hater"]
yes_text_index = 0
no_text_index = 0

# Create label
label = tk.Label(root, text="Do you want to be my Valentine?")
label.pack(pady=10)

# Create Yes button
yes_button = tk.Button(root, text="Yes", command=on_yes_click, width=10, height=2)
yes_button.pack(side=tk.LEFT, padx=5)

# Create No button
no_button = tk.Button(root, text="No", command=on_no_click, width=10, height=2)
no_button.pack(side=tk.RIGHT, padx=5)

# Initialize click count for the "No" button
no_click_count = 0

# Run the main loop
root.mainloop()
