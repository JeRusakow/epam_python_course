from homework6.task1.counter import instances_counter


def test_instance_counting():
    @instances_counter
    class A:
        pass

    _, _, _ = A(), A(), A()
    assert A.get_created_instances() == 3


def test_reset_returns_counter_before_resetting():
    @instances_counter
    class A:
        pass

    _, _, _ = A(), A(), A()
    assert A.reset_instances_counter() == 3


def test_reset_counter():
    @instances_counter
    class A:
        pass

    _, _, _ = A(), A(), A()
    A.reset_instances_counter()
    assert A.get_created_instances() == 0
