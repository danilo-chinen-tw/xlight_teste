#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import tftpy


server = tftpy.TftpServer('tftpboot')
server.listen('0.0.0.0', 69)
