import time

initial_prompt = "{base_prompt}: "


def make_show_clock(base_prompt, current_prompt, command):
    return time.time()


board_show_info = """

Product name       : AEN-1000-GE
MAC base address   : 00:15:AD:16:5F:38
Unit identifier    : {hostname}
Firmware version   : AEN_4.9.3.2_30737
Serial number      : G123-1234
Assembly           : 500-005-14:8:2:00

"""
interface_show = """

Interface name    State    DHCP     IP address      Netmask         Gateway         Info
----------------- -------- -------- --------------- --------------- --------------- --------------
Management        Enabled  Disabled 192.168.1.254   255.255.255.0   ---             ---
Network           Enabled  Disabled 10.0.0.2        255.255.255.0   10.0.0.1        VLAN ID: 2
Auto              Disabled Disabled ---             255.255.255.0   ---             Auto interface

"""


port_show_status = """

Status Connector  Port name         State    Speed     MDI
------ ---------- ----------------- -----    --------- ----
Down   SFP-A      Monitor-1         Enabled  No-link   ---
Down   SFP-B      Monitor-2         Enabled  No-link   ---
Down   Management Management        Enabled  No-link   ---
Down   RJ45-A     Client            Enabled  No-link   ---
Up     RJ45-B     Network           Enabled  1G-FD     MDIX

"""

port_show_configuration = """

Connector  Port name         State    Speed     MTU   MDI  MAC address
---------- ----------------- -----    --------- ----- ---- -----------------
SFP-A      Monitor-1         Enabled  Auto      2000  Auto 00:15:AD:16:5F:3C
SFP-B      Monitor-2         Enabled  Auto      2000  Auto 00:15:AD:16:5F:3D
Management Management        Enabled  Auto      2000  Auto 00:15:AD:16:5F:3B
RJ45-A     Client            Enabled  Auto      2000  Auto 00:15:AD:16:5F:3E
RJ45-B     Network           Enabled  Auto      2000  Auto 00:15:AD:16:5F:3F

"""


commands = {
    "session writelock": {
        "output": None,
        "new_prompt": "{base_prompt}# ",
        "help": "enter exec prompt",
    },
    "board show info": {
        "output": board_show_info,
        "help": "show board information",
    },
    "interface show": {
        "output": interface_show,
        "help": "show interface information",
    },
    "port show status": {
        "output": port_show_status,
        "help": "show port information",
    },
    "port show configuration": {
        "output": port_show_configuration,
        "help": "show port configuration",
    },
}
