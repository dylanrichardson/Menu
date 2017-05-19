from menu import Menu


class UserExample:
    def __init__(self):
        self.logged_in = False
        self.username = "example_user"

        settings_options = [
            ("Change username", self.change_username),
            ("Go back", Menu.CLOSE)
        ]
        self.settings_menu = Menu(
            options=settings_options,
            title="Settings",
            message="Username: " + self.username,
            refresh=self.updateUsername
        )
        self.logged_out_options = [
            ("Login", self.login),
            ("Exit", Menu.CLOSE)
        ]
        self.logged_in_options = [
            ("Settings", self.settings_menu.open),
            ("Logout", self.logout),
            ("Exit", Menu.CLOSE)
        ]
        self.main_menu = Menu(
            title="Main Menu",
            message="Hello guest",
            refresh=self.checkUser)
        self.main_menu.set_prompt(">")

    def updateUsername(self):
        self.settings_menu.set_message("Username: " + self.username)

    def checkUser(self):
        if self.logged_in:
            self.main_menu.set_options(self.logged_in_options)
            self.main_menu.set_message("Hello " + self.username)
        else:
            self.main_menu.set_options(self.logged_out_options)
            self.main_menu.set_message("Hello guest")

    def login(self):
        input("Password: ")
        self.logged_in = True

    def logout(self):
        self.logged_in = False

    def change_username(self):
        self.username = input("New username: ")

    def run(self):
        self.main_menu.open()


if __name__ == "__main__":
    UserExample().run()
