#! /usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re
import csv


def main():
    fields = ['bill id', 'chamber', 'committee', 'sponsor']

    url = "https://www.congress.gov/search?pageSize=250&q=%7B%22" \
          "congress%22%3A%22117%22%2C%22bill-status%22%3A%22law%" \
          "22%2C%22house-committee%22%3A%22Veterans%27+Affairs%2" \
          "2%7D"

    response = requests.get(url)  # GET request
    html = response.content  # document
    soup = BeautifulSoup(html, "html.parser")  # soup object

    # ------------------------------------------------------------------------------

    # EXTRACT BILL ID

    bill_id_list = []
    bill_id_tags = soup.find_all('span', class_='result-heading')

    for bill_tag in range(len(bill_id_tags)):
        if bill_tag % 2 == 0:
            bill_id_list.append(bill_id_tags[bill_tag].contents[0].string)

        # ------------------------------------------------------------------------------

        # EXTRACT COMMITTEE

    committee_list = []
    committee_tags = soup.find_all('span', class_='result-item')

    for committee_tag in committee_tags:
        if committee_tag.contents[2].string is not None:
            if committee_tag.contents[2].string.strip() != '':
                committee_list.append(committee_tag.contents[2].string.strip())

    for element in committee_list:
        if element == 'The House Rules Committee Print':
            committee_list.remove(element)

        # ------------------------------------------------------------------------------

        # EXTRACT SPONSORS

    sponsors_list = []
    sponsor_list = []
    sponsor_tags = soup.find_all('a', target="_blank")

    # parsing rep and sen names from a longer string

    for i in range(len(sponsor_tags)):
        sponsor_rep = re.search(r'Rep\.\s[a-zA-Z\s]+,.+\[',
                                str(sponsor_tags[i].contents[0]))
        sponsor_sen = re.search(r'Sen\.\s[a-zA-Z\s]+,.+\[',
                                str(sponsor_tags[i].contents[0]))
        if sponsor_rep:
            snippet_rep = sponsor_rep.group(0)
            sponsor_list.append(snippet_rep[5:len(snippet_rep) - 2])
        if sponsor_sen:
            snippet_sen = sponsor_sen.group(0)
            sponsor_list.append(snippet_sen[5:len(snippet_sen) - 2])

    for j in range(len(sponsor_list)):
        if j % 2 == 0:
            sponsors_list.append(sponsor_list[j])

    """Myriam"""
    # rows, cols = (len(bill_id_list), 3)
    # arr = [[0] * cols] * rows

    """Brett"""
    chamber_list = []
    for i in range(len(committee_list)):
        line = committee_list[i].split(' - ')
        chamber_list.append(line[0])
        delimiter_1 = ' | '
        delimiter_2 = '; '
        if delimiter_1 in line[1]:
            partitioned = line[1].partition(delimiter_1)
            line[1] = partitioned[0]
        if delimiter_2 in line[1]:
            partitioned = line[1].partition(delimiter_2)
            line[1] = partitioned[0]
        committee_list[i] = line[1]

    full_list = []

    for bill, chamber, committee, sponsor in zip(bill_id_list, chamber_list,
                                                 committee_list, sponsors_list):
        full_list.append([bill, chamber, committee, sponsor])

    """Brett Testing"""
    # print(bill_id_list)
    # print(len(bill_id_list))
    # print(committee_list)
    # print(len(committee_list))
    # print(sponsors_list)
    # print(len(sponsors_list))
    # print(full_list)

    """Myriam"""
    # for row in range(len(bill_id_list)):
    #     arr[row][0] = bill_id_list[row]
    #     arr[row][1] = committee_list[row]
    #     arr[row][2] = sponsors_list[row]
    #     print(arr[row])  # trying to get each line of output from
    #     # this print statement into each row of
    #     # a csv file
    #
    # with open('bills.csv', 'w', encoding='utf8') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(fields)
    #     writer.writerow(arr)

    """Brett"""
    with open('bills.csv', 'w', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        for item in full_list:
            writer.writerow(item)


if __name__ == '__main__':
    main()
