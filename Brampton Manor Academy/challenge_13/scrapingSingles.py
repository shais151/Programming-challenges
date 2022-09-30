import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

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
        position = newString[pos_start+len(posLooking):pos_end]

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

if __name__ == "__main__":
    html = scrape(url)
    data = processData(html)
    table(data)