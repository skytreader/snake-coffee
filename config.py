#! /usr/bin/env python3

import json
import sys

from builder import JavaWriter

IO_CONFIG_IMPORTS = ("FileWriter", "IOException", "PrintWriter", "Reader")
OTHER_CONFIG_IMPORTS = ("java.util.Properties")

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
    jwriter.add_line("config_file = new Properties();")
    jwriter.add_line("config_file.load(r);")
    jwriter.add_line("}")

    return str(jwriter)
