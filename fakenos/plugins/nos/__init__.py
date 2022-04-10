from . import cisco_ios
from . import accedian
from . import apc_nmc

nos_plugins = {
    "cisco_ios": cisco_ios,
    "accedian": accedian,
    "apc": apc_nmc,
}
