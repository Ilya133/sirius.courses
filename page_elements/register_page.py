from time import sleep

from selene import browser, query, have, be, by

from locators import RegisterPageLocators


class StringField:

    @staticmethod
    def change_property(label, value):
        field = browser.element(
            f".//*[contains(@class, '{RegisterPageLocators.FIELD_LABEL}')"
            f" and .//*[contains(text(), '{label}')]]").type(value)

        if label == 'Дата рождения':
            field.element(RegisterPageLocators.DATE_TIME_INPUT_LOCATOR).wait_until(have.text(value))

    @staticmethod
    def get_error_text():
        return browser.element('.text-xs').get(query.text)


class RadioButton:

    @staticmethod
    def click_radio_button():
        browser.element(f'.{RegisterPageLocators.RADIO_BUTTON_LOCATOR}').click()


class CheckBox:

    @staticmethod
    def click_check_boxes():
        check_boxes = browser.all(f'.{RegisterPageLocators.CHECK_BOX_LOCATOR}')

        for check_box in check_boxes:
            if check_box.matching(have.css_class('ui-schema-auth-form__checkbox-unset')):
                check_box.click()


class Button:

    @staticmethod
    def click_register_button():
        browser.element(f'.{RegisterPageLocators.REGISTER_BUTTON_LOCATOR}').should(be.clickable).click()

    @staticmethod
    def click_lang_switcher_button(language):
        languages = {
            'Русский': RegisterPageLocators.RU_SWITCH_BUTTON_LOCATOR,
            'Английский': RegisterPageLocators.ENG_SWITCH_BUTTON_LOCATOR
        }

        browser.element(RegisterPageLocators.DROPDOWN_BUTTON_LOCATOR).click()
        browser.element(languages[language]).click()

    @staticmethod
    def click_back_button():
        browser.element(RegisterPageLocators.BACK_BUTTON_LOCATOR).click()


class RegistrationPanel:

    @staticmethod
    def get_panel_text():
        return browser.element(RegisterPageLocators.REG_PANEL_SUCCESS_MESSAGE_LOCATOR).get(query.text)
