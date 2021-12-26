from googlesearch import search

def google_search_result(search_string):
    links = []
    for i in search(search_string,tld='com',num=10,stop=10,pause=2):
        links.append(i)
    return links