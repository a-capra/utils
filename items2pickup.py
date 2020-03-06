import requests
from html.parser import HTMLParser
import re
import smtplib
from email.mime.text import MIMEText
from time import sleep
import datetime

class PickUpParser(HTMLParser):

    def __init__(self):
        super().__init__() 
        self._relevant_section = False
        self._tag_counter = 0
        self._name_bin={}

    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        for attr in attrs:
            #print("     attr:", attr)
            if attr[0] == 'class' and attr[1] == 'node__content':
                self._relevant_section=True
                #print(" relevant attr:", attr)
        if self._relevant_section:
            self._tag_counter += 1

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        if self._relevant_section:
            self._tag_counter -= 1
        if self._tag_counter == 0:
            self._relevant_section = False
        
    def handle_data(self, data):
        #print("Encountered some data  :", data)
        if self._relevant_section:
            self.get_name_bin(data)

    def get_name_bin(self,data):
        if data.isspace():
            pass
        else:
            res1=re.match(r'.+, [A-Z]{1} [0-9]{1,3}',data)
            res2=re.match(r'^.+- [0-9]{1,3}',data)
            if res1:
                #print(res1.group(0))
                last,temp=res1.group(0).split(',')
                last = last.strip()
                #print(temp)
                mobj1=re.search(r'[A-Z]{1}',temp)
                mobj2=re.search(r'[0-9]{1,3}',temp)
                if mobj1 and mobj2:
                    iniz=mobj1.group(0).strip()
                    binn=mobj2.group(0).strip()
                    #print(iniz+'. ',last,'\tbin #',binn)
                    self._name_bin[iniz+'. '+last]=int(binn)
            elif res2:
                #print(res2.group(0))
                name,binn=res2.group(0).split('-')
                #print(name.strip(),'\tbin #',binn.strip())
                self._name_bin[name.strip()]=int(binn.strip())
            #print('<---------- Start ---------->')
            #print(data)
            #print('>---------- End ----------<')

    def print_name_bin(self):
        for x, y in self._name_bin.items():
            print('Name:',x, 'Bin:', y)

    def Item(self,name):
        for x, y in self._name_bin.items():
            if name in x:
                return y
        return -1

    def notify(self,bin_number):
        msg = MIMEText("Hey Andrea,\n you've got an item waiting for in bin {}\nCheers,\nPyalpha".format(bin_number))
        address='andrea.capra85@gmail.com'
        #address='acapra@triumf.ca'
        msg['Subject'] = 'Item for you to pick-up at Stores'
        msg['From'] = 'alpha01'
        msg['To'] = address
        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail('alpha01', [address], msg.as_string())
        s.quit()
  

while True:
    parser = PickUpParser()
    response = requests.get('https://www.triumf.ca/supply-chain-management/receiving-pick-ups')
    if response.status_code == 200:
        #print(response.content.decode())
        parser.feed(response.content.decode())
        #parser.print_name_bin()
        bin_number = parser.Item('Capra')
        if bin_number > 0:
            parser.notify(bin_number)
        else:
            print('I checked at',datetime.datetime.now(),'and no items were delivered')
    else:
        print('Status:',response.status_code)

    sleep(3600)
