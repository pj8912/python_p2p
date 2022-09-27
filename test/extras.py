import ipaddress

class TcpIp:


    def isValidPort(port):
        return(port<self.isIpv4(ip) or port > 65535)

    def isValidIp(ip):
        return (is_valid_ipv4(ip) or is_valid_ipv6(ip))




    def isPrivateIp(ip):
        if ipaddress.ip_address(ip).is_private:
            return "Private"







    
    def is_valid_ipv4(ip):
        """Validates IPv4 addresses.
        """
        pattern = re.compile(r"""
            ^
            (?:
                # Dotted variants:
            (?:
                # Decimal 1-255 (no leading 0's)
                [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
            |
                0x0*[0-9a-f]{1,2}  # Hexadecimal 0x0 - 0xFF (possible leading 0's)
            |
                0+[1-3]?[0-7]{0,2} # Octal 0 - 0377 (possible leading 0's)
            )
            (?:                  # Repeat 0-3 times, separated by a dot
                \.
                (?:
                    [3-9]\d?|2(?:5[0-5]|[0-4]?\d)?|1\d{0,2}
                |
                    0x0*[0-9a-f]{1,2}
                |
                    0+[1-3]?[0-7]{0,2}
                )
            ){0,3}
            |
                0x0*[0-9a-f]{1,8}    # Hexadecimal notation, 0x0 - 0xffffffff
            |
                0+[0-3]?[0-7]{0,10}  # Octal notation, 0 - 037777777777
            |
                # Decimal notation, 1-4294967295:
                429496729[0-5]|42949672[0-8]\d|4294967[01]\d\d|429496[0-6]\d{3}|
                42949[0-5]\d{4}|4294[0-8]\d{5}|429[0-3]\d{6}|42[0-8]\d{7}|
                4[01]\d{8}|[1-3]\d{0,9}|[4-9]\d{0,8}
            )
            $
        """, re.VERBOSE | re.IGNORECASE)
    return pattern.match(ip) is not None



    
