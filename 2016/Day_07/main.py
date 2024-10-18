"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP
addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to
figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two
different characters followed by the reverse of that pair, such as xyyx or
abba. However, the IP also must not have an ABBA within any hypernet sequences,
which are contained by square brackets.

PART 1: How many IPs in your puzzle input support TLS?
"""


def read_ip_addresses(file_path: str) -> list[(str, str, str)]:
    """
    Read and parse an IP address file into a list of tuples of the
    three string parts of the address.
    """
    pass


def str_has_abba(ip_part: str) -> bool:
    """
    Determine if a part of an ip address is a pair of two different characters
    followed by the reverse of that pair.
    """
    pass


def supports_tls(ip_address: (str, str, str)) -> bool:
    """
    Does a supplied IP address support TLS?
    """
    pass


def count_valid_ip(all_ips: list[(str, str, str)]) -> int:
    """
    Count the number of IP addresses that support TLS.
    """
    pass


if __name__ == "__main__":
    pass
