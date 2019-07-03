#!/usr/bin/env python3

from hdfs import Client

def main():
   client = Client("http://127.0.0.1:50070",root="/",timeout=100,session=False)
   #client.makedirs("/news")
   client.upload("/input","x.html")
   print(client.list("/"))

if __name__ == "__main__":
  main()
