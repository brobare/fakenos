from cmd import Cmd
import logging
import time
import traceback

log = logging.getLogger(__name__)


class APCShell(Cmd):

    use_rawinput = False

    commands = {
        "exit": {
            "output": True,
            "help": "exist commands shell",
        },
        "default": {
            "output": "E101: Command Not Found",
            "help": "Output to print for unknown commands",
        },
    }

    def __init__(
        self,
        stdin,
        stdout,
        nos,
        base_prompt,
        intro="""


        Schneider Electric                      Network Management Card AOS    v1.4.2.1
        (c) Copyright 2020 All Rights Reserved  Smart-UPS APP                  v1.4.2.1
        -------------------------------------------------------------------------------
        Name      : {hostname}                                Date : 04/10/2022
        Contact   : noc@example.com                           Time : 11:20:01
        Location  : 1234 Any St, Any City, Any St             User : Administrator
        Up Time   : 16 Days 10 Hours 10 Minutes               Stat : P+ N4+ N6+ A+
        -------------------------------------------------------------------------------
        IPv4               : Enabled            IPv6               : Enabled
        Ping Response      : Enabled
        -------------------------------------------------------------------------------
        HTTP               : Disabled           HTTPS              : Enabled
        FTP                : Enabled            Telnet             : Disabled
        SSH/SCP            : Enabled            SNMPv1             : Read-Only
        SNMPv3             : Disabled           Modbus TCP         : Disabled
        BACnet/IP          : Disabled
        -------------------------------------------------------------------------------
        Super User         : Enabled            RADIUS             : Enabled
        Administrator      : 1 Enabled          Device User        : Disabled
        Read-Only User     : Disabled           Network-Only User  : Disabled


        Type ? for command listing
        Use tcpip command for IP address(-i), subnet(-s), and gateway(-g)

        """,
        ruler="",
        completekey="tab",
    ):
        self.nos = nos
        self.ruler = ruler
        self.intro = intro
        self.base_prompt = base_prompt
        self.prompt = nos.initial_prompt.format(base_prompt=base_prompt)
        self.commands.update(nos.commands or {})

        # call the base constructor of cmd.Cmd, with our own stdin and stdout
        super(APCShell, self).__init__(
            completekey=completekey,
            stdin=stdin,
            stdout=stdout,
        )

    def start(self):
        self.cmdloop()

    def stop(self):
        return True

    def writeline(self, value):
        for line in str(value).splitlines():
            self.stdout.write(line + "\r\n")

    def emptyline(self):
        self.stdout.write("")

    def precmd(self, line):
        return line

    def postcmd(self, stop, line):
        return stop

    def default(self, command):
        """Method called if no do_xyz methods found"""
        log.debug("shell.run_command running command '{}'".format(command))
        try:
            cmd_data = self.commands[command]
            ret = cmd_data["output"]
            if callable(ret):
                ret = ret(
                    base_prompt=self.base_prompt,
                    current_prompt=self.prompt,
                    command=command,
                )
            if "new_prompt" in cmd_data:
                self.prompt = cmd_data["new_prompt"].format(
                    base_prompt=self.base_prompt
                )
        except KeyError:
            try:
                if self.commands.get("default"):
                    ret = self.commands["default"]["output"]
                    if callable(ret):
                        ret = ret(
                            base_prompt=self.base_prompt,
                            current_prompt=self.prompt,
                            command=command,
                        )
                else:
                    ret = "Undefined command"
            except:
                ret = traceback.format_exc()
                ret = ret.replace("\n", "\r\n")
        except:
            ret = traceback.format_exc()
            ret = ret.replace("\n", "\r\n")

        # returning True will close the shell
        if ret is True:
            return True
        # if not None, wite output to stdout
        elif ret is not None:
            self.writeline(ret)
