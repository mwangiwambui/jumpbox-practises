`cat /proc/cpuinfo`
Check cpu info, if linux is slow

`lscpu`
To check more of cpu usage

`services --status-all`
To check which services started at boot time.

`chkconfig --list`
Also used to list services started at boot time

`sudo systemctl list-unit-files --state=enabled`
Command to check services at start time for systemd