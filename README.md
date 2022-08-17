# wallpapercave-scraper 0.3

A simple Python script that will scrape images from wallpapercave.com and install them into a folder called images.

Now works for front page, all searches, and all categories.

Under development:

    Interface improvements


How to use:

If you have python 3 installed, simple run:

    python main.py [URL]

The url can be ommitted, it will default to https://wallpapercave.com/
Python dependencies are:

    click
    requests
    bs4

All the latest versions as of today 27th of July 2022.


Program can also be run using the binary file in the dist folder. Simply run as any executable in Linux. (No Windows or Mac version as of yet.)

This typically looks like this (making sure you are in the dist folder):

    chmod +x wpc-scraper
    ./wpc-scraper
