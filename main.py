import requests
from bs4 import BeautifulSoup
import re

#for comparing text of 2 places (own logic)
def compareString(string1,string2):
    count = 0
    for i in list(string1.split()):
        for j in list(string2.split()):
            if i==j:
                count = count + 1
    if (2*count)/(len(string1.split())+len(string2.split()))>0.4:
        print(string1)

if __name__=="__main__":
    #for taking input from the user asking the city he wanted to visit
    inp = input("Enter the City you want to Visit: ")
    #temporary list and dictionary objects to be used in the program later
    places_for_each_link = []
    count_dict = {}

    #list of links we want to scrape for getting data with their required parameters.
    url = [["https://wikitravel.org/en/"+inp,"span","fn org",0],["https://en.wikivoyage.org/wiki/"+inp,"span","fn org listing-name",0],["https://www.holidify.com/places/"+inp+"/sightseeing-and-things-to-do.html","h2","card-heading",5]]

    #traversing the links and getting url requests and having data according to required format.
    for link in url:
        html = requests.get(link[0]).text
        soup = BeautifulSoup(html)
        all_links = soup.find_all(link[1],class_=link[2])
        places_for_each_link.append(all_links)
        for place in all_links:
            for finalPlace in count_dict:
                if compareString(place,finalPlace)>0.6:
                    count_dict[finalPlace] += 1
                elif place not in count_dict:
                    count_dict[place] = 0
            print(place.text[link[3]:])
    print(count_dict)

    #for printing the places in sorted order.        
    sorted_places = sorted(count_dict, key=count_dict.get, reverse=True)
    for place in sorted_places:
        print(place)
        #print(mat.prettify())