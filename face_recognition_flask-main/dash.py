import csv

from flask import Flask
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.camera import Camera
from kivy.clock import Clock


app = Flask(__name__)


class AttendanceApp(App):
    def build(self):
        self.title = 'Smart Attendance App'
        self.layout = BoxLayout(orientation='vertical')

        # Subject dropdown
        self.subject_spinner = Spinner(text='Select Subject', values=('DBMS', 'Data Science', 'Python'))
        self.layout.add_widget(self.subject_spinner)

        # Teacher dropdown
        self.teacher_spinner = Spinner(text='Select Teacher',
                                       values=('prof. Kamaljeet kaalsi', 'prof. pinkal jain', 'prof. Vimmy Pandey'))
        self.layout.add_widget(self.teacher_spinner)

        # Widgets for live photo capture
        self.camera = Camera(resolution=(640, 480), play=True)
        self.layout.add_widget(self.camera)

        self.capture_button = Button(text='Capture', size_hint=(None, None), size=(100, 50))
        self.capture_button.bind(on_press=self.capture_photo)
        self.layout.add_widget(self.capture_button)

        # Export button
        self.export_button = Button(text='Export Attendance', size_hint=(None, None), size=(150, 50))
        self.export_button.bind(on_press=self.export_attendance)
        self.layout.add_widget(self.export_button)

        return self.layout

    def capture_photo(self, instance):
        Clock.schedule_once(self.save_photo, 0)

    def save_photo(self, dt):
        # Save photo to a file, implement your logic here
        pass

    def export_attendance(self, instance):
        subject = self.subject_spinner.text
        teacher = self.teacher_spinner.text

        # Dummy attendance data, replace with actual data
        attendance_data = [
            {'Subject': subject, 'Teacher': teacher, 'Name': 'isha', 'Status': 'Present'},
            {'Subject': subject, 'Teacher': teacher, 'Name': 'ADVIK', 'Status': 'Absent'},
            {'Subject': subject, 'Teacher': teacher, 'Name': 'madhuri', 'Status': 'Present'}
        ]

        # Write data to CSV file
        filename = f'attendance_{subject}.csv'
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Subject', 'Teacher', 'Name', 'Status'])
            writer.writeheader()
            writer.writerows(attendance_data)

        self.show_popup(f'Attendance for {subject} exported successfully')

    def show_popup(self, message):
        popup = Popup(title='Export Status', content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()



if __name__ == '__main__':
    AttendanceApp().run()

