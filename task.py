from RPA.Browser.Selenium import Selenium

browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)


def search_for(term):
    input_field = "css:input"
    browser_lib.wait_until_page_contains_element(input_field)
    browser_lib.input_text(input_field, term)
    browser_lib.press_keys(input_field, "ENTER")


def store_screenshot(filename):
    browser_lib.screenshot(filename=filename)


def expand_sandwich_menu():
    browser_lib.wait_until_page_contains_element("css:#app > div:nth-child(3) > div > header > section.css-9kr9i3.e1m0pzr42 > div.css-qo6pn.ea180rp0 > div.css-6n7j50 > button")
    browser_lib.click_element("css:#app > div:nth-child(3) > div > header > section.css-9kr9i3.e1m0pzr42 > div.css-qo6pn.ea180rp0 > div.css-6n7j50 > button")


def define_news_range(date):
    start_date = "05/01/2023"
    browser_lib.wait_until_page_contains_element("css:#site-content > div.css-1wa7u5r > div.css-1npexfx > div.css-1az02az > div > div > div.css-wsup08 > div > div > button")
    browser_lib.click_button("css:#site-content > div.css-1wa7u5r > div.css-1npexfx > div.css-1az02az > div > div > div.css-wsup08 > div > div > button")
    browser_lib.wait_until_page_contains_element("css:#site-content > div.css-1wa7u5r > div.css-1npexfx > div.css-1az02az > div > div > div.css-wsup08 > div > div > div > ul > li:nth-child(6) > button")
    browser_lib.click_button("css:#site-content > div.css-1wa7u5r > div.css-1npexfx > div.css-1az02az > div > div > div.css-wsup08 > div > div > div > ul > li:nth-child(6) > button")
    start_range_input = "css:#startDate"
    browser_lib.wait_until_page_contains_element(start_range_input)
    browser_lib.input_text(start_range_input, "05/01/2023")

def click_search_button():
    browser_lib.click_button('xpath://*[@id="app"]/div[2]/div/header/section[1]/div[1]/div[2]/button')


# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website("nytimes.com")
        expand_sandwich_menu()
        search_for("Brazil")
        store_screenshot("output/screenshot.png")
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()


# """Template robot with Python."""


# def minimal_task():
#     print("Done.")


# if __name__ == "__main__":
#     minimal_task()
