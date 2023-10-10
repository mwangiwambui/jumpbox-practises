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