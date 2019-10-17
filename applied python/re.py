import re
a = re.findall(r"\d[3]-\d[2]-\d[]2", "asd, ass: 222-23-44")
r = re.compile(r"\d[3]-\d[2]-\d[]2")
res = r.findall("asd, ass: 222-23-44")
