#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Oct 24, 2015 '
__author__= 'samuel'

import pynats

def main():
    c = pynats.Connection(url='nats://gnatsd:4222', verbose=True)
    c.connect()
    c.publish('foo', 'Hello World!')
    c.close()


if __name__ == '__main__':
    main()
