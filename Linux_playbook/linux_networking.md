` cat /proc/sys/net/ipv4/ip_forward `
File used to configure the configurations for ip forwarding. The default value is set to 0

` echo 1 > /proc/sys/net/ipv4/ip_forward `
Sets the forwarding value to 1

`ip link`
List and modify interfaces on the host

`ip addr`
See the ip addresses assined to the interfaces on the device.

`ip addr add`
Used to add ips to an interface

=================================

` cat /etc/nsswitch.conf`
Used to determine the order at which DNS records should be searched, e.g. first file(/etc/hosts) then dns nameserver
