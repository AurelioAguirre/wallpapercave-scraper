# kerei-scraper 0.3

A fork of the wallpaper-scraper Python script that will scrape images from wallpapercave.com and install them into a folder called images.

Now works for front page, all searches, and all categories.

Under development:

    Interface improvements


How to use:

Step 1

Install the latest version of python for Windows 10/11 and make sure to install it on PATH.
https://www.python.org/downloads/windows/


Step 2

    Open CMD


Step 3

Install git from https://git-scm.com/download/win and then:

    git clone https://github.com/Atkoset/kerei-scraper.git

Step 4

The url can be ommitted, it will default to https://wallpapercave.com/
For the Python dependencies you can copy and then run:

    cd kerei-scraper
    pip3 install requirements.txt
    
If you have python 3 installed on PATH, simple run:

    python main.py [URL]    

 This all works as of 20th of September 2022.


Program can also be run using the binary file in the dist folder. Simply run as any executable in Windows 10.

This typically looks like this (making sure you are in the dist folder):

    .\wpc-scraper
