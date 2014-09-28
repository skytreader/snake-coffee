#! /usr/bin/env python3

import json
import sys

from builder import JavaWriter

EXCEPTION_CONSTRUCTOR_SIGS = (("",),
  ("String message",), 
  ("String message", "Throwable cause"),
  ("String message", "Throwable cause", "boolean enableSuppression",
    "boolean writableStackTrace"),
  ("Throwable cause",))

def make_exception(filename):
    """
    Creates an Exception class. The json file is expected to have as follows:

    {
        "package":"net.skytreader.kode",
        "class":"TheOnlyException"
    }

    That's all.
    """
    jsonf = json.load(open(filename))
    jwriter = JavaWriter()

    jwriter.add_line("package " + jsonf["package"] + ";")
    jwriter.add_line("")
    jwriter.add_line("public class " + jsonf["class"] + " extends Exception{")

    for sig in EXCEPTION_CONSTRUCTOR_SIGS:
        param_list = ", ".join(sig)
        args = []
        for param in sig:
            # FIXME What about multiple spaces???!!?!?!?!?!?
            argsplit = param.split(" ")
            if len(argsplit) == 2:
                args.append(argsplit[1])
        
        args_list = ", ".join(args)

        jwriter.add_line("public " + jsonf["class"] + "(" + param_list + "){")
        jwriter.add_line("super(" + args_list + ");")
        jwriter.add_line("}")

    jwriter.add_line("}")

    return str(jwriter)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 " + sys.argv[0] + " <json-object-desc>")
        sys.exit(1)

    print(make_exception(sys.argv[1]))
