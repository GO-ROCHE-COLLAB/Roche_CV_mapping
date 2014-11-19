import requests # http://docs.python-requests.org/en/latest/
import re
import json
import getpass
import warnings

## Standard GitHub APIs seemed a bit heavy-weight for this.

def anchor_sub(match):
    """Sub for use in regex.  Takes a match object, returns one turned 
    lower case and with all spaces changed to -"""
    if match.group(1) == ' ':
        return '-'
    else:
        return match.group(1).lower()

class issueConn:
    """Class packaging connection details and methods for GET/POST issues to GitHub"""
    
    GITHUB_URL = "https://api.github.com"
    HEADERS = {'Content-Type': 'application/json'}
    
    def __init__(self, org, repo, usr):
        self.issues_url = "{0}/{1}".format(self.GITHUB_URL, "/".join(
             ["repos", org, repo, "issues"]))
        self.usr = usr
        self.set_credentials_from_cl()
        self.all_issues = []
        self.get_all_tickets()
        # Add in a connection test here?
    
    def test_conn(self):
        return requests.get(self.issues_url, auth=self.AUTH)
        
        
    def __str__(self):
        return "Object for GET/POST to %s" % self.issues_url
        
    def set_credentials_from_cl(self, i=0):
        pwd = getpass.getpass().rstrip("\n")
        self.AUTH = (self.usr, pwd)
        t = self.test_conn()
        if not t.status_code == 200:
            i +=1
            warnings.warn(t.reason)
            if i <= 3:
                self.set_credentials_from_cl(i)

        
    def set_pwd(self, pwd):
        self.AUTH = (self.usr, pwd)

    def get_ticket_state(self, number):
        """Queries GitHub using ticket number, returns json."""
        url = self.issues_url + '/' + str(number)
        issue = requests.get(url, auth=self.AUTH)
        ij = issue.json()
        return ij
    
    def create_github_issue(self, data):
        """
        Creates a gitHub issue using data, returns json.
        """
    
        r= requests.post(self.issues_url,
                              auth=self.AUTH,
                              headers=self.HEADERS,
                              data=json.dumps(data))
        return r.json() # Better to return object?
        
    def create_standard_review_ticket(self, RCV_id, RCV_name):
        """Post a standard format review ticket"""
        termstring = "%s %s" % (RCV_name, RCV_id)
        title = "Review %s" % termstring
        
        filename = re.sub(' ', '_', termstring)
        anchor = re.sub('(.)', anchor_sub, termstring) 
        results_link = "https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/%s.tsv" % filename
        summary_link = "https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/results_summary.md#" + anchor
        data = {
          "title": title,
          "body": "This ticket is intended for discussion of the definition and mapping of %s\n" \
          "* [Summary of mapping](%s)\n" \
          "* [Results table for mapping](%s)" % (termstring, summary_link, results_link), 
            "milestone": 3,
          "labels": [
            "Mapping_review"
          ]
        }
        return self.create_github_issue(data)
        
    def ticket_exists(self, title, labels=[]):
        """Searches open and closed for issue with specified title.
        If exists, return json, otherwise return False.
        Optionally specify a list of labels, ticket is only returned if all labels match"""
        out = []
        labels = set(labels)
        for i in self.all_issues:
            if i['title'] == title:
                ticket_label_names = set(map(lambda x: x['name'],  i['labels']))
                if ticket_label_names.intersection(labels) == labels:
                    out.append(i)
        return out
    
    
    def get_all_tickets(self, url=False):
        """Populates self.all_issues with a json of all tickets"""
        payload = { 'state': 'all' }
        if not url: # first time around
            url = self.issues_url # Get first page
            self.all_issues = []  # Blank this issues list
        issues = requests.get(url, auth=self.AUTH, params=payload)
        self.all_issues.extend(issues.json())
        links = issues.links
        if 'next' in links:
            self.get_all_tickets(links['next']['url'])
            
    
    def get_milestones(self):
        return

            
            
        
        
    