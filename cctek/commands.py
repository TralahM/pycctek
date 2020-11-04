"""Console Scripts Entry Points For cctek Distribution."""
import cctek
import argparse
import yaml


def luhn_check(args):
    """Run Luhn Algorithm checks on the card numbers."""
    for c in args.cards:
        res = {str(c): cctek.luhn_checker(c)}
        print(yaml.dump(res))
    return


def lookup_bin(args):
    """Lookup Issuer Identification Numbers."""
    for b in args.bins:
        res = cctek.bin_checker(b)
        print(yaml.dump(res))
    return


def random_card(args):
    """Generate a random credit card number of the specified type."""
    fmap = {
        "amex": cctek.random_amex_card,
        "diners": cctek.random_carteblanche_diners_card,
        "discover": cctek.random_discover_card,
        "enroute": cctek.random_enroute_card,
        "mastercard": cctek.random_euro_mastercard,
        "jcb": cctek.random_jcb_card,
        "visa": cctek.random_visa_card,
    }
    print(fmap.get(args.card_type)())
    return


def usage(*args, **kwargs):
    """Use Default function to handle empty namespace."""
    return


def main():
    """Run Main Command Executor."""
    parser = argparse.ArgumentParser()
    parser.set_defaults(func=usage)
    parser.add_argument(
        "--version", action="version", version=f"cctek {cctek.__version__}"
    )
    subparsers = parser.add_subparsers()
    # random card subparser card_type
    random_card_parser = subparsers.add_parser(
        "random_card",
        aliases=[
            "rc",
        ],
        help="""Generate a random credit card number of the specified type.""",
    )
    random_card_parser.set_defaults(func=random_card)
    random_card_parser.add_argument(
        "card_type",
        choices=[
            "amex",
            "diners",
            "discover",
            "enroute",
            "jcb",
            "mastercard",
            "visa",
        ],
    )
    # luhn checker subparser cards
    luhn_parser = subparsers.add_parser(
        "luhn",
        aliases=[
            "ln",
        ],
        help="""Run Luhn Algorithm checks on the card numbers.""",
    )
    luhn_parser.set_defaults(func=luhn_check)
    luhn_parser.add_argument(
        "cards",
        help="""Credit Card Numbers or Bank/Issuer Identification Numbers to Lookup.""",
        nargs="+",
        metavar="credit_card_number(s)",
    )
    # lookup bin subparser bins
    lookup_bin_parser = subparsers.add_parser(
        "lookup",
        aliases=[
            "lk",
        ],
        help="""Lookup Issuer Identification Numbers.""",
    )
    lookup_bin_parser.set_defaults(func=lookup_bin)
    lookup_bin_parser.add_argument(
        "bins",
        help="""Credit Card Number or Bank/Issuer Identification Number(first 6
        digits) to Lookup.""",
        nargs="+",
        metavar="BIN(s)",
    )
    # parse the args
    args = parser.parse_args()
    args.func(args)
    return
