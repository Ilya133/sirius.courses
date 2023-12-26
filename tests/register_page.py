import pytest

from page_elements.register_page import StringField, RadioButton, CheckBox, Button, RegistrationPanel
from test_data.register_form_data import *


@pytest.mark.xdist_group(name="group1")
def test_fill_in_register_form_and_start_testing(runner):
    # step 1
    for item_key, item_value in register_form_text_values.items():
        StringField.change_property(item_key, item_value)

    RadioButton.click_radio_button()
    CheckBox.click_check_boxes()

    # step 2
    Button.click_register_button()


@pytest.mark.xdist_group(name="group1")
def test_language_switcher(runner):
    # step 1
    Button.click_lang_switcher_button('Английский')

    # step 2
    expected_text = RegistrationPanel.get_panel_text()
    assert expected_text == page_letter_confirmation['eng_text']

    # step 3
    Button.click_lang_switcher_button('Русский')

    # step 4
    expected_text = RegistrationPanel.get_panel_text()
    assert expected_text == page_letter_confirmation['ru_text']


@pytest.mark.xdist_group(name="group1")
def test_return_to_register_page(runner):
    # step 1
    Button.click_back_button()


@pytest.mark.xdist_group(name="group2")
def test_wrong_snils(runner):
    # step 1
    StringField.change_property(snils_length_error['Имя поля'], snils_length_error['Значение'])

    # step 2
    expected_error_text = StringField.get_error_text()
    assert expected_error_text == snils_length_error['Текст ошибки']

    # step 3
    StringField.change_property(snils_only_numbers_error['Имя поля'], snils_only_numbers_error['Значение'])

    # step 4
    expected_error_text = StringField.get_error_text()
    assert expected_error_text == snils_only_numbers_error['Текст ошибки']


@pytest.mark.xdist_group(name="group2")
def test_wrong_vosh_login(runner):
    # step 1
    StringField.change_property(wrong_vosh_login['Имя поля'], wrong_vosh_login['Значение'])

    # step 1
    expected_error_text = StringField.get_error_text()
    assert expected_error_text == wrong_vosh_login['Текст ошибки']
