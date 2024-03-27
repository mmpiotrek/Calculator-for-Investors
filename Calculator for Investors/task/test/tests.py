from hstest import CheckResult, StageTest, dynamic_test, TestedProgram

main_menu = """
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
"""

crud_menu = """
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
"""

top_ten_menu = """
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
"""

farewell_msg = "Have a nice day!"
ask_option_msg = "Enter an option:"
invalid_option_msg = "Invalid option!"
not_implemented_msg = "Not implemented!"

# index 0 entered value, index 1 expected value
test_data_1 = [
    {
        "test_values": [
            ("two", (invalid_option_msg + main_menu + ask_option_msg)),
            ("999", (invalid_option_msg + main_menu + ask_option_msg)),
            ("0", farewell_msg),
        ]
    },
    {
        "test_values": [
            ("1", (crud_menu + ask_option_msg)),
            ("1", (not_implemented_msg + main_menu + ask_option_msg)),
            ("1", (crud_menu + ask_option_msg)),
            ("3", (not_implemented_msg + main_menu + ask_option_msg)),
            ("0", farewell_msg),
        ]
    },
    {
        "test_values": [
            ("2", (top_ten_menu + ask_option_msg)),
            ("1", (not_implemented_msg + main_menu + ask_option_msg)),
            ("2", (top_ten_menu + ask_option_msg)),
            ("3", (not_implemented_msg + main_menu + ask_option_msg)),
            ("0", farewell_msg),
        ]
    }
]


class InvestorTest(StageTest):

    # testing entered vs expected
    @dynamic_test(data=test_data_1)
    def test1(self, dict_):
        t = TestedProgram()
        output = t.start().strip()
        text = main_menu.strip() + ask_option_msg.strip()
        if output.replace("\n", "") != text.replace("\n", ""):
            # print(repr(output))
            # print(repr(text))
            return CheckResult.wrong(
                f"Your program should output:\n{text}\ninstead of:\n{output}")
        for test_values in dict_.values():
            for item in test_values:
                output = t.execute(item[0]).strip()
                text = item[1]
                if output.replace("\n", "") != text.replace("\n", ""):
                    # print(repr(output))
                    # print(repr(text))
                    return CheckResult.wrong(
                        f"Your program should output:\n{text}\ninstead of:\n{output}")
        return CheckResult.correct()


if __name__ == '__main__':
    InvestorTest().run_tests()
