__author__ = 'ugunipati'

from assembla import API
import csv

assembla = API(
    key='9df77f45ea5b26a24b57',
    secret='5f329a8fc5bad7e04b368494767a037c0d23aec1',

)

def getalldetails():

    for space in assembla.spaces():
       if space['name']=='test1-space1':
           print 'space name : ' + space['name']
           for milestone in space.milestones():
                print 'milestone id : '+ str (milestone['id'])
                val=milestone['id']
                if (val==8173293):
                    for ticket in space.tickets():
                        print ticket
                        print ticket['id']
                        print ticket['summary']
                        print ticket['status']
                        print ticket['priority']
                        print ticket['assigned_to_id']
                        print ticket['completed_date']
                        print ticket['component_id']
                        print ticket['created_on']
                        print ticket['estimate']
                        print ticket['importance']

                break

def getticketsdatatocsv():

    for space in assembla.spaces():
       if space['name']=='test1-space1':
           print 'space name : ' + space['name']
           for milestone in space.milestones():
                print 'milestone id : '+ str (milestone['id'])
                val=milestone['id']
                if (val==8173293):
                    for ticket in space.tickets():
                        print ticket
                        print type(ticket.data)

                        print ticket.data.keys()
                        print ticket.data.values()

                        with open('mycsvfile.csv','wb') as f:
                            w = csv.writer(f)
                            w.writerow(ticket.data.keys())
                            w.writerow(ticket.data.values())


                break




getticketsdatatocsv()

