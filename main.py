from kivy.app import App
from LoginPage import LoginPage

class LoginApp(App):
    def build(self):
        return LoginPage()

if __name__ == '__main__':
    LoginApp().run()
