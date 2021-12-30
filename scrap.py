from bs4 import BeautifulSoup
import requests
import csv

page= requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250").text

soup= BeautifulSoup(page,"lxml")

movie_list= soup.find("tbody",class_="lister-list")
#print(movie_list)
i=1

csv_file= open("scrap.csv","w")
file_writer= csv.writer(csv_file)
file_writer.writerow(["position",'name','year','rating'])



for information in movie_list.find_all('tr'):

    movie_name=information.find("td",class_="titleColumn").a.text
    #print(movie_name)

    movie_year=information.find("td",class_="titleColumn").span.text
    #print(movie_year)

    movie_rating=information.find("td",class_="ratingColumn imdbRating").strong.text
    #print(movie_rating)

   

    print(f'{i} {movie_name} {movie_year} {movie_rating}')

    file_writer.writerow([i,movie_name,movie_year,movie_rating])

    i=i+1

csv_file.close()