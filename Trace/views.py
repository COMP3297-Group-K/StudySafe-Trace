from django.shortcuts import render
from django.views.generic import TemplateView
import requests
import json

# Create your views here.

class View(TemplateView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.head = 'venues/infectious-venues/'
        self.data = []
        self.subject = 0
        self.date = 00000000
    
    def get_infected(self):
        with open('data/json_data.json') as json_file:
            self.infected = (json.load(json_file))

    def get_data(self):
        # self.data = []
        for infected in self.infected['infected']:
            try:
                hkuID, date = infected['hkuID'], infected['date']
                path = 'http://group-k-studysafe.herokuapp.com/core/' + self.head + str(hkuID) + '/' + str(date)
                data = requests.get(url=path)
            except:
                self.error = 1
            else: 
                self.data += json.loads(data.text)
        self.unique()

    def unique(self):
        res = []
        for data in self.data:
            if data not in res:
                res.append(data)
        self.data = res
    
    def get_context_data(self, **kwargs):
        self.get_infected()
        self.get_data()
        context = dict()
        context['error'] = self.error
        context['data'] = self.data
        context['subject'] = self.subject
        context['date'] = self.date
        return context


class ViewVenuesAll(View):
    template_name = "VenuesAll.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.head = 'venues/infectious-venues/'
        self.error = 0


class ViewContactsAll(View):
    template_name = "ContactsAll.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.head = 'members/close-contacts/'
        self.error = 0


class ViewVenues(View):
    template_name = "Venue.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.head = 'venues/infectious-venues/'
        self.error = 0

    def get_infected(self, **kwargs):
        with open('data/json_data.json') as json_file:
            infected = (json.load(json_file))
        hkuID = self.kwargs['hkuID']
        flag = 1
        for member in infected['infected']:
            if member['hkuID'] == hkuID:
                self.infected = {'infected': [{'hkuID': member['hkuID'], 'date': member['date']}]}
                self.subject, self.date = member['hkuID'], member['date']
                flag = 0
        if flag:
            self.error = 1
            self.infected = {'infected':[]}


class ViewContacts(ViewVenues):
    template_name = "Contact.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.head = 'members/close-contacts/'
        self.error = 0


class ViewInfected(TemplateView):
    template_name = "infected.html"
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.error = 0
        self.data = []
    
    def get_infected(self):
        with open('data/json_data.json') as json_file:
            self.infected = (json.load(json_file))

    def get_data(self):
        data = []
        for infected in self.infected['infected']:
            hkuID, date = infected['hkuID'], str(infected['date'])
            date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
            venues = 'http://group-k-studysafe-trace.herokuapp.com/trace/venues/' + str(hkuID)
            contacts = 'http://group-k-studysafe-trace.herokuapp.com/trace/contacts/' + str(hkuID)
            data += [{'hkuID':hkuID, 'date':date, 'venues':venues, 'contacts':contacts}]
        self.data = data

    def get_context_data(self, **kwargs):
        self.get_infected()
        self.get_data()
        context = dict()
        context['error'] = self.error
        context['data'] = self.data
        return context



if __name__ == '__main__':
    venues = ViewVenues()
    print(venues.get_context_data())
    contacts = ViewContacts()
    print(contacts.get_context_data())
    print(contacts.data)
