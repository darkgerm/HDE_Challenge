#!/usr/bin/env python3
import ctypes
lib = ctypes.cdll.LoadLibrary('./libchallenge.so')
lib.run()
