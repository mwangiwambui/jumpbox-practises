`id`
Used to check user group and id

`curl https://www.random.co.ke/some-file.txt -O`
Linux command used to download files from the internet.

`wget http://www.some-site/some-file.txt -O some-file.txt`
used to download a file from the internet

`ls /etc/*release* `
to check the os-version
 
 `cat /etc/*release*`
 to see more details about the OS

 # Package Management
 `rpm -i telnet.rpm`
 To install a package

 `rpm -e telnet.rpm`
 To uninstall a package

 `rpm -q telnet.rpm`
 To query a package

 RPM does not look at the dependencies needed by various packages.

 YUM is best because it installs the package and all its dependencies.
  `yum --showduplicates list package`

  to see a list of available package versions.

`yum install package-versionName`
To install a specific version of a package.