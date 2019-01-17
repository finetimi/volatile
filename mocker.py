from unittest.mock import mock

m = mock.Mock()
assert isinstance(m.foo, mock.Mock)
assert isinstance(m.bar, mock.Mock)
assert isinstance(m(), mock.Mock)

assert m.foo is not m.bar is not m()