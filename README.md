# Pool Live Pro Point And Stick Automation Program With A Lot Of Flaws (PLP-PAPSAP-WALAF)
This is a quite successful bot with a 50% win ratio so far!

## Dependencies
- Python 2.7 (preferably 32bit, cause there were some compatibility issues with 64bit one)
- pywin32
- OpenCV v2
- As for other, im not quite sure. OpenCV itself requires a lot of stuff, so I'm just listing every pip module I have installed.


    $ pip list
    matplotlib (1.3.0)
    numpy (1.7.1)
    PIL (1.1.7)
    pip (7.1.0)
    pyparsing (2.0.1)
    python-dateutil (2.2)
    pytz (2014.2)
    pywin32 (219)
    setuptools (16.0)
    six (1.6.1)
    wheel (0.24.0)
    

## Running it
A lot of stuff is hardcoded therefore, you need to open [Pool Live Pro on Gamedesire](http://www.gamedesire.com/#/?n=100&gg=143)
maximized, on your primary screen with 1920x1080 resolution. This sucks if you have only one screen, I know.

`python bot_targeting.py` runs "smart" bot with image detection.


`python bot_dummy.py` runs "dumb" bot always targeting middle of the table.

## Remarks
 - Codebase is fairly ugly, sorry.
 - Remember, this app moves your cursor around. Make sure you remember your "Stop running app" shortcut if you run it from IDE.

