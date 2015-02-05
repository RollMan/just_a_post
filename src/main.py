import dropbox
import init
import datetime

client = init.Init()
d = datetime.datetime.today()

content = raw_input("Input here: ")
date = "{:0>4}{:0>2}{:0>2}{:0>2}{:0>2}{:0>2}.txt".format(d.year, d.month, d.day, d.hour, d.minute, d.second)
f = open(date, "w")
print date
f.write(content)
f.close()

print date
f = open(date, "rb")
response = client.put_file(date, f)
print response
