from flask import json
from flask.views import MethodView
import csv


# parse the csv partners.csv and return the info in json format
class Partners(MethodView):
    def post(self):
        # Assuming partners info is stored as a csv in the form:
        # Name, Location, County, AnalysisCost, PaperworkCost, CourtFees, ContactName, ContactInfo
        # Delimiter is semicolon ;
        # File has a header row
        # Empty values are filled with "Unknown"

        partnerDict = {}
        first_row = True
        with open("partners.csv", newline='\n') as partnersFile:
            partners = csv.reader(partnersFile, delimiter=';')
            for partner in partners:
                # skip header row
                if first_row:
                    first_row = False
                else:
                    #  Name
                    key = partner[0]
                    # Location, County, AnalysisCost, PaperworkCost, CourtFees, ContactName, ContractInfo
                    value = (partner[1], partner[2], partner[3], partner[4], partner[6], partner[7])
                    partnerDict.update({key: value})

        return json.dumps(partnerDict)



def register(app):
    app.add_url_rule("/partners", view_func=Partners.as_view("partners"))
