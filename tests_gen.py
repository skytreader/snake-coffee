import sys
import unittest

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

class FunctionsTest(unittest.TestCase):
    
    def test_null_gen(self):
        plain_string_test = null_gen(['"something1"', '"something2"'],
          "MyObject mo = new MyObject", "MyObjectNull",
          "expection.expect(NullPointerException.class)")

        expected_plain_string_test = """@Test
public void testMyObjectNull0(){
    expection.expect(NullPointerException.class);
    MyObject mo = new MyObject(null,"something2");
}

@Test
public void testMyObjectNull1(){
    expection.expect(NullPointerException.class);
    MyObject mo = new MyObject("something1",null);
}
        """
        
        self.assertEqual(plain_string_test, expected_plain_string_test)

if __name__ == "__main__":
    unittest.main()
