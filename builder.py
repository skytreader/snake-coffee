#! /usr/bin/env python3
import json
import sys

class JavaSyntaxError(Exception):
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Syntax error on: " + self.value

class JavaWriter(object):
    """
    Write you those Java strings. Features "syntax check" as
      - brace matching
      - auto indent
    """
    OPEN_GROUPERS = ("(", "{", "[")
    CLOSE_GROUPERS = (")", "}", "]")
    INDENT_SIZE = 4

    def __init__(self):
        self.grouper_stack = []
        self.code_base = []
        self.current_indent_count = 0
    
    def add_line(self, line):
        code_line = line.strip()

        if code_line == "":
            self.code_base.append(code_line)
        else:
            # Check them parens and braces
            for token in code_line:
                if token in JavaWriter.OPEN_GROUPERS:
                    self.grouper_stack.insert(0, token)
                elif token in JavaWriter.CLOSE_GROUPERS:
                    try:
                        match = self.grouper_stack.pop()
                    except IndexError:
                        raise JavaSyntaxError(code_line)

            indent = " " * self.current_indent_count
            self.code_base.append(indent + code_line)

            if code_line[len(code_line) - 1] in JavaWriter.OPEN_GROUPERS:
                self.current_indent_count += 4
            elif code_line[len(code_line) - 1] in JavaWriter.CLOSE_GROUPERS:
                self.current_indent_count -= 4

    def __str__(self):
        return "\n".join(self.code_base)

def json_to_java(filename):
    json_desc = json.load(open(filename))
    jwriter = JavaWriter()

    jwriter.add_line("package " + json_desc["package"] + ";")
    jwriter.add_line("")
    jwriter.add_line("public class " + json_desc["class_name"] + "{")

    required_fields = []
    optional_fields = []

    # List out the fields 
    for field in json_desc["fields"].keys():
        field_type = json_desc["fields"][field]["type"]
        jwriter.add_line("private final " + field_type + " " + field + ";")

        if json_desc["fields"][field].get("required"):
            required_fields.insert(0, field)
        else:
            optional_fields.insert(0, field)

    # Start the Builder class
    jwriter.add_line("")
    jwriter.add_line("public static class Builder{")

    for req_field in required_fields:
        field_type = json_desc["fields"][req_field]["type"]
        jwriter.add_line("private final " + field_type + " " + req_field + ";")

    jwriter.add_line("")

    for opt_field in optional_fields:
        field_type = json_desc["fields"][opt_field]["type"]
        default = str(json_desc["fields"][opt_field]["default"])
        jwriter.add_line("private " + field_type + " " + opt_field + " = " + default + ";")

    return str(jwriter)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 " + sys.argv[0] + " <json-object-desc>")
        sys.exit(1)

    print(json_to_java(sys.argv[1]))
