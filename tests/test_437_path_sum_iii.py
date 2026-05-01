import pytest

from tests.conftest import import_solution

mod = import_solution("437_PathSumIII")


def make_tree(values, TreeNode):
    """Level-order builder using the solution module's TreeNode."""
    from collections import deque

    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


@pytest.mark.parametrize(
    "values,target,expected",
    [
        ([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3),
        ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3),
        ([1], 1, 1),
        ([], 0, 0),
    ],
)
def test_path_sum(values, target, expected):
    root = make_tree(values, mod.TreeNode)
    assert mod.Solution().pathSum(root, target) == expected
