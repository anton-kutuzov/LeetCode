from tests.conftest import import_solution

mod = import_solution("1_TwoSum")


def test_examples():
    sol = mod.Solution()
    # TODO: write parametrized cases — pick your own edge cases first,
    #       then add a couple from the original problem.
    assert sol
