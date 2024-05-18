# Importing necessary library
import pandas as pd

# Read CSV files
df1 = pd.read_csv('face_recognition_flask-main/Attendance/Attendance-05_16_24.csv')
df2 = pd.read_csv('face_recognition_flask-main/attendance_Data Science.csv')

# Merge the two DataFrames on the 'name' column
merged_df = pd.merge(df1, df2, on='Name')

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)

print("Merged CSV file saved successfully!")
