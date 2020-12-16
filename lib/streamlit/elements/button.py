# Copyright 2018-2020 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional

from streamlit.proto.Button_pb2 import Button as ButtonProto
from .utils import _get_widget_ui_value


class ButtonMixin:
    def button(dg, label, key=None):
        """Display a button widget.

        Parameters
        ----------
        label : str
            A short label explaining to the user what this button is for.
        key : str
            An optional string to use as the unique key for the widget.
            If this is omitted, a key will be generated for the widget
            based on its content. Multiple widgets of the same type may
            not share the same key.

        Returns
        -------
        bool
            If the button was clicked on the last run of the app.

        Example
        -------
        >>> if st.button('Say hello'):
        ...     st.write('Why hello there')
        ... else:
        ...     st.write('Goodbye')

        """
        return dg._button(label, key, is_form_submitter=False)

    def _button(
        dg, label: str, key: Optional[str], is_form_submitter: bool
    ) -> "DeltaGenerator":
        button_proto = ButtonProto()

        button_proto.label = label
        button_proto.default = False
        button_proto.is_form_submitter = is_form_submitter

        ui_value = _get_widget_ui_value("button", button_proto, user_key=key)
        current_value = ui_value if ui_value is not None else False

        return dg._enqueue("button", button_proto, current_value)  # type: ignore
