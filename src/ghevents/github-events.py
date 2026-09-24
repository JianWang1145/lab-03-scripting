#!/usr/bin/env python3
import os
import json
import requests

GHUSER = os.getenv("GITHUB_USER")
url = f"https://api.github.com/users/{GHUSER}/events"

def retrieve_events(url):
    response_text = requests.get(url).text
    events_data = json.loads(response_text)
    return events_data
'''retrieves github event file in json form and returns it as events_data'''

def print_events(events, n=5):
    for x in events[:n]:
        event = x["type"] + " :: " + x["repo"]["name"]
        print(event)
'''print the first n events in the event data in the form type::repo'''

def main():
    print(GHUSER)
    print(url)
    returned_list = retrieve_events(url)
    print_events(returned_list)
'''print the initial variable, call retrieve_events function and stores it in variable "returned_list",
call "print_events" to output in said format. Main is the function for executing the action of fetching recent GitHub
events.'''


if __name__ == "__main__":
    main()
