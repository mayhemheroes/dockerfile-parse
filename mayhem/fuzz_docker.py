#!/usr/bin/env python3

import atheris
import io
import sys
import tempfile

with atheris.instrument_imports():
    from dockerfile_parse import DockerfileParser

@atheris.instrument_func
def TestOneInput(data):
        f = tempfile.NamedTemporaryFile()
        f.write(data)
        f.flush()
        DockerfileParser(f.name)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
