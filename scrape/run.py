#!/usr/bin/env python
import argparse
import nflcollect

p = argparse.ArgumentParser(description='Scrape data from NFLGSIS.')
p.add_argument('-u', '--username', metavar='U', type=str, required=True, help='your username for NFLGSIS.')
p.add_argument('-p','--password', metavar='P', type=str, required=True, help='your password for NFLGSIS.')
p.add_argument('-g', '--gamebook', dest='seasons', metavar='YYYY', type=int, required=False, nargs='+', help='collect gamebooks for specific NFL season(s).')
args = p.parse_args()

def main():
    if args.seasons:
        driver = nflcollect.get_driver()
        print 'Logging into NFLGSIS...'
        driver = nflcollect.login_nflgsis(driver, args.username, args.password)
        print 'Success'
        for season in args.seasons:
            gamebooks = nflcollect.get_gamebooks_for_year(season, driver)
            nflcollect.write_gamebooks(gamebooks)
        driver.close()

if __name__ == "__main__":
    main()
