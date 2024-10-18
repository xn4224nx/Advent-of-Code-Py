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


def read_ip_addresses(file_path: str) -> list[dict[str:[str]]]:
    """
    Read and parse an IP address file into a list of tuples of the
    three string parts of the address.
    """
    ip_adrs = []

    with open(file_path) as fp:

        # Extract the two parts of the ip address for each line
        for line in fp.readlines():
            all_brack = []
            all_out_brack = []

            brack_txt = ""
            out_brack_txt = ""
            in_brack = False

            # For each line in the file
            for char in line:
                if char == "\n":
                    break

                elif char == "[":
                    in_brack = True

                    # When entering a bracket save the text outside
                    if len(out_brack_txt) > 0:
                        all_out_brack.append(out_brack_txt)
                        out_brack_txt = ""

                elif char == "]":
                    in_brack = False

                    # When exiting a bracket save the text outside
                    if len(brack_txt) > 0:
                        all_brack.append(brack_txt)
                        brack_txt = ""

                elif in_brack:
                    brack_txt += char

                else:
                    out_brack_txt += char

            # If the end of the string has been reached save the result.
            if len(out_brack_txt) > 0:
                all_out_brack.append(out_brack_txt)

            if len(brack_txt) > 0:
                all_brack.append(brack_txt)

            ip_adrs.append({"brack_txt": all_brack, "out_brack_txt": all_out_brack})

    return ip_adrs


def str_has_abba(ip_part: str) -> bool:
    """
    Determine if a part of an ip address is a pair of two different characters
    followed by the reverse of that pair.
    """
    for idx in range(3, len(ip_part)):

        # Check to see that the first char equals the last and the two inside
        # chars are equal and all four chars are not the same.
        if (
            ip_part[idx - 3] == ip_part[idx]
            and ip_part[idx - 2] == ip_part[idx - 1]
            and ip_part[idx] != ip_part[idx - 1]
        ):
            return True

    # If the end of the string has been reached and no abba has been found.
    else:
        return False


def supports_tls(ip_addr: dict[str:[str]]) -> bool:
    """
    Does a supplied IP address support TLS?
    """

    # If the internal text has a abba it can never support TLS.
    for inter_addr in ip_addr["brack_txt"]:
        if str_has_abba(inter_addr):
            return False

    # Then in the external text has abba it will support TLS.
    for ext_addr in ip_addr["out_brack_txt"]:
        if str_has_abba(ext_addr):
            return True

    # If neither group has abba it can't support TLS.
    else:
        return False


def count_valid_ip(all_ips: list[(str, str, str)]) -> int:
    """
    Count the number of IP addresses that support TLS.
    """
    return sum([supports_tls(x) for x in all_ips])


if __name__ == "__main__":
    addr = read_ip_addresses("./data/input.txt")
    print(f"Part 1 = {count_valid_ip(addr)}")
