from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import datetime

class AlarmApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Set Alarm Time (HH:MM format)", font_size=24)
        self.layout.add_widget(self.label)
        self.time_input = TextInput(multiline=False, font_size=24, size_hint=(1, 0.2))
        self.layout.add_widget(self.time_input)
        self.set_alarm_btn = Button(text="Set Alarm", size_hint=(1, 0.3), font_size=24)
        self.set_alarm_btn.bind(on_press=self.set_alarm)
        self.layout.add_widget(self.set_alarm_btn)
        self.alarm_time = None
        self.alarm_triggered = False
        Clock.schedule_interval(self.check_alarm, 1)
        return self.layout

    def set_alarm(self, instance):
        self.alarm_time = self.time_input.text.strip()
        self.alarm_triggered = False
        self.label.text = f"Alarm set to: {self.alarm_time}"

    def check_alarm(self, dt):
        if self.alarm_time and not self.alarm_triggered:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == self.alarm_time:
                sound = SoundLoader.load('alarm.wav')
                if sound:
                    sound.play()
                self.label.text = "Wake up!"
                self.alarm_triggered = True

if __name__ == '__main__':
    AlarmApp().run()
