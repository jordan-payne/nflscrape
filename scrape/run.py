#!/usr/bin/env python
import argparse

p = argparse.ArgumentParser(description='Scrape data from NFLGSIS.')
p.add_argument('--username', metavar='U', type=str, required=True, nargs=1, help='your username for NFLGSIS.')
p.add_argument('--password', metavar='P', type=str, required=True, nargs=1, help='your password for NFLGSIS.')
p.add_argument('-g', metavar='YYYY', type=int, required=False, nargs=1, help='collect gamebooks for specific NFL season.')
args = p.parse_args()

def main():
    p.print_help()
    print args.username
    print args.g

if __name__ == "__main__":
    main()
