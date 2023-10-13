`ps aux`
Used to run view all linux process, the users running the process, including the processes that do not have a TTY.

`top`
The command used to give a more real time view of the processes running your machine.

`ps l`
where the l is the long format. Gives an even more detailed view of the process. Including the parent ID.

`nice -n 5 apt upgrade`
Used to set the niceness level of a process.

`renice 10 -p {pid}`
Used to set the niceness level of an existing process.

`cat /proc/{pid}/status`
Used to see more information about a process. All details about process are stores in the /proc partition.

`jobs`
Used to view the commands sent to the background and the status of the commands sent to the background.

`bg`
Send an existing job to the background after you temporarily suspend it with CTRL+Z

`fg {pid}`
To bring a job to the foreground with a pid.



