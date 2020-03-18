#!/usr/bin/python

# Guilhem Mizrahi 11/2019

# Imports

import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Functions

def get_html(url):
    '''
    This function will retreive the html code from the webpage at URL
    '''
    try:
        r = requests.get(url) # submit a get request
        r_html=r.text
        return(r_html)
    except:
        # if the request could not be submitted then the url is invalid
        return(-1)

def save_code(html_code, file_name):
    '''
    This function will save the html code into a file with the specified filename
    '''
    f = open(file_name, "w+")
    f.write(html_code)
    f.close()

def get_links(html_code):
    '''
    this function will harvest al the links inside <a href= tags
    '''
    soup=BeautifulSoup(html_code, 'html.parser')
    links_list=[]
    for link in soup.find_all('a'): # html tag for links is a
        links_list.append(link.get('href')) # url for the link is in the href parameter
    return(links_list)

def build_url(url, referrer):
    '''
    This function creates an absolute url from a relative url and a referrer
    '''
    return(urljoin(url, referrer))

def update_history(url, history):
    '''
    This script updates the history with the url
    '''
    history.append(url)
    return(history)

def initialize_stack():
    '''
    This function initializes the stack with the root url
    The purpose of having an initialization function is that it allows for easily adding multiple root urls
    '''
    return([])

def initialize_history():
    '''
    This function initializes the history of already visited URLs
    The purpose of a standalone function is to allow for an easy way to blacklist urls
    '''
    return([])

def update_stack(url, stack, history):
    '''
    This function will update the stack of website to go to
        check if the link is in the history (already visited)
        if not push it to the stack
    '''
    if not (url in history or url in stack):
        stack.append(url)
    return(stack)

def main(root_url, max_request=10):
    '''
    How the crawler works : 
        1- start from a root URL
                initialize a stack of urls with only this root URL
        2- go to this URL
                pop the URL from the stack
                add it to the history of visited URLs
        3- harvests all links on the page
                check if the URL linked have already been visited
                    if no then push them to the stack of URLs
                    else don't add them
        4- go to the next URL on the stack
    '''
    stack = initialize_stack()
    history = initialize_history()
    stack = update_stack(root_url, stack, history)
    count_request=0
    while len(stack)>0 and count_request<max_request:
        count_request+=1
        url = stack.pop(0)
        print("Current url={}".format(url))
        code = get_html(url)
        if code!=-1:
            save_code(code, "dump/"+url.split('//')[1].replace('/','_'))
            history = update_history(url, history)
            links = get_links(code)
            #print("Found link(s)\n\t{}".format('\n\t'.join(links)))
            print("\nFound links")
            for link in links:
                print(build_url(url, link))
                stack = update_stack(build_url(url, link), stack, history)
            print("")
        else:
            print("\tInvalid url")
        print("link stack\n{}\n".format('\n'.join(stack)))
        print('-'*50)
    print("Visisted {} url(s)\n{}".format(len(history), '\n'.join(history)))

if __name__=="__main__":
    base_url=sys.argv[1]
    try:
        max_request=int(sys.argv[2])
        main(base_url, max_request)
    except:
        print("Invalid arguments")
