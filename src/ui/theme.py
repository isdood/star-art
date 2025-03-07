class ThemeManager:
    def __init__(self):
        self.current_theme = "light"
        self.themes = {
            "light": {
                "background_color": "#FFFFFF",
                "text_color": "#000000",
                "button_color": "#E0E0E0",
                "button_text_color": "#000000"
            },
            "dark": {
                "background_color": "#000000",
                "text_color": "#FFFFFF",
                "button_color": "#424242",
                "button_text_color": "#FFFFFF"
            }
        }

    def get_theme(self):
        return self.themes[self.current_theme]

    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name

    def evolve_theme(self):
        # Example of evolving theme logic
        if self.current_theme == "light":
            self.set_theme("dark")
        else:
            self.set_theme("light")
