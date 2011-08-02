# get-shit-done
get-shit-done is an easy to use command line program that blocks websites known to distract us from our work.

After cloning this repository, put it in your $PATH and ensure it is executable.

Execute it as root because it modifies your hosts file and restarts your network daemon (if any).

## To get-shit-done
`sudo get-shit-done work`

## To no longer get-shit-done
`sudo get-shit-done play`

### $siteList
Add or remove elements of this array for sites to block or unblock.

### ./hosts.list
List all domains (one per line) to deny.

### $restartNetworkingCommand
Update this variable with the path to your network daemon along with any parameters needed to restart it.

### $hostsFile
Update this variable to point to the location of your hosts file. Make sure it is an absolute path.

# Updates
It's amazing how fast this repository has grown, I had never expected a single link on Hacker News would have caused that! I love it.

I'd really love if anyone wanted to follow some of my other repositories, including [jolt](https://github.com/leftnode/jolt) or [dbmigrator](https://github.com/leftnode/dbmigrator). I think both are promising projects and I know I could use some help on them.

Thanks!

-Vic Cherubini
