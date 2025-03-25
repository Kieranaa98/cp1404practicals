from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Kivy app that dynamically creates labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]  # List of names

    def build(self):
        """Load the Kivy file and return the root widget."""
        self.root = Builder.load_file('dynamic_widgets.kv')
        return self.root

    def on_start(self):
        """Dynamically create labels for each name in the list."""
        main_layout = self.root.ids.main  # Get reference to BoxLayout with id 'main'
        for name in self.names:
            main_layout.add_widget(Label(text=name))  # Add a Label for each name

DynamicLabelsApp().run()
