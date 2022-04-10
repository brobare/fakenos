import time

initial_prompt = "{base_prompt}>"


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

commands = {
    "upsabout": {
        "output": upsabout,
        "help": "show ups information",
    },
}
