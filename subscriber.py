#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Oct 24, 2015 '
__author__= 'samuel'

import pynats

def callback(msg):
    print 'Received a message: %s' % msg.data

def main():
    c = pynats.Connection(url='nats://gnatsd:4222', verbose=True)
    c.connect()
    sub = c.subscribe('foo', callback)
    print 'waiting for 1 msg'
    c.wait(count=1)
    print 'received 1 msg'
    c.unsubscribe(sub)
    c.close()


if __name__ == '__main__':
    main()
