import sys

def null_gen(arg_list, call, case_name, catcher):
    """
    Generate tests for null checks in multiple arguments.

    arg_list - an ordered `list` of arguments to be called and nulled out one
    by one
    call - the `string` preceding the arg_list. Can be a Java function call or
    constructor call
    case_name - `String` what test case is this?
    catcher - `String` JUnit expection catcher
    """
    limit = len(arg_list)
    generated_test = []

    for i in range(limit):
        spam = arg_list[i]
        arg_list[i] = "null"
        generated_test.append("@Test")
        generated_test.append("public void test" + case_name + str(i) + "(){")
        generated_test.append("    " + catcher + ";")
        generated_test.append("    " + call + "(" + ','.join(arg_list) + ");")
        generated_test.append("}")
        generated_test.append("")
        arg_list[i] = spam

    return "\n".join(generated_test)

if __name__ == "__main__":
    print("Just a collection of functions for generating standard but boring test cases.")
