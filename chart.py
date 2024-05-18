
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('face_recognition_flask-main/Attendance/merged.csv')

# Assuming 'values' column contains the data for the pie chart
# You may need to adjust this depending on your CSV structure
values = data['values']

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(values, labels=data['labels'], autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

