#!/usr/bin/env python
"""
Author: Seunghyun Hwang aka Toezilla <innuendobeat@gmail.com>
Date: 2022-06-05
Purpose: Say Hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument('-n', '--name', metavar='name', default='World',
                        help='Input Name to greet!')
    return(parser.parse_args())


def main():
    """chief in size or importance"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == "__main__":
    main()
