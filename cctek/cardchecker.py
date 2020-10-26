#!/usr/bin/env python
"""CreditCardChecker."""

import re
import random
from . import dataloader


def bin_checker(card):
    """The first 6 digit of a card is known as BIN Number.


    BIN stands for Bank Identification Number.
    It's a 6 digit code which identifies the financial institution that issued the Card to the card holder.
    It also referred as IIN (Issuer Identification Number).
    BIN can be used to identify issuing financial institution of a Credit Card, Debit Card, Prepaid Card and rewards Card.
    Credit & Debit Card Number Format
    As per ISO/IEC 7812, the length of Credit & Debit Card number can be upto 19 digits.
    PQQQQRRRRRRRRRRRS

    P - Major industry Identifier

    Q - Issuing Financial Institution identifier

    R - Account Identifier up to 12 digits

    S - Checksum to validate Card Number.

    Where PQQQQQ combined are known as BIN number or IIN code.

    Uses of BIN Number
    It is commonly used by merchants to identify the card type and issuing bank of the Credit Card.

    It also helps in preventing Fraud. In case the Billing Address and the issuing country of the card is different, it may be a fraudulent transaction. With BIN search they can easily identify such transactions.
    """
    return dataloader.load_iin(card).get(card[:6])


def luhn_checker(card, debug=False):
    """Validate whether credit card number satisfies luhn's algorithm.

    set debug to True to print debugging details like calculated checksum digit,
    PAN(Primary Account Number) and Whole Card String.
    Only when a valid checksum is validated do we output the whole card: else
    just calculated checksum and expected checksum.
    Return True else False
    """
    odd_digits = card[0:-1:2]
    even_digits = card[1:-1:2]
    # Double odd_digits
    dbl_odd_digits = [int(x) * 2 for x in odd_digits]
    # subtract 9 from dbl_digits if digit is >10 else remain same
    dbl_less_nine = [j if j < 10 else j - 9 for j in dbl_odd_digits]
    even_digits_as_Z = [int(x) for x in even_digits]
    # calculate checksum using 10-( sum(of even_digits+dbl_less_nine) % 10)
    checksum = 10 - ((sum(even_digits_as_Z) + sum(dbl_less_nine)) % 10)
    # Get The PAN (Primary Account Number)
    # from the 7th digit of the card number
    # If the Checksum is equal to the last digit of card, then it satisfies
    # luhns algorithm so we return true else false.
    if str(checksum) == card[-1]:
        if debug:
            PAN = card[6:]  # Not used in calculation FYI
            print(f"Card:\t{card}")
            print(f"PAN:\t{PAN}")
            print(
                f"Calculated Checksum:\t{checksum} \tExpected Checksum:{card[-1]}")
        return True
    else:
        if debug:
            print(
                f"Calculated Checksum:\t{checksum} \tExpected Checksum:{card[-1]}")
        return False


def random_euro_mastercard():
    # 5[1-5][0-9]{14}
    a = range(1, 6)
    b = range(0, 10)
    prefix = f"5{random.choice(a)}"
    suffix = "".join([str(random.choice(b)) for i in range(14)])
    return prefix + suffix


# 4([0-9]{12}|[0-9]{15})
def random_visa_card():
    b = range(0, 10)
    prefix = "4"
    suffix = random.choice(
        [
            "".join([str(random.choice(b)) for i in range(12)]),
            "".join([str(random.choice(b)) for i in range(15)]),
        ]
    )
    return prefix + suffix


# 3[47][0-9]{13}
def random_amex_card():
    a = [4, 7]
    b = range(0, 10)
    prefix = f"3{random.choice(a)}"
    suffix = "".join([str(random.choice(b)) for i in range(13)])
    return prefix + suffix


# 3(0[0-5][0-9]{11}|[68][0-9]{12})
def random_carteblanche_diners_card():
    prefix = "3"
    b = range(0, 10)
    suffix = random.choice(
        [
            f"0{random.choice(range(6))}"
            + "".join([str(random.choice(b)) for i in range(11)]),
            f"{random.choice([6,8])}"
            + "".join([str(random.choice(b)) for i in range(12)]),
        ]
    )
    return prefix + suffix


# 6011[0-9]{12}
def random_discover_card():
    b = range(0, 10)
    return "6011" + "".join(str(random.choice(b)) for i in range(12))


# (3[0-9]{15}|(2131|1800)[0-9]{11})
def random_jcb_card():
    b = range(0, 10)
    return random.choice(
        [
            "3" + "".join(str(random.choice(b)) for i in range(15)),
            "2131" + "".join(str(random.choice(b)) for i in range(11)),
            "1800" + "".join(str(random.choice(b)) for i in range(11)),
        ]
    )


# 2(014|149)[0-9]{11}
def random_enroute_card():
    b = range(0, 10)
    return random.choice(
        [
            "2014" + "".join(str(random.choice(b)) for i in range(11)),
            "2149" + "".join(str(random.choice(b)) for i in range(11)),
        ]
    )


def get_cc_type(pattern: str) -> list:
    if re.match("5[1-5][0-9]{14}", pattern):
        return ["MASTERCARD", "EUROCARD", "EUROCARD/MASTERCARD"]

    if re.match("4([0-9]{12}|[0-9]{15})", pattern):
        return [
            "VISA",
        ]

    if re.match("3[47][0-9]{13}", pattern):
        return ["AMEX", "AMERICANEXPRESS", "AMERICAN EXPRESS"]

    if re.match("3(0[0-5][0-9]{11}|[68][0-9]{12})", pattern):
        return ["DINERS", "DINERSCLUB", "DINERS CLUB", "CARTEBLANCHE", "CARTE BLANCHE"]

    if re.match("6011[0-9]{12}", pattern):
        return [
            "DISCOVER",
        ]

    if re.match("(3[0-9]{15}|(2131|1800)[0-9]{11})", pattern):
        return [
            "JCB",
        ]

    if re.match("2(014|149)[0-9]{11}", pattern):
        return [
            "ENROUTE",
        ]
    return [
        "UKNOWN",
    ]


def validate_cvv_format(cvv: str, cardType: str):
    """Validate a card verification value format.

    * This method only checks for the format. It doesn't
    * validate that the value is the one on the card.
    *
    * CVV is also known as
    *  - CVV2 Card Validation Value 2 (Visa)
    *  - CVC  Card Validation Code (MasterCard)
    *  - CID  Card Identification (American Express and Discover)
    *  - CIN  Card Identification Number
    *  - CSC  Card Security Code
    *
    * Important information regarding CVV:
    *    If you happen to have to store credit card information, you must
    *    NOT retain the CVV after transaction is complete. Usually this
    *    means you cannot store it in a database, not even in an encrypted
    *    form.
    *
    * This method returns FALSE for card types that don't support CVV.
    *
    * param: string cvv      value to verify
    * param: string cardType type/brand of card (case insensitive)
    *               "MasterCard", "Visa", "AMEX", "AmericanExpress",
    *               "American Express", "Discover", "Eurocard/MasterCard",
    *               "Eurocard"
    *
    * return bool   TRUE if format is correct, FALSE otherwise
    """
    if cardType.upper() in [
        "MASTERCARD",
        "EUROCARD",
        "EUROCARD/MASTERCARD",
        "VISA",
        "DISCOVER",
    ]:
        digits = 3

    if cardType.upper() in ["AMEX", "AMERICANEXPRESS", "AMERICAN EXPRESS"]:
        digits = 4

    if len(cvv) == digits and cvv.isdigit():
        return True

    return False
