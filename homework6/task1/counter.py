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
    Adds two methods:
    get_created_instances # returns the amount of created class instances
    reset_instance_counter # resets the instance counter and returns the amount before resetting
    """

    original_init = getattr(cls, "__init__")

    setattr(cls, "instance_counter", 0)

    def modified_init(self, *args, **kwargs):
        cls.instance_counter += 1
        return original_init(self, *args, **kwargs)

    def get_created_instances(self=None):
        return cls.instance_counter

    def reset_instances_counter(self=None):
        res = cls.instance_counter
        cls.instance_counter = 0
        return res

    setattr(cls, "__init__", modified_init)
    setattr(cls, "get_created_instances", get_created_instances)
    setattr(cls, "reset_instances_counter", reset_instances_counter)

    return cls


@instances_counter
class User:
    pass


if __name__ == "__main__":

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
