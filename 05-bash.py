#!/usr/bin/env python3

import os

def main():
  cmd = "/usr/local/hadoop/bin/hdfs dfs -ls /"
  os.system(cmd)

if __name__ == "__main__":
  main()
