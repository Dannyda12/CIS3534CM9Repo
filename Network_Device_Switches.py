#!/usr/bin/env python3
# Network_Devices_Switches.py
# CIS3534C - Module 7
# Switch class inheriting from NetworkDevice

from networkdevice import NetworkDevice


class Switch(NetworkDevice):
    """A network switch that inherits from NetworkDevice"""

    # class variable to count switches
    __switch_count = 0

    def __init__(self, IPaddr, MACaddr, hostname, default_gateway):
        # initialize parent (validates IP + stores MAC)
        super().__init__(IPaddr, MACaddr)

        # private attributes
        self.__hostname = hostname
        self.__default_gateway = self.validateIP(default_gateway)

        # increment switch counter
        Switch.__switch_count += 1

    # getter/setter for hostname
    def getHostname(self):
        return self.__hostname

    def setHostname(self, hostname):
        self.__hostname = hostname

    # getter/setter for default gateway
    def getDefaultGateway(self):
        return self.__default_gateway

    def setDefaultGateway(self, gateway):
        self.__default_gateway = self.validateIP(gateway)

    # class method to track number of switches
    @classmethod
    def getSwitchCount(cls):
        return cls.__switch_count

    # string output (matches assignment format)
    def __str__(self):
        return (f"IP address {self.getIPaddr()}; MAC address {self.getMACaddr()}\n"
                f"    hostname: {self.__hostname}, default gateway {self.__default_gateway}")


# ---------------- TEST CODE ----------------
def main():
    s1 = Switch("192.168.1.99", "AA:BB:CC:DD:EE:FF", "switch1", "192.168.1.1")
    print("Your switch:", s1)
    print()

    s2 = Switch("888.888.888.888", "AA:BB:CC:11:22:33", "Switch Name Unknown", "192.168.1.1")
    print("Your switch:", s2)
    print()

    s1.setHostname("WavyBlue")
    print("Your updated switch:", s1)

    print(f"You created {Switch.getSwitchCount()} switches today!")


if __name__ == "__main__":
    main()
