import sys
import os

from antlr4 import *

# Make sure that ANTLR_JAR is set to antlr-4.8-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
print(ANTLR_JAR)
