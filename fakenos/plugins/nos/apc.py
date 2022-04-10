import time

initial_prompt = "{base_prompt}>"

hostname = "{base_prompt}"

about = """
E000: Success
Hardware Factory
---------------
Model Number: 		AP9640
Serial Number: 		ZA123412341234
Hardware Revision: 	5
Manufacture Date: 	01/23/2021
MAC Address: 		28 29 86 47 69 82
Management Uptime: 	16 Days 9 Hours 3 Minutes

Application Module
---------------
Name: 			su
Version: 		v1.4.2.1
Date: 			Dec 15 2020
Time: 			21:10:50

APC OS(AOS)
---------------
Name: 			aos
Version: 		v1.4.2.1
Date: 			Dec 15 2020
Time: 			21:10:50

APC Boot Monitor
---------------
Name: 			boot
Version: 		v1.3.6.1
Date: 			May 11 2021
Time: 			09:07:45
"""

alarmcount = """
E000: Success
AlarmCount: 1
"""

boot = """
E000: Success
Boot Mode:	    manual
DHCP Cookie:	disabled
Vendor Class: 	APC
Client ID: 	    28 29 86 47 69 82
User Class: 	SU

"""

console = """
E000: Success

Boot Mode:	    manual
DHCP Cookie:	disabled
Vendor Class: 	APC
Client ID: 	    28 29 86 47 69 82
User Class: 	SU

apc>console
E000: Success
Telnet:      disabled
SSH:         enabled
Telnet Port: 23
SSH Port:    22
Baud Rate:   9600

"""

date = """
E000: Success
Date: 04/10/2022
Time: 10:14:25
Format: mm/dd/yyyy
Time Zone: -09:00

"""

dns = f"""
E000: Success
Active Primary DNS Server:	    0.0.0.0
Active Secondary DNS Server:	0.0.0.0

Override Manual DNS Settings:	enabled
Primary DNS Server:		        0.0.0.0
Secondary DNS Server:		    0.0.0.0
Domain Name:			        example.com
Domain Name IPv6:		        example.com
System Name Sync: 		        Enabled
Host Name:			            {hostname}

"""

firewall = """
E000: Success
Firewall: 	disabled
File name: 	example.fwl

"""

ftp = """
E000: Success
Service: 	enabled
Ftp Port: 	21

"""

lang = """
E000: Success

Languages
enUs - English
jaJa - 日本語
ruRu - Русский
deDe - Deutsch
zhCn - 中文
frFr - Français
itIt - Italiano
esEs - Español
ptBr - Português
koKo - 한국어

"""

lastrst = """
12 WDT Reset
E000: Success

"""

portspeed = """
E000: Success
Port Speed: Auto_negotiation
Current Port Speed: 1000 Full_Duplex

"""

radius = """
E000: Success
Access: 			        RADIUS, then Local
Primary Server: 		    192.0.2.1
Primary Server Port: 		1812
Primary Server Secret: 		<Password Hidden>
Primary Server Timeout: 	5
Secondary Server: 		    192.0.2.1
Secondary Server Port: 		1812
Secondary Server Secret: 	<Password Hidden>
Secondary Server Timeout: 	5

"""

upsabout = """
E000: Success
Model: Smart-UPS X 1000
SKU: SMX1000
Serial Number: AS12341234
Firmware Revision: UPS 03.8 (ID11)
Manufacture Date: 10/28/2011
Apparent Power Rating: 1000 VA
Real Power Rating: 800 W
Internal Battery SKU: APCRBC116
External Battery SKU: SMX48RMBP2U


"""

session = """
User              Interface         Address           Logged In Time    ID
-------------------------------------------------------------------------------
user              SSH               192.0.2.1         00:07:30          225
E000: Success

"""

smtp = """
E000: Success

  From: 	    address@example.com
  Server: 	    mail.example.com
  Port: 	    25
  Auth: 	    disabled
  User: 	    User
  Password: 	<not set>
  Encryption: 	none
  Req. Cert: 	disabled
  Cert File: 	<n/a>

"""

snmp = """
E000: Success
  SNMPv1:     enabled

Access Control Summary:
  Access Control #:	1
  Community:		public
  Access Type:		read
  Address:		    192.0.2.255

  Access Control #:	2
  Community:		priavte
  Access Type:		read
  Address:		    0.0.0.0

  Access Control #:	3
  Community:		public
  Access Type:		read
  Address:		    0.0.0.0

  Access Control #:	4
  Community:
  Access Type:		disabled
  Address:		    0.0.0.0


"""

snmptrap = """
E000: Success

SNMP Trap Configuration

  Index: 	    1
  Receiver IP: 	192.0.2.1
  Community: 	public
  Trap Type: 	SNMPV1
  Generation: 	enabled
  Auth Traps: 	enabled
  User Name: 	apc snmp profile1
  Language: 	enUs - English


"""

