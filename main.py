
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class RuffierProcessor:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.heartbeat1 = 0
        self.heartbeat2 = 0
        self.heartbeat3 = 0

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = int(age)

    def set_hb1(self,hb1):
        self.heartbeat1 = int(hb1)

    def set_hb2(self,hb2):
        self.heartbeat2 = int(hb2)

    def set_hb3(self,hb3):
        self.heartbeat3 = int(hb3)

    def do_result(self):
        result = (4*(self.heartbeat1+self.heartbeat2+self.heartbeat3)-200)/10
        if self.age >= 15:
            if result >= 15:
                text = 0
            elif result >= 11 and result <= 14:
                text = 1
            elif result >= 6 and result <= 10:
                text = 2
            elif result >= 1 and result <= 5:
                text = 3
            else:
                text = 4
        elif self.age == 13 or self.age == 14:
            if result >= 16:
                text = 0
            elif result >= 12 and result <= 15:
                text = 1
            elif result >= 7 and result <= 11:
                text = 2
            elif result >= 2 and result <= 6:
                text = 3
            else:
                text = 4
        elif self.age == 11 or self.age == 12:
            if result >= 18:
                text = 0
            elif result >= 14 and result <= 17:
                text = 1
            elif result >= 9 and result <= 13:
                text = 2
            elif result >= 3 and result <= 8:
                text = 3
            else:
                text = 4
        elif self.age == 9 or self.age == 10:
            if result >= 19:
                text = 0
            elif result >= 15 and result <= 18:
                text = 1
            elif result >= 10 and result <= 14:
                text = 2
            elif result >= 5 and result <= 9:
                text = 3
            else:
                text = 4
        elif self.age == 7 or self.age == 8:
            if result >= 21:
                text = 0
            elif result >= 17 and result <= 21:
                text = 1
            elif result >= 12 and result <= 16:
                text = 2
            elif result >= 6 and result <= 11:
                text = 3
            else:
                text = 4
        else:
            text = 5
        return text
client = RuffierProcessor()
result = ['Unsatisfactory','Weak','Satisfactory','Good','Excellent',"For that age, we can't calculate the result"]

class ScrButton(Button):
    def __init__(self, screen, goal, direction='left', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Scr1Button(ScrButton):
    def __init__(self,screen,goal,direction='left',**kwargs):
        super().__init__(screen,goal,direction,**kwargs)

    def on_press(self):
        print('sdasdada')
        client.set_name(self.screen.text_in_name.text)
        client.set_age(self.screen.text_in_age.text)
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Scr2Button(ScrButton):
    def __init__(self, screen, goal, direction='left', **kwargs):
        super().__init__(screen, goal, direction, **kwargs)

    def on_press(self):
        client.set_hb1(self.screen.text_in.text)
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class Scr3Button(ScrButton):
    def __init__(self, screen, goal, direction='left', **kwargs):
        super().__init__(screen, goal, direction, **kwargs)

    def on_press(self):
        client.set_hb2(self.screen.text_in_1.text)
        client.set_hb3(self.screen.text_in_2.text)
        screen4.replace(result[client.do_result()])
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        layout_main = BoxLayout(orientation='vertical', padding=20, spacing=80)
        layout_sub = BoxLayout(padding=25, spacing=10)
        label = Label(
            text="The Ruffier-Dickson index a simple test to know how your heart responds to physical exertion.\n  1.The subject's pulse is taken while sitting at rest for 15 s.\n  2.The subject then performs 30 squats for 45 s.\n  3.After that, his/her heart rate is recorded for the first and last 15 s of the first minute of recovery.\nThe Ruffier-Dixon index is calculated using the formula: IR = 4 (P1 + P2 + P3) - 200/10, where IR - Ruffier-Dixon index,\nP1 - HR at rest sitting for 15 s, P2 - HR for the first 15 s of the first minute of recovery,\nP3 - HR for the last 15 s of the first minute of recovery.\n\nFor more accurate verification, enter your full age and name",
            font_size='15sp')
        label_main = Label(text="Test Ruffier", font_size='20sp', halign="left", valign="middle")
        btn1 = Scr1Button(self, 'scr1', text='Next')
        self.text_in_age = TextInput(text='')
        self.text_in_name = TextInput(text='')
        label_name = Label(text='Name:', font_size='15sp')
        label_age = Label(text='Age:', font_size='15sp')
        layout_main.add_widget(label_main)
        layout_main.add_widget(label)
        layout_sub.add_widget(label_name)
        layout_sub.add_widget(self.text_in_name)
        layout_sub.add_widget(label_age)
        layout_sub.add_widget(self.text_in_age)
        layout_main.add_widget(layout_sub)
        layout_main.add_widget(btn1)
        self.add_widget(layout_main)


class SubScreen1(Screen):
    def __init__(self, name, goal):
        super().__init__(name=name)
        layout_main = BoxLayout(orientation='vertical', padding=20, spacing=70)
        label = Label(text="1.The subject's pulse is taken while sitting at rest for 15 s.")
        btn = Scr2Button(self, goal, text='next')
        self.text_in = TextInput(text='', multiline=False)
        layout_main.add_widget(label)
        layout_main.add_widget(self.text_in)
        layout_main.add_widget(btn)
        self.add_widget(layout_main)


class SubScreen2(Screen):
    def __init__(self, name, goal):
        super().__init__(name=name)
        layout_main = BoxLayout(orientation='vertical', padding=20, spacing=70)
        label = Label(text='2.The subject then performs 30 squats for 45 s.\n3.After that, his/her heart rate is recorded for the first and last 15 s of the first minute of recovery.')
        btn = Scr3Button(self, goal, text='next')
        label_1 = Label(text ='First record')
        self.text_in_1 = TextInput(text='', multiline=False)
        label_2 = Label(text='Second record')
        self.text_in_2 = TextInput(text='', multiline=False)
        layout_main.add_widget(label)
        layout_main.add_widget(label_1)
        layout_main.add_widget(self.text_in_1)
        layout_main.add_widget(label_2)
        layout_main.add_widget(self.text_in_2)
        layout_main.add_widget(btn)
        self.add_widget(layout_main)


class SubScreen3(Screen):
    def __init__(self, name):
        super().__init__(name=name)
        layout_main = BoxLayout(orientation='vertical', padding=20, spacing=70)
        self.label = Label(
            text='Your result:')
        label1 = Label(text = 'Thank you for taking the test!\nIf you click the button, you can restart the test.')
        btn = ScrButton(self, 'main', text='Назад')
        layout_main.add_widget(self.label)
        layout_main.add_widget(label1)
        layout_main.add_widget(btn)
        self.add_widget(layout_main)

    def replace(self, main_result):
        self.label = Label(text = 'Your result:'+ main_result )

screen4 = None
class MyApp(App):
    def build(self):
        global screen4
        sm = ScreenManager()
        sm.add_widget(MainScr())
        scr1 = SubScreen1('scr1', 'scr2')
        scr2 = SubScreen2('scr2', 'scr4')
        scr4 = SubScreen3('scr4')
        screen4 = scr4
        sm.add_widget(scr1)
        sm.add_widget(scr2)
        sm.add_widget(scr4)
        return sm


app = MyApp()
app.run()
