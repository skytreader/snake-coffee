#! /usr/bin/env python3

import json
import re
import sys

from builder import JavaWriter

IO_CONFIG_IMPORTS = ("FileWriter", "IOException", "PrintWriter", "Reader")
OTHER_CONFIG_IMPORTS = ("java.util.Properties",)

def __upper_names(cfg_field):
    words = re.split("[\-_]", cfg_field)
    return "".join((w[0].upper() + w[1:len(w)] for w in words))

def generate_config(cfg_path):
    cfg = json.load(open(cfg_path))
    jwriter = JavaWriter()
    jwriter.add_line("package " + cfg["package"])
    jwriter.add_line("")

    for java_lib in IO_CONFIG_IMPORTS:
        jwriter.add_line("import java.io." + java_lib)
    jwriter.add_line("")

    for java_lib in OTHER_CONFIG_IMPORTS:
        jwriter.add_line("import " + java_lib)
    jwriter.add_line("")

    jwriter.add_line("public class ConfigReader{")
    jwriter.add_line("")
    jwriter.add_line("private Properties configFile;")
    jwriter.add_line("")
    jwriter.add_line("public ConfigReader(Reader r) throws IOException{")
    jwriter.add_line("configFile = new Properties();")
    jwriter.add_line("configFile.load(r);")
    jwriter.add_line("}")
    jwriter.add_line("")

    for config_field in cfg["config-fields"]:
        jwriter.add_line("public " + config_field["return-type"] + " " + __upper_names(config_field["field-name"]) + "{")
        jwriter.add_line("return configFile.getProperty(\""  + config_field["field-name"] + "\");")
        jwriter.add_line("}")
        jwriter.add_line("")

    jwriter.add_line("}")

    return str(jwriter)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 " + sys.argv[0] + " <cfg.json>")
        exit(1)
    
    print(generate_config(sys.argv[1]))
