"""Chapter 11: Web Scraping
Section: Step 3: Find and Download the Comic Image
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter11
Type: book script/example
PPT map: Syllabus Ch11: webbrowser, requests, bs4, selenium
File: ch11_script_26_step_3_find_and_download_the_comic_image.py (26 of 34 in this chapter)
"""

#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

--snip--

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
         print('Could not find comic image.')
    else:
         try:
             comicUrl = 'http:' + comicElem[0].get('src')
             # Download the image.
             print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
             res.raise_for_status()
         except requests.exceptions.MissingSchema:
             # skip this comic
             prevLink = soup.select('a[rel="prev"]')[0]
             url = 'http://xkcd.com' + prevLink.get('href')
             continue


    # TODO: Save the image to ./xkcd.

    # TODO: Get the Prev button's url.

print('Done.')
