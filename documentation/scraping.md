# NRL data scraping 

## Overview 
### Purpose
This documents the scraping module for the NRL-Data section. It is a work in progress, and will be iteratively developed. It aims to explain how the data is obtained from nrl.com, some of the rationale, and the subsequent processing from raw. 

### Source data
This tool scrapes the official NRL statistics from nrl.com; other websites, such as Foxsports, aggregate their own statistics that may or may not match the data. Verify only against nrl.com.

### Why Selenium?
NRL.com is a dynamic web-page, so using packages likes urllib will not extract all required source HTML for further processing in other modules.   

## References and further
Links tp references and further reading for this module that was found useful with the scraping module.
* [Breuss, M. (n.d.). Beautiful Soup: Build a Web Scraper With Python – Real Python](https://realpython.com/beautiful-soup-web-scraper-python/)
* [Richardson, L. (2019). Beautiful Soup Documentation — Beautiful Soup 4.4.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
### Chromium ChromeDriver
* [ChromeDriver overview. (n.d.). Chrome for Developers.](https://developer.chrome.com/docs/chromedriver/)
* [List of Chromium Command Line Switches Peter Beverloo. (n.d.). Peter.sh.](https://peter.sh/experiments/chromium-command-line-switches/)

‌