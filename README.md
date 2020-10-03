
[![Build Status](https://travis-ci.com/TralahM/pycctek.svg?branch=master)](https://travis-ci.com/TralahM/pycctek)
[![Build status](https://ci.appveyor.com/api/projects/status/yvvmq5hyf7hj743a/branch/master?svg=true)](https://ci.appveyor.com/project/TralahM/pycctek/branch/master)
[![Documentation Status](https://readthedocs.org/projects/pycctek/badge/?version=latest)](https://pycctek.readthedocs.io/en/latest/?badge=latest)
[![License: GPLv3](https://img.shields.io/badge/License-GPLV2-green.svg)](https://opensource.org/licenses/GPLV2)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![Views](http://hits.dwyl.io/TralahM/pycctek.svg)](http://dwyl.io/TralahM/pycctek)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pycctek/pull/)
[![GitHub pull-requests](https://img.shields.io/badge/Issues-pr-red.svg?style=flat-square)](https://github.com/TralahM/pycctek/pull/)
[![Language](https://img.shields.io/badge/Language-Python-3572A5.svg)](https://github.com/TralahM)
<img title="Watching" src="https://img.shields.io/github/watchers/TralahM/pycctek?label=Watchers&color=blue&style=flat-square">
<img title="Stars" src="https://img.shields.io/github/stars/TralahM/pycctek?color=red&style=flat-square">
<img title="Forks" src="https://img.shields.io/github/forks/TralahM/pycctek?color=green&style=flat-square">

# pycctek.
Issuer Identification Number Database and Verification Utility Library. Luhn Algorithm, BIN Checker, Random Credit Card Generators.

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)

# Documentation

[![Documentation](https://img.shields.io/badge/Docs-pycctek-blue.svg?style=for-the-badge)](https://github.com/TralahM/pycctek)

## Issuer Identification Numbers

ISO/IEC 7812 Identification cards — Identification of issuers was first published by the International Organization for Standardization (ISO) in 1989.
It is the international standard specifies "a numbering system for the identification of the card issuers,
the format of the issuer identification number (IIN) and the primary account number (PAN).


The registration authority for Issuer Identification Numbers (IINs) is the American Bankers Association.

An IIN is currently six digits in length.
The leading digit is the major industry identifier (MII), followed by 5 digits, which together make up the IIN.
This IIN is paired with an individual account identification number, and a single digit checksum.
MII 9 has been assigned to national standards bodies for national use.

The first digit is a 9 followed by a three-digit numeric country code numeric-3 country code from ISO 3166-1.
National Numbering Systems are managed by ISO-member national standards bodies.
The US National Numbering system is managed by the American National Standards Institute.

| MII  | Digit Value Issuer Category                                             |
| ---- | --------------------------------                                        |
| 0    | ISO/TC 68 Assignment                                                    |
| 1    | Airline cards                                                           |
| 2    | Airlines cards (and other future industry assignments)                  |
| 3    | Travel and Entertainment Cards                                          |
| 4    | Banking and Financial Cards                                             |
| 5    | Banking and Financial Cards                                             |
| 6    | Merchandising and Financial Cards                                       |
| 7    | Gas Cards- Other Future Industry Assignments                            |
| 8    | Healthcare Cards- Telecommunications- Other Future Industry Assignments |
| 9    | For Use by National Standards Bodies                                    |

The first six digits, including the major industry identifier, compose the issuer identifier number (IIN) which identifies the issuing organization.
The IIN is sometimes referred to as a "bank identification number" (BIN).
The IIN's use is much broader than identification of a bank.
IINs are used by companies other than banks.


## Luhn Algorithm
The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod 10" algorithm, named after its creator, IBM scientist Hans Peter Luhn,
is a simple checksum formula used to validate a variety of identification numbers,
such as:
- credit card numbers,
- IMEI numbers,
- National Provider Identifier numbers in the United States,
- Canadian Social Insurance Numbers,
- Israeli ID Numbers,
- South African ID Numbers,
- Greek Social Security Numbers (ΑΜΚΑ),
- and survey codes appearing on McDonald's, Taco Bell, and Tractor Supply Co. receipts.

It is described in U.S. Patent No. 2,950,048, filed on January 6, 1954, and granted on August 23, 1960.

[Read The Wikipedia Page for a more comprehensive description of Luhn's
Algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)

# How to Install
```bash
# In terminal do:
$ pip install pycctek
```

## Building from Source for Developers

```console
$ git clone https://github.com/TralahM/pycctek.git
$ cd pycctek
$ python setup.py install
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)


# Support

# LICENCE

[Read the license here](LICENSE)


# Self-Promotion

[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-red?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-red.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://org.tralahtek.com)


