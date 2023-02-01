#!/usr/bin/env python3

import atheris
import sys
import fuzz_helpers

with atheris.instrument_imports(enable_loader_override=False):
    import dockerfile_parse

def TestOneInput(data):
        fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
        with fdp.ConsumeMemoryStringFile(all_data=True) as f:
            dfile = dockerfile_parse.DockerfileParser(fileobj=f)
            for struct in dfile.structure:
                pass

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    atheris.instrument_all()
    main()
