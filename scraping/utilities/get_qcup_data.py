#############################################################################
# A Webscraper for Queensland Cup data using official statistics from nrl.com
# to extract player and match data. 

# TODO: explore if competition_id ca n be used as variable for 
# universal website scraper
#############################################################################

# import modules 
from bs4 import BeautifulSoup
import get_raw_page_html as raw

def fn_get_raw_qcup_data(competition_id, season, round):

    # initialise variables
    competition_id = int(competition_id) # NRL website competition identifer 
    season_int = int(season)
    round_int = int(round)
    url_str = (f"https://www.nrl.com/draw/?competition={competition_id}" + \
               f"&round={round_int}&season={season_int}")

    # print('Ok -'+ str(competition_id) + str(season_int) + str(round_int))
    print(url_str)

    # get raw HTML data data
    raw.fn_get_raw_page_html(url_str)

fn_get_raw_qcup_data(114,2022,1) 