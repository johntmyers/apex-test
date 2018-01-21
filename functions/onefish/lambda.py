"""Lambda Connector"""
import sys
sys.path.insert(0, "./lib")

import main


def handle(event, context):
    # parse some event stuff if need be
    main.run()
