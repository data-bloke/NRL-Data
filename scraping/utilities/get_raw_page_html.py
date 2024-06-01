

def fn_get_raw_page_html(url):
    # Initialise Chrome browser instance for automated scraping
    # Note: WebDriver is an open source tool for automated testing of webapps. 
    # In Python, WebDriver class will connect you to a browser’s instance 
    # Initialised as per https://pypi.org/project/chromedriver-autoinstaller/

    from selenium import webdriver 
    from selenium.webdriver.chrome.options import Options
    import chromedriver_autoinstaller

    # Initialise input     
    url_str = url
    
    # Initialise webdriver 
    chromedriver_autoinstaller.install()  # Check if the current version of 
                                        # chromedriver exists and if it doesn't
                                        # exist, download it automatically,
                                        # then add chromedriver to path
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_browser_type_str= webdriver.Chrome(options=options)
    
    # Scrape raw data from URL for given NRL season and round 
    page_source_txt = driver_browser_type_str.get(url_str)
    driver_browser_type_str.quit()

    print('OK. Scraped raw data from NRL website for given season and round.')
    return page_source_txt 

# fn_get_raw_page_html("https://www.nrl.com/draw/?competition=114&round=1&" + \
#                     "season=2022")
