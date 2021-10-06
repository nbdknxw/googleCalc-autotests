from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class SearchLocators:
    search_field_loc = (By.XPATH, "//input[@name='q']")
    main_search_button_loc = (By.XPATH, "(//input[@name='btnK'])[2]")
    dropdown_search_button_loc = (By.XPATH, "(//input[@name='btnK'])[1]")


class MainGooglePage(BasePage):

    def enter_search_query(self, searchQuery):
        search_field = self.find_element(SearchLocators.search_field_loc)
        search_field.send_keys(searchQuery)
        return search_field

    def click_on_the_main_search_button(self):
        return self.find_element(SearchLocators.main_search_button_loc).click()

    def click_on_the_dropdown_search_button(self):
        return self.find_element(SearchLocators.dropdown_search_button_loc).click()

    def go_to_site(self):
        return self.driver.get(self.base_url)
