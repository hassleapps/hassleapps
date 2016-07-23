from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from twilio.twiml import Response

import datetime

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


@csrf_exempt
def home(request):
    return HttpResponse(render_to_string('home.html'), content_type='text/html')

@csrf_exempt
def sms(request):
    # return HttpResponse(render_to_string('sms.xml'), content_type='text/xml')
    print('in here')

    response = Response()
    events = get_events()

    body = request.POST.get('Body', '')

    if body.isdigit() and int(body) in range(0, len(events)):
      event = events[int(body)]
      message = event['summary']
    else:
      message = 'Upcoming events. Text event number for more info.\n'
      for idx, event in enumerate(events):
          message += str(idx) + ': ' + event['summary'][:20] + '\n'

    response.message(message)

    print(message)

    return HttpResponse(response)

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

# def main():
#     """Shows basic usage of the Google Calendar API.

#     Creates a Google Calendar API service object and outputs a list of the next
#     10 events on the user's calendar.
#     """
#     credentials = get_credentials()
#     http = credentials.authorize(httplib2.Http())
#     service = discovery.build('calendar', 'v3', http=http)

#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#     print('Getting the upcoming 10 events')
#     eventsResult = service.events().list(
#         calendarId='brain-arts.org_frpcorsl0jsn7rf8isrt12r4pg@group.calendar.google.com', timeMin=now, maxResults=10, singleEvents=True,
#         orderBy='startTime').execute()
#     events = eventsResult.get('items', [])

#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])

def get_events():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    eventsResult = service.events().list(
        calendarId='brain-arts.org_frpcorsl0jsn7rf8isrt12r4pg@group.calendar.google.com', timeMin=now, maxResults=5, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    return events
