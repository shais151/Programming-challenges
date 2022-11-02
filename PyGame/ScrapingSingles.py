# pygame template - BMACS 2020
import pygame  # accesses pygame files
import sys  # to communicate with windows
import urllib.request  # scrape websites

url = "https://www.officialcharts.com/charts/singles-chart"

# game setup ################ only runs once
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1000, 800  # sets size of screen/window
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
# set variables for colors RGB (0-255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
purple = (255, 0, 255)


gameState = "running"  # controls which state the games is in
####### game loop #######runs 60 times a second!
while gameState != "exit":  # game loop - note:  everything in the mainloop is indented one tab
    for event in pygame.event.get():  # get user interaction events
        if event.type == pygame.QUIT:  # tests if window's X (close) has been clicked
            gameState = "exit"  # causes exit of game loop
        if event.type == pygame.KEYDOWN:  # tests if a key has been pressed down
            if event.key == pygame.K_ESCAPE:  # tests if that pressed key is the escape key
                gameState = "exit"  # causes exit of game loop
    ####### your code starts here #######

    def scrape(url):
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        return mystr


    def processData(html):
        singles = {}
        i = 0
        loop = 0

        while loop < 10:
            open_tr = html.find('<tr>', i)
            close_tr = html.find("</tr>", open_tr)

            newString = html[open_tr:close_tr]

            posLooking = '"position">'
            pos_start = newString.find(posLooking)
            pos_end = newString.find('</', pos_start)
            position = newString[pos_start + len(posLooking):pos_end]

            trackLooking = '/">'
            pos_start = newString.find(trackLooking)
            pos_end = newString.find('</a>', pos_start)
            title = newString[pos_start + len(trackLooking):pos_end]

            artistLooking = '/">'
            pos_start = newString.find(artistLooking, pos_end)
            pos_end = newString.find('</a>', pos_start)
            artist = newString[pos_start + len(artistLooking):pos_end]

            singles[int(position)] = {
                "title": title,
                "artist": artist
            }

            i = close_tr
            loop += 1
        return singles


    def table(data):
        headerValues = ["Pos", "Track", "Artist"]
        print(f'{headerValues[0]} {headerValues[1]:>23} {headerValues[2]:>33}')

        pos = 1
        while pos < 11:
            title = data[pos]["title"]
            artist = data[pos]["artist"]
            titleLength = len(title)
            print(f"{pos} {title:>33}  {artist:>30}")
            pos += 1

    ####### your code ends here ###############################
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value

####### out of game loop #######
print("The game has closed")  # notifies user the game has ended
pygame.quit()  # stops the game engine
sys.exit()  # close operating system window