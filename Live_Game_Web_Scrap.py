import sys
import time
import datetime
import bs4
import requests
import gc
from bs4 import BeautifulSoup
from urllib.request import urlopen

for i in range (10):
    for i in range (1):
        URL = "https://sportsbook.draftkings.com/leagues/football/nfl"

        page = requests.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")

        results0 = soup.find('div', class_="event-cell__name-text").text
        results1 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').text
        results2 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').text
        results3 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').text
        results5 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results6 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results7 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        results8 = soup.find('div', class_="event-cell__name-text").find_next('div', class_="event-cell__name-text").text
        results9 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results10 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results11 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results12 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results13 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results14 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
    
        print("NFL")
        print(results0,"  Spread", results1,  results2, "  Total", results3, results5,  results6,  "  Money Line",  results7)
        print(results8,"  Spread", results9, results10, "  Total", results11,results12, results13, "  Money Line", results14)
        print(" ")


    for i in range (1):
        URL = "https://sportsbook.draftkings.com/leagues/baseball/mlb"

        page = requests.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")

        results0 = soup.find('div', class_="event-cell__name-text").text
        results1 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').text
        results2 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').text
        results3 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').text
        results5 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results6 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results7 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        results8 = soup.find('div', class_="event-cell__name-text").find_next('div', class_="event-cell__name-text").text
        results9 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results10 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results11 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results12 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results13 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results14 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        print("MLB")
        print(results0,"  Spread", results1,  results2, "  Total", results3, results5,  results6,  "  Money Line",  results7)
        print(results8,"  Spread", results9, results10, "  Total", results11,results12, results13, "  Money Line", results14)
        print(" ")

    for i in range (1):
        URL = "https://sportsbook.draftkings.com/leagues/football/ncaaf"

        page = requests.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")

        results0 = soup.find('div', class_="event-cell__name-text").text
        results1 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').text
        results2 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').text
        results3 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').text
        results5 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results6 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results7 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        results8 = soup.find('div', class_="event-cell__name-text").find_next('div', class_="event-cell__name-text").text
        results9 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results10 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results11 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results12 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results13 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results14 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        print("College Football")
        print(results0,"  Spread", results1,  results2, "  Total", results3, results5,  results6,  "  Money Line",  results7)
        print(results8,"  Spread", results9, results10, "  Total", results11,results12, results13, "  Money Line", results14)
        print(" ")

    for i in range (1):
        URL = "https://sportsbook.draftkings.com/leagues/basketball/nba"

        page = requests.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")

        results0 = soup.find('div', class_="event-cell__name-text").text
        results1 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').text
        results2 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').text
        results3 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').text
        results5 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results6 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results7 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        results8 = soup.find('div', class_="event-cell__name-text").find_next('div', class_="event-cell__name-text").text
        results9 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results10 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results11 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results12 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results13 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results14 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        print("NBA")
        print(results0,"  Spread", results1,  results2, "  Total", results3, results5,  results6,  "  Money Line",  results7)
        print(results8,"  Spread", results9, results10, "  Total", results11,results12, results13, "  Money Line", results14)
        print(" ")

    for i in range (1):
        URL = "https://sportsbook.draftkings.com/leagues/hockey/nhl"

        page = requests.get(URL)

        soup = BeautifulSoup(page.text, "html.parser")

        results0 = soup.find('div', class_="event-cell__name-text").text
        results1 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').text
        results2 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').text
        results3 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').text
        results5 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results6 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results7 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        results8 = soup.find('div', class_="event-cell__name-text").find_next('div', class_="event-cell__name-text").text
        results9 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results10 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results11 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results12 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results13 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text
        results14 = soup.find('div', class_="sportsbook-outcome-cell no-label").find('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').find_next('span').text

        print("NHL")
        print(results0,"  Spread", results1,  results2, "  Total", results3, results5,  results6,  "  Money Line",  results7)
        print(results8,"  Spread", results9, results10, "  Total", results11,results12, results13, "  Money Line", results14)
        print(" ")

sys.exit

