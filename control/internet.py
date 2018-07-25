#!/usr/bin/python2
#
# Copyright 2016 Kirk A Jackson DBA bristoSOFT all rights reserved.  All methods,
# techniques, algorithms are confidential trade secrets under Ohio and U.S.
# Federal law owned by bristoSOFT.
#
# Kirk A Jackson dba bristoSOFT
# 4100 Executive Park Drive
# Suite 11
# Cincinnati, OH  45241
# Phone (513) 401-9114
# email jacksonkirka@bristosoft.com
#
# The trade name bristoSOFT is a registered trade name with the State of Ohio
# document No. 201607803210.
#
'''
This internet.py module provides testing of the existence, reliability and 
performance of an internet connection.
'''

import urllib2
import socket

class InternetConnection:
    '''
    InternetConnection is a class of resources used to
    verify that an internet connection has been established.
    '''
    @staticmethod
    def inet_request(_url):
        '''
        inet_request accepts a url and returns true or false booleans.
        
        
        >>> iconnect = InternetConnection()
        >>> _address = 'google.com'
        >>> conn = iconnect.inet_request(_address)
        >>> conn
        True
        >>> _address = 'googlee.com'
        >>> conn = iconnect.inet_request(_address)
        >>> conn
        False
        '''
        try:
            urllib2.urlopen(_url,timeout=30)
            return True
        except urllib2.URLError:
            return False
    
    @staticmethod
    def inet_socket_request(hostname):
        '''
        inet_socket_reuqest accepts a url and returns true or false booleans.
        
        gaierror(get address info), herror(host), timeout inheret from error.
        '''
        try:
            host = socket.gethostbyname(hostname) # resolve hostname
            socket.create_connection((host, 80), 2) # connect
            return True
        except socket.error:
            return False

class InternetReliability:
    pass
    
class InternetPerformance:
    '''
    Internet "speed" actually consists of multiple factors, including bandwidth,
    latency, and packet loss. What exactly are you trying to measure? If it's
    bandwidth (data transfer speed in bits per second), then you should also
    measure transfers of larger payloads, because the time to complete small
    transfers will tend to be dominated by latency effects. If it's latency
    (milliseconds for a round trip) that you are want to measure, then a tiny
    packet (typically an ICMP echo request, commonly called a "ping") would be
    more appropriate.

    In addition, there are confounding issues:

    Upload vs. download speed:
        Residential Internet connections tend to significantly favour downloads,
        since that's what most consumers care about.
    Traffic shaping:
        Some ISPs will throttle the bandwidth to penalize very large transfers,
        so that smaller responses feel more responsive.
    Server performance:
        It does take a few milliseconds for Google's server to formulate the
        response payload; that delay would be a more significant fraction of the
        measured round-trip time for a short response than for a long response.
    HTTP and HTTPS overhead:
        You're considering only the size of the HTTP response payload. Since you're
        using HTTPS, there are also multiple TCP round trips needed to perform the TLS
        handshake, and a few kilobytes to transfer the certificates. The HTTP
        headers could add another kilobyte or so. All of this is significant
        when the payload is only ~10 kB short.
    DNS overhead:
        Resolving the google.com hostname to an IP address might involve a DNS 
        lookup, which would add a few milliseconds. The time for that DNS lookup
        is accounted for in your benchmark, but not the traffic.
    Proximity:
        The "Internet" is not one entity. Connectivity to various parts of the
        Internet will have different performance characteristics.

    '''
    pass

