import requests
from html.parser import HTMLParser
import re
import smtplib
from email.mime.text import MIMEText
from time import sleep
import datetime
import getpass
import argparse

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

    def notify(self,user,address,bin_number):
        sender = getpass.getuser()
        msg = MIMEText("Hey {},\nyou've got an item waiting for you in bin {}\nCheers,\n{}".format(user,bin_number,sender))
        msg['Subject'] = 'Item for you to pick-up at Stores'
        msg['From'] = str(sender)
        msg['To'] = ', '.join(address)
        s = smtplib.SMTP('localhost')
        s.sendmail(sender, address, msg.as_string())
        s.quit()
  


if __name__ == '__main__':

    first_name = 'Andrea'
    last_name = 'Capra'
    sleep_time = 3600 # seconds
    email=['andrea.capra85@gmail.com','acapra@triumf.ca']

    argparser = argparse.ArgumentParser()
    argparser.add_argument("email",help="recipient address",nargs='+')
    argparser.add_argument("last",help="last name for search",type=str)
    argparser.add_argument("-f","--first",help="first name for notification message",type=str,default="Stranger")
    argparser.add_argument("-t","--time",help="time interval between queries",type=int,default=3600)
    argparser.add_argument("-v", "--verbose", help="print all people/bin pairs",action="store_true")

    args = argparser.parse_args()

    email=args.email
    last_name=args.last
    first_name=args.first
    sleep_time=args.time

    while True:
        htmlparser = PickUpParser()
        response = requests.get('https://www.triumf.ca/supply-chain-management/receiving-pick-ups')
        when=datetime.datetime.today().strftime("%A, %d %B %Y at %H:%M")
        if response.status_code == 200:
            #print(response.content.decode())
            htmlparser.feed(response.content.decode())
            #htmlparser.print_name_bin()
            if args.verbose:
                htmlparser.print_name_bin()
            bin_number = htmlparser.Item(last_name)
            if bin_number > 0:
                htmlparser.notify(first_name,email,bin_number)
                print('User {} has been notified on {}'.format(first_name,when))
            else:
                print('I checked today',when,'and no items were delivered to',first_name)
        else:
            print('Status:',response.status_code)

        sleep(sleep_time)
