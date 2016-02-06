#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime
import csv
import os

from credentials import INSTANCE_URL, TOKEN
from v1pysdk import V1Meta

statuses = [
    'Not Started',
    'Ready for Dev',
    'Developing',
    'Ready for Test',
    'Testing',
    'Tested',
]

select_template = "Workitems:PrimaryWorkitem[Status.Name='{0}'].Estimate.@Sum"


def parsedate(d):
    return datetime.datetime.strptime(d, "%Y-%m-%d")


def as_of_times(start, end, hoursper=6):
    current = start
    while current <= end:
        yield current
        current += datetime.timedelta(hours=hoursper)


if __name__ == "__main__":
    sprintName = 'Sprint 1'
    with V1Meta(instance_url=INSTANCE_URL, token=TOKEN) as v1:
        timebox = (v1.Timebox
                   .where(Name=sprintName)
                   .select("BeginDate", "EndDate")
                   .first())
        startdate = parsedate(timebox.BeginDate)
        enddate = parsedate(timebox.EndDate) + datetime.timedelta(days=1)
        individual_times = as_of_times(startdate, enddate)
        select_list = [select_template.format(status) for status in statuses]
        results = (v1.Timebox
                   .asof(individual_times)
                   .where(Name=sprintName)
                   .select(*select_list))
        outfilename = os.path.join("output.dat")
        with open(outfilename, "w") as outfile:
            writer = csv.writer(outfile, delimiter="|")
            writer.writerow(['# Date'] + statuses)
            for result in results:
                for select_term in select_list:
                    try:
                        row = result.data[select_term]
                        writer.writerow([result.data['AsOf']] + row)
                    except KeyError, kex:
                        print "No key {!s} in {!r}".format(kex, result)
