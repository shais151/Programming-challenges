import csv
import codecs

def read_csv(path):
    csv_contents = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents

def read_html(path):
    file = codecs.open(path, "r", "utf-8")
    return file.read()

def process(csv, html):
    new = html

    loop = 1
    i = 0
    for data in csv:
        link = data[0]
        initials = data[1]
        name = data[2]

        init_search = "initials"+str(loop)
        name_search = "name"+str(loop)
        image_code = "<img src="+link+" alt="+name+">"

        new = new.replace(init_search, initials)
        new = new.replace(name_search, name)

        start = '<div class="el__bg">'
        end = '</div>'
        pos_start = new.find(start, i)
        pos_end = new.find(end, pos_start)

        new = new[:pos_start+ len(start)] + image_code + new[pos_end:]

        i = pos_end
        loop += 1
    return new

def write_html(path, html):
    file = open(path, "w")
    file.write(html)
    file.close()

if __name__ == "__main__":
    csv = read_csv(path="south.csv")
    html = read_html(path="south.html")
    new_html = process(csv=csv, html=html)
    write_html(path="south_final.html", html=new_html)