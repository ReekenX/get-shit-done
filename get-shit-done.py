#!/usr/bin/env python

from __future__ import print_function
import sys
import getpass
import subprocess
import os


def exit_error(error):
    print(error, file=sys.stderr)
    exit(1)

list_file = os.path.join(os.getcwd(), "hosts.list")

if "linux" in sys.platform:
    restart_network_command = ["echo", "-n"]
elif "darwin" in sys.platform:
    restart_network_command = ["dscacheutil", "-flushcache"]
else:
    # Intention isn't to exit, as it still works, but just requires some
    # intervention on the user's part.
    message = '"Please contribute DNS cache flush command on GitHub."'
    restart_network_command = ['echo', message]

hosts_file = '/etc/hosts'
start_token = '## start-gsd'
end_token = '## end-gsd'
default_sites = ['reddit.com', 'digg.com', 'break.com', 'news.ycombinator.com',
                 'twitter.com', 'facebook.com', 'blip.com', 'youtube.com',
                 'vimeo.com', 'delicious.com', 'flickr.com', 'friendster.com',
                 'hi5.com', 'linkedin.com', 'livejournal.com', 'plurk.com',
                 'stumbleupon.com', 'slashdot.org']


def sites_from_file(filename):
    if os.path.exists(filename):
        site_list = []
        file_handle = open(filename)
        for line in file_handle.readlines():
            site_list.append(line.strip())
        return site_list
    else:
        raise Exception('No list file in the user home dir')


def rehash():
    subprocess.check_call(restart_network_command)


def work():
    hFile = open(hosts_file, 'a+')
    contents = hFile.read()

    site_list = sites_from_file(list_file)

    if start_token in contents and end_token in contents:
        exit_error("Work mode already set.")

    print(start_token, file=hFile)

    # remove duplicates by converting list to a set
    for site in set(site_list):
        print("127.0.0.1\t" + site, file=hFile)
        print("127.0.0.1\twww." + site, file=hFile)

    print(end_token, file=hFile)

    rehash()


def play():
    hosts_file_handle = open(hosts_file, "r+")
    lines = hosts_file_handle.readlines()

    startIndex = -1

    for index, line in enumerate(lines):
        if line.strip() == start_token:
            startIndex = index

    if startIndex > -1:
        lines = lines[0:startIndex]

        hosts_file_handle.seek(0)
        hosts_file_handle.write(''.join(lines))
        hosts_file_handle.truncate()

        rehash()


def main():
    if getpass.getuser() != 'root':
        exit_error('Please run script as root.')
    if len(sys.argv) != 2:
        exit_error('usage: ' + sys.argv[0] + ' [work|play]')
    {"work": work, "play": play}[sys.argv[1]]()


if __name__ == "__main__":
    main()
