'''
To Start, assume every character in the input string is unique

Breakdown:
    Break the problem into subproblems:
        getting all permutations for all charters except for the last one
    We need to have a base case:
        for string that only has 1 character, the permutation is itself
'''
def get_permutation(string):
    # Base Case
    if len(string) <= 1:
        return set([string])
    
    all_chars_except_for_last = string[:-1]
    last_char = string[-1]

    # Recursive call: get all possible permutations for all chars except for last
    permutations_of_all_chars_except_for_last = get_permutation(all_chars_except_for_last)

    # Put the lat char in all possible positions for each of
    # the above permutation
    permutations = set()
    for permutation_of_all_chars_except_for_last in permutations_of_all_chars_except_for_last:
        for position in range(len(all_chars_except_for_last) + 1):
            permutation = (
                permutation_of_all_chars_except_for_last[:position]
                + last_char
                + permutation_of_all_chars_except_for_last[position:]
            )
        permutations.add(permutation)

    return permutations

'''
Summary
    Playing with a sample input is huge. Two part process:
        first figure out how you would solve the problem by hand, as though
        the input was a stack of paper on a desk in front of you
        Then, translate that process into code.

'''