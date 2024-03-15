from selenium import webdriver

def take_screenshot(url, output_file):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot(output_file)
    driver.quit()

if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    output_file = input("Enter the output file name: ")
    take_screenshot(url, output_file)
