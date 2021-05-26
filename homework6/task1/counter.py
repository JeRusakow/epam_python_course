"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """
    Adds private _instance_counter property to a class along with two methods:

    get_created_instances - returns the amount of created class instances
    reset_instance_counter - resets the instance counter and returns the
        amount before resetting
    """

    original_init = cls.__init__

    cls.__instance_counter = 0

    def modified_init(self, *args, **kwargs):
        """Modified __init__ method. Takes the same arguments as original one"""
        cls.__instance_counter += 1
        return original_init(self, *args, **kwargs)

    @classmethod
    def get_created_instances(cls_) -> int:
        """Returns the amount of created class instances"""
        return cls_.__instance_counter

    @classmethod
    def reset_instances_counter(cls_) -> int:
        """Forcibly sets the amount of created class instances to zero"""
        res = cls_.__instance_counter
        cls_.__instance_counter = 0
        return res  # noqa

    cls.__init__ = modified_init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    print(User.get_created_instances())  # noqa # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # noqa # 3
    print(user.reset_instances_counter())  # noqa # 3
