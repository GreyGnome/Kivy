#
#   Copyright 2016 Michael Anthony Schwager
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# This is the InputPopup class. It presents something like a traditional
# modal dialog box to the Kivy programmer, including a TextInput widget
# so you may request text input from the end user. The text obtained is
# returned to a callback function in the calling class.

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
