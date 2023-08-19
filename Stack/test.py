from stack import LinkedListStack

def test_problem_stack(string):
    pair = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = LinkedListStack()
    for s in string:
        if s in '({[':
            stack.push(pair[s])
        else:
            if stack.pop() != s:
                return False
    return stack.is_empty()

assert test_problem_stack("()")
assert test_problem_stack("()[]{}")
assert test_problem_stack("({[][]})")
assert test_problem_stack("({[]})")
assert not test_problem_stack("(]")
assert not test_problem_stack("(()]")
assert not test_problem_stack("(((])")
assert not test_problem_stack("((())")