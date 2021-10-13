import papexp.core
import sys

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        papexp.core.check_and_run()
    else:
        if args[1] == "-c":
            papexp.core.export_recipes()
        else:
            print("Use no arguments or -c to run without status check")
