'''
This module helps pull daily horoscope from
https://www.astrology.com/horoscope/daily/gemini.html
'''
import urllib.request
import bs4 as bs


def setup_sauce(sign, day):
    '''setup our sauce. if today horoscope is chosen, it actually doesn't add anything to the url'''
    target_url = 'https://www.astrology.com/horoscope/daily/'
    if day.lower() != 'today':
        target_url += day.lower() + '/' + sign.lower() + '.html'
    else:
        target_url += sign.lower() + '.html'
    return urllib.request.urlopen(target_url).read()


def setup_soup(sign, day):
    '''using lxml for our bs object and return it to grab_paragraph for grabbing horoscope text'''
    sauce = setup_sauce(sign, day)
    soup = bs.BeautifulSoup(sauce, 'lxml')
    return soup


def grab_paragraph(sign, day):
    '''scrapes the appropriate paragraph from astrology.com using sign and day'''
    soup = setup_soup(sign, day)
    return soup.p.string


def get_horoscope(sign, day='today'):
    '''will grab dpriaily horoscope from astrology.com. day must be yesterday, today, or tomorrow'''
    horoscope = grab_paragraph(sign, day)
    return horoscope
