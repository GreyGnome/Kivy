from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class InputPopup(Popup):
    def __init__(self, *args, **kwargs):
        self.text = None
        self.multiple_lines = kwargs.pop('multiline', False)
        self.text_input = TextInput(multiline=self.multiple_lines, text=kwargs.pop('text', "xxx"))

        self.open_function = kwargs.pop('on_open', None)
        super(InputPopup, self).__init__(*args, content=self.text_input, **kwargs)

        self.text_input.bind(on_text_validate=self.validate)
        self.validate_function = kwargs.pop('on_validate', None)
        self.bind(on_open=self.open_callback)


    def validate(self, instance):
        self.dismiss()
        if self.validate_function:
            self.validate_function(self.text_input.text)

    def open_callback(self, instance):
        if self.open_function:
            self.open_function(self)
        self.text_input.focus = True