snmpv3 = """
E000: Success
SNMPv3 Configuration
  SNMPV3: 	disabled

SNMPv3 User Profiles

  Index: 		        1
  User Name: 		    apc snmp profile1
  Authentication: 	    None
  Encryption: 		    None

  Index: 		        2
  User Name: 		    apc snmp profile2
  Authentication: 	    None
  Encryption: 		    None

  Index: 		        3
  User Name: 		    apc snmp profile3
  Authentication: 	    None
  Encryption: 		    None

  Index: 		        4
  User Name: 		    apc snmp profile4
  Authentication:   	None
  Encryption: 		    None


SNMPv3 Access Control

  Index: 		        1
  User Name: 		    apc snmp profile1
  Access: 		        disabled
  NMS IP/Host Name: 	0.0.0.0

  Index: 		        2
  User Name: 		    apc snmp profile2
  Access: 		        disabled
  NMS IP/Host Name: 	0.0.0.0

  Index: 		        3
  User Name: 		    apc snmp profile3
  Access: 		        disabled
  NMS IP/Host Name: 	0.0.0.0

  Index: 		        4
  User Name: 		    apc snmp profile4
  Access: 		        disabled
  NMS IP/Host Name: 	0.0.0.0

"""

system = f"""
E000: Success
Host Name Sync: Enabled
Name: 		    {hostname}
Contact: 	    noc@example.com
Location: 	    1234 Any Street, Any City, Any State, USA
Message:
DateTime: 	    04/10/2022:10:36:08
User: 		    username
Up Time: 	    16 Days 9 Hours 26 Minutes
Stat: 		    P+ N4+ N6+ A+
Bootmon: 	    boot:v1.3.6.1
AOS: 		    aos:v1.4.2.1
App: 		    su:v1.4.2.1

"""

tcpip = f"""
E000: Success

Active IPv4 Settings
--------------------
  Active IPv4 Address:		192.0.2.2
  Active IPv4 Subnet Mask:	255.255.255.0
  Active IPv4 Gateway:		192.0.2.1

Manually Configured IPv4 Settings
---------------------------------

  IPv4:			    enabled
  Manual Settings:	enabled

  IPv4 Address:		192.0.2.2
  Subnet Mask:		255.255.255.0
  Gateway:		    192.0.2.1
  MAC Address:		28 29 86 47 69 82
  Domain Name:		example.com
  Host Name:		{hostname}

"""

user = """
E000: Success
Name                    User Type                      Status
----                    ---------                      ------
apc                     Super User                     Enabled

"""

web = """
E000: Success
Http:			        disabled
Https:			        enabled
Http Port: 		        80
Https Port: 		    443
Minimum Protocol:	    TLS1.2
Limited Status Access:	disabled
Lim. Status Page Used:	n/a
TLS1.2 Cipher Suite Filter:	4

"""
commands = {
    "about": {
        "output": about,
        "help": "Display about information",
    },
    "boot": {
        "output": boot,
        "help": "Display boot information",
    },
    "console": {
        "output": console,
        "help": "Display the console configuration",
    },
    "date": {
        "output": date,
        "help": "Display the date and time",
    },
    "dns": {
        "output": dns,
        "help": "Show DNS settings",
    },
    "firewall": {
        "output": firewall,
        "help": "Display firewall settings",
    },
    "ftp": {
        "output": ftp,
        "help": "Display FTP settings",
    },
    "lang": {
        "output": lang,
        "help": "Display language settings",
    },
    "lastrst": {
        "output": lastrst,
        "help": "Display last reset information",
    },
    "portspeed": {
        "output": portspeed,
        "help": "Display port speed settings",
    },
    "radius": {
        "output": radius,
        "help": "Display RADIUS settings",
    },
    "upsabout": {
        "output": upsabout,
        "help": "show ups information",
    },
    "session": {
        "output": session,
        "help": "Display session information",
    },
    "smtp": {
        "output": smtp,
        "help": "Display SMTP settings",
    },
    "snmp": {
        "output": snmp,
        "help": "Display SNMP settings",
    },
    "snmptrap": {
        "output": snmptrap,
        "help": "Display SNMP Trap settings",
    },
    "snmpv3": {
        "output": snmpv3,
        "help": "Display SNMPv3 settings",
    },
    "system": {
        "output": system,
        "help": "Display system information",
    },
    "tcpip": {
        "output": tcpip,
        "help": "Display TCP/IP settings",
    },
    "user": {
        "output": user,
        "help": "Display user information",
    },
    "web": {
        "output": web,
        "help": "Display web settings",
    },
}
