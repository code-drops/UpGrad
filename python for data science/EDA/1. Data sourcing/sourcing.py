import urllib.request as url
import bs4
import pandas as pd

#  file
f = open("imdb_top50.csv","w")
f.write("name,year,runtime,genre,rating\n")

# html upload
path = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"
http = url.urlopen(path)        # creates a http object or url.urlopen(path).read()

# html parser
page = bs4.BeautifulSoup(http,"html.parser")

# extraction
containers = page.findAll("div",class_="lister-item-content")
for container in containers:
    title = container.find("h3",class_="lister-item-header").find("a").text
    title = title.replace(',', ':')
    year = container.find("span",class_="lister-item-year text-muted unbold").text[1:-1]
    runtime = container.find("span",class_="runtime").text
    genre = container.find("span",class_="genre").text
    genre = genre.replace(',',':')
    rating = container.find("div",class_="inline-block ratings-imdb-rating").find("strong").text

    f.write(title.strip()+","+year.strip()+","+runtime.strip()+","+genre.strip()+","+rating.strip()+"\n")
f.close()

movies = pd.read_csv("imdb_top50.csv",encoding="latin1")
print(movies.head())