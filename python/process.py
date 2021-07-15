#!/usr/bin/python

import sys
import csv

fields = ["Step", "Time", "Scale-factor", "Redshift", "Time-step", "Time-bins", "", "Updates", "g-Updates", "s-Updates", "Sink-Updates", "b-Updates", "Wall-clock time [ms]", "Props", "Cumulative wall-clock time"]
values = []

wallclock = 0.0
with open(sys.argv[1], "r") as in_file:
    for _ in range(14):
        next(in_file)
    
    l = in_file.readline()
    while l:
        d = l.split()
        wallclock += float(d[12])
        d.append(wallclock)
        values.append(d)
        l = in_file.readline()

with open(sys.argv[1][:-3]+"csv", "x") as out_file:
    write = csv.writer(out_file)
    write.writerow(fields)
    write.writerows(values)
