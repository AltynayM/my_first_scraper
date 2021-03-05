import requests
from bs4 import BeautifulSoup

def request_github_trending(url):
    return(requests.get(url).text)

def extract(page):
    return(BeautifulSoup(page, 'lxml'))

def transform(html_repos):
    names = []
    stars = []
    for article in html_repos.find_all('article'):
        names.append(article.h1.text)
        stars.append(article.find(class_ = 'f6 color-text-secondary mt-2').find(class_ = 'd-inline-block float-sm-right').text)
    res_list = []
    res_dict = {}
    for i in range(len(names)):
        names[i] = names[i].split()
        stars[i] = stars[i].split()
        res_dict['developer'] = names[i][0]
        res_dict['repository_name'] = names[i][2]
        res_dict['nbr_stars'] = stars[i][0]
        res_list.append(res_dict)
        res_dict = {}
    # print(res_list)
    return res_list

def format(repositories_data):
    csv_string = "Developer,Repository Name,Number of Stars" + r'\n'
    for i in range(len(repositories_data)):
        temp = list(repositories_data[i].values())
        for j in range(len(temp) - 1):
            csv_string += temp[j] + ','
        csv_string += temp[len(temp) - 1] + r'\n'
    print(csv_string)
    return csv_string

page = request_github_trending('https://github.com/trending')
html_repos = extract(page)
repositories_data = transform(html_repos)
format(repositories_data)
