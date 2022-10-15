class Stack:
    """
    Базовый класс описывающий стек (добавление и удаление элемента)

    """
    def __init__(self):
        self.__st = []
    """
    Инициализация списка элементов
    """

    def __str__(self):
        """

        :return: вывод
        """
        return '; '.join(self.__st)

    def push(self, elem):
        """
        Добавление элемента
        """
        self.__st.append(elem)

    def pop(self):
        """
        :return: удаление и возвращение последнего элемента в списке
        """
        if len(self.__st) == 0:
            return None
        return self.__st.pop()

class TaskManager():
    """
    Базовый класс описывающий задачи и приоритет
    """
    def __init__(self):
        self.task = dict()
        """
        Инициализация словаря
        """
    def __str__(self):
        display = []
        if self.task:
            for prior in sorted(self.task.keys()):
                display.append('{prior} {task}\n'.format(
                    prior=str(prior),
                    task=self.task[prior]
                ))
        return ''.join(display)

    def new_task(self, task, priority):
        """
        :param task: Задача
        :param priority: приоритет
        """
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
