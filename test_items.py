
def test_guest(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.find_element_by_css_selector("#add_to_basket_form > button")