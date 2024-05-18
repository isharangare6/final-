import tkinter as tk
from tkinter import filedialog
import pandas as pd


def merge_csv():
    # Open file dialog to choose the first CSV file
    file_path1 = filedialog.askopenfilename(title="Select CSV file 1", filetypes=[("CSV files", "*.csv")])

    if file_path1:
        # Open file dialog to choose the second CSV file
        file_path2 = filedialog.askopenfilename(title="Select CSV file 2", filetypes=[("CSV files", "*.csv")])

        if file_path2:
            # Read both CSV files
            df1 = pd.read_csv(file_path1)
            df2 = pd.read_csv(file_path2)

            # Merge the CSV files
            merged_df = pd.concat([df1, df2], ignore_index=True)

            # Save the merged CSV file
            save_path = filedialog.asksaveasfilename(title="Save merged CSV file", defaultextension=".csv",
                                                     filetypes=[("CSV files", "*.csv")])
            if save_path:
                merged_df.to_csv(save_path, index=False)
                print("CSV files merged successfully and saved as", save_path)
            else:
                print("Operation cancelled.")
        else:
            print("Operation cancelled.")
    else:
        print("Operation cancelled.")


# Create tkinter window
root = tk.Tk()
root.title("CSV File Merger")

# Create merge button
merge_button = tk.Button(root, text="Merge CSV Files", command=merge_csv)
merge_button.pack(pady=20)

# Run the tkinter event loop
root.mainloop()
