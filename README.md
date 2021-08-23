# pytest_defer - A "defer" fixture for pytest


```python
def test_example(defer):
    # All functions appended to defer will execute at test end in reverse order
    instance1 = spin_instance()
    defer.append(lambda: delete_instance(instance1))  # called second
    instance2 = spin_instance()
    defer.append(lambda: delete_instance(instance2))  # called first

    # Test code using instance1 & instance2
    ...
```
