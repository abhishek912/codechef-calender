import requests
from bs4 import BeautifulSoup

def fetch_details(table, event_code, event_name,event_link ,event_start_time, event_end_time):

    for row in table.findAll("tr"):
        col = row.findAll("td")
        if len(col)==4:
            event_code.append(col[0].find(text=True))
            event_name.append(col[1].find('a').contents[0])
            event_link.append("https://www.codechef.com"+col[1].find('a')['href'])
            event_start_time.append(col[2]['data-starttime'])
            event_end_time.append(col[3]['data-endtime'])
    

def print_details(event_code, event_name,event_link, event_start_time, event_end_time):
    i=0
    for event in event_code:
        print(i+1, ")", event_code[i], "||", event_name[i], "||",event_link[i],"||", event_start_time[i], "||", event_end_time[i])
        i+=1

def fetch_events():
    url = 'https://codechef.com/contests'
    html_page = requests.get(url)
    parsed_html_page = BeautifulSoup(html_page.text, 'html.parser')
    contestTables = parsed_html_page.findAll('table', class_ = 'dataTable')

    EVENT_CODE=[]
    EVENT_NAME=[]
    EVENT_LINK=[]
    EVENT_START_TIME=[]
    EVENT_END_TIME=[]
    i=0;

    for contest in contestTables:
        if(i==0 or i==1):
            fetch_details(contest, EVENT_CODE, EVENT_NAME, EVENT_LINK,EVENT_START_TIME, EVENT_END_TIME)
        i+=1
    
    print_details(EVENT_CODE, EVENT_NAME,EVENT_LINK, EVENT_START_TIME, EVENT_END_TIME)        
    return [EVENT_CODE,EVENT_NAME,EVENT_LINK,EVENT_START_TIME,EVENT_END_TIME]

fetch_events()
