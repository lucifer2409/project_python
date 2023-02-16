echo "Enter the operation you want to be performed :\n"
echo "1:if config \n 2:ping command \n 3:dig command \n 4:Netstat command"
read operation
case "$operation" in
	1)ifconfig;;
	2)echo "Enter the url / ipaddress you want to ping:"
	       read url_1
       	       ping -c 12 $url_1;;	       
	3)echo "Enter the url or ip-address you want to dig :"
		read url_ip
		dig $url_ip;;
	4)echo "Enter the url or ip-address you want to perform netstat command on :"
		read url
		netstat $url;;
esac

	
