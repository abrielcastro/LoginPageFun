from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import re


class LoginPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        self.user_data = {'abriel': 'Abriel@123'}

        # Widgets
        self.username_label = Label(text="Username:", color=(1, 1, 1, 1))
        self.username_input = TextInput(multiline=False)
        self.password_label = Label(text="Password:", color=(1, 1, 1, 1))
        self.password_input = TextInput(multiline=False, password=True)
        self.login_button = Button(text="Enter", on_press=self.perform_login)
        self.register_button = Button(text="Register", on_press=self.show_registration_page)

        # Add widgets to layout
        self.add_widget(Label(text="Register a new account", font_size=45, color=(1, 0, 0, 1)))
        self.add_widget(self.username_label)
        self.add_widget(self.username_input)
        self.add_widget(self.password_label)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)
        self.add_widget(self.register_button)

    def perform_login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if not username or not password:
            self.show_popup("Error", "Both username and password are required.")
            return

        if username not in self.user_data or self.user_data[username] != password:
            self.show_popup("Invalid Credentials", "Invalid username or password.")
        else:
            self.show_logged_in_page()

    def show_registration_page(self, instance):
        self.clear_widgets()
        self.add_widget(Label(text="Registration", font_size=45, color=(1, 0, 0, 1)))

        new_username_label = Label(text="New Username:", color=(1, 1, 1, 1))
        new_username_input = TextInput(multiline=False)

        new_password_label = Label(text="New Password:", color=(1, 1, 1, 1))
        new_password_input = TextInput(multiline=False, password=True)

        reenter_password_label = Label(text="Reenter Password:", color=(1, 1, 1, 1))
        reenter_password_input = TextInput(multiline=False, password=True)

        register_button = Button(text="Register", on_press=lambda x: self.perform_registration(new_username_input.text,
                                                                                               new_password_input.text,
                                                                                               reenter_password_input.text))
        back_button = Button(text="Back to Login", on_press=self.show_login_page)

        self.add_widget(new_username_label)
        self.add_widget(new_username_input)
        self.add_widget(new_password_label)
        self.add_widget(new_password_input)
        self.add_widget(reenter_password_label)
        self.add_widget(reenter_password_input)
        self.add_widget(register_button)
        self.add_widget(back_button)

    def perform_registration(self, new_username, new_password, reenter_password):
        if new_username in self.user_data:
            self.show_popup("Registration Error", "Username already exists.")
            return

        if not (re.search(r'[A-Z]', new_password) and
                re.search(r'[a-z]', new_password) and
                re.search(r'\d', new_password) and
                re.search(r'[!@#$%^&*(),.?":{}|<>]', new_password) and
                len(new_password) >= 8):
            self.show_popup("Registration Error", "Password does not meet requirements :|")
            return

        if new_password != reenter_password:
            self.show_popup("Registration Error", "Passwords do not match :(")
            return

        self.user_data[new_username] = new_password
        self.show_popup("Registration Successful", "You can now log in :)")
        self.show_login_page()

    def show_logged_in_page(self):
        self.clear_widgets()
        self.add_widget(Label(text="Welcome", font_size=45, color=(1, 1, 1, 1)))
        logout_button = Button(text="Logout", on_press=self.show_login_page)
        self.add_widget(logout_button)

    def show_login_page(self, instance=None):
        self.clear_widgets()
        self.__init__()

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()


class LoginApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    LoginApp().run()

