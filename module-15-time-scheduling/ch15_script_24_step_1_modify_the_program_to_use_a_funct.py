"""Chapter 15: Keeping Time Scheduling Launching Programs
Section: Step 1: Modify the Program to Use a Function
Source: Automate the Boring Stuff with Python, 1st ed., Al Sweigart (CC-BY-NC-SA)
  https://automatetheboringstuff.com/1e/chapter15
Type: book script/example
PPT map: Syllabus Ch15: time, datetime, subprocess, threading
File: ch15_script_24_step_1_modify_the_program_to_use_a_funct.py (24 of 37 in this chapter)
"""

   #! python3
   # multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

   import requests, os, bs4, threading
 os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

 def downloadXkcd(startComic, endComic):
     for urlNumber in range(startComic, endComic + 1):
           # Download the page.
           print('Downloading page http://xkcd.com/%s...' % (urlNumber))
         res = requests.get('http://xkcd.com/%s' % (urlNumber))
           res.raise_for_status()

         soup = bs4.BeautifulSoup(res.text)

           # Find the URL of the comic image.
         comicElem = soup.select('#comic img')
           if comicElem == []:
               print('Could not find comic image.')
           else:
             comicUrl = comicElem[0].get('src')
               # Download the image.
               print('Downloading image %s...' % (comicUrl))
             res = requests.get(comicUrl)
               res.raise_for_status()

               # Save the image to ./xkcd.
               imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
               for chunk in res.iter_content(100000):
                   imageFile.write(chunk)
               imageFile.close()

   # TODO: Create and start the Thread objects.
   # TODO: Wait for all threads to end.
