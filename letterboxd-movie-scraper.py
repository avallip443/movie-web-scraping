from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import get
import random

def movie_list_scrapper(user_url, movie_list, movie_links):
    page_num = 1
    
    while True:
        url = user_url + 'page/' + str(page_num)
        response = get(url) 
        # print('Processing URL: ', url, '\n')

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            try:
                movies = soup.find_all('li', class_='poster-container')
                
                if movies:                    
                    for movie in movies:
                        movie_name = movie.find('img')['alt']
                        movie_list.append(movie_name)
                        
                        movie_link = movie.find('div').get('data-poster-url').split('/', 3)
                        movie_url = 'https://letterboxd.com' + '/'.join(movie_link[:3])
                        movie_links.append(movie_url)
                        
                    page_num += 1
                    
                else:
                    return
            
            except Exception as e:
                print('Error:', e)
        else:
            print('Failed to retrieve the webpage. Status Code:', response.status_code)

        
def select_random_movie(movie_list, movie_links):
    random_number = random.randint(1, len(movie_list)-1)
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("\n\nLet's watch...", movie_list[random_number], '!!\n')
    print("Here's the link!")
    print(movie_links[random_number])
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')

    another_movie = input("Want something else? 1 - Yes, 2 - No \n")
    return another_movie
    

if __name__ == "__main__":
    url = input("Enter list URL: ")
    movie_list = []
    movie_links = []
    movie_list_scrapper(url, movie_list, movie_links)
    
    while select_random_movie(movie_list, movie_links) == '1':
        select_random_movie(movie_list, movie_links)
    
    
    
    