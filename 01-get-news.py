#!/usr/bin/env python3

import requests 
import re

def main():
  url = "http://news.baidu.com/"
  header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
  }
  resp = requests.get(url, headers=header)
  data = resp.content.decode("utf-8")
  
  pattern = re.compile("""<a href="(.*)" mon="(.*)" target="_blank">(.*)</a>""")
  ret = pattern.findall(data)
  lst = []
  for i in ret:
    x = (i[0],i[-1])
    lst.append(x)

  html = """<html>
<head></head>
<body>
<h3>news site</h3>
<ul>
"""
  for i in lst:
    html += """<li><a href="""
    html += i[0]
    html += """">""" 
    html += i[1]
    html += """</a></li>""" 
  html += """</ul></body></html>""" 


  with open("01.html", "w", encoding = "utf-8") as f:
    f.write(html)

if __name__ == "__main__":
  main()
