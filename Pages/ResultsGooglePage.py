from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ResultsPageLocators:
    calc_input_loc = (By.XPATH, "//div[@class='jlkklc']")
    calc_history_field_loc = (By.CLASS_NAME, "vUGUtc")
    calc_result_field_loc = (By.CLASS_NAME, "qv3Wpe")
    calc_numpad_buttons_loc = (
        By.XPATH, "//table[@class='ElumCf']//div[@role='button' and not(contains(@style,'display:none'))]")


class Calculator(BasePage):

    def enter_calc_expression(self, expr):
        calc_input = self.find_element(ResultsPageLocators.calc_input_loc)
        calc_input.send_keys(expr)
        return calc_input

    def current_calc_value(self):
        calc_input = self.find_element(ResultsPageLocators.calc_input_loc).text
        return calc_input

    def calc_click(self):
        return self.find_element(ResultsPageLocators.calc_input_loc).click()

    def check_history(self):
        self.history = self.find_element(ResultsPageLocators.calc_history_field_loc).text
        for char in self.history:
            if char == "×":
                self.history = self.history.replace(char, "*")
            elif char == "÷":
                self.history = self.history.replace(char, "/")
            elif char == "-":
                self.history = self.history.replace(char, "-")

        return self.history

    def check_result(self):
        result_field = self.find_element(ResultsPageLocators.calc_input_loc).text
        return result_field

    def click_numpad(self, expr):
        self.numpad_buttons = self.find_elements(ResultsPageLocators.calc_numpad_buttons_loc)
        self.values = expr.split()
        self.values = ["×" if x == "*" else x for x in self.values]
        self.values = ["÷" if x == "/" else x for x in self.values]
        self.values = ["−" if x == "-" else x for x in self.values]

        for self.value in self.values:
            for self.button in self.numpad_buttons:
                if self.button.text == self.value:
                    self.button.click()

        return self.button
