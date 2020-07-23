class Value_Error:

    @staticmethod
    def raise_error(keyword, amount):
        raise ValueError('Invalid value for {}, got {}'.format(keyword, amount))


class Item(Value_Error):
    def __init__(self, name, price, category):
        if price <= 0:
            self.raise_error('price', price)
        self._name = name
        self._price = price
        self._category = category

    def __str__(self):
        return '{}@{}-{}'.format(self._name, self._price, self._category)


class Query(Value_Error):
    operation_list = [
        'IN', 'EQ', 'GT', 'GTE', 'LT',
        'LTE', 'STARTS_WITH', 'ENDS_WITH', 'CONTAINS']

    def __init__(self, field, operation, value):
        if operation not in Query.operation_list:
            self.raise_error('operation', operation)
        self._value = value
        self._field = field
        self._operation = operation
    def __str__(self):
        return '{} {} {}'.format(self._field, self._operation, self._value)


class Store:
    def __init__(self, instance_list=[]):
        self._list_of_items = instance_list
        self._count_of_items = 0

    def __str__(self):
        if self._list_of_items:
            string_form = [str(i) for i in self._list_of_items]
            string_form = '\n'.join(string_form)
        else:
            string_form = 'No items'
        return string_form

    def add_item(self, items):
        self._list_of_items.append(items)
        self._count_of_items = len(self._list_of_items)

    def count(self):
        return self._count_of_items

    def lt_lte_gt_gte_operations(self, query):
        temporary_list = []
        if query._operation == 'GT':
            if query._field == 'price':
                for items in self._list_of_items:
                    if items._price > query._value:
                        temporary_list.append(items)

        elif query._operation == 'GTE':
            if query._field == 'price':
                for items in self._list_of_items:
                    if items._price >= query._value:
                        temporary_list.append(items)

        elif query._operation == 'LT':
            if query._field == 'price':
                for items in self._list_of_items:
                    if items._price < query._value:
                        temporary_list.append(items)

        elif query._operation == 'LTE':
            if query._field == 'price':
                for items in self._list_of_items:
                    if items._price <= query._value:
                        temporary_list.append(items)

        return Store(temporary_list)

    def equal_to_operations(self, query):
        temporary_list = []
        if query._operation == 'EQ':
            if query._field == 'name':
                for items in self._list_of_items:
                    if query._value == items._name:
                        temporary_list.append(items)
            elif query._field == 'price':
                for items in self._list_of_items:
                    if query._value == items._price:
                        temporary_list.append(items)
            elif query._field == 'category':
                for category in query._value:
                    for items in self._list_of_items:
                        if category == items._category:
                            temporary_list.append(items)
        return Store(temporary_list)

    def in_operation(self, query):
        temporary_list = []
        if query._field == 'category':
            for category in query._value:
                for items in self._list_of_items:
                    if category == items._category:
                        temporary_list.append(items)
        elif query._field == 'price':
            for value in query._value:
                for items in self._list_of_items:
                    if value == items._price:
                        temporary_list.append(items)
        elif query._field == 'name':
            for name in query._value:
                for items in self._list_of_items:
                    if name == items._name:
                        temporary_list.append(items)
        return Store(temporary_list)

    def starts_with_operation(self, query):
        temporary_list = []
        if query._field == 'name':
            for items in self._list_of_items:
                if  items._name.startswith(query._value):
                    temporary_list.append(items)
        elif query._field == 'category':
            for items in self._list_of_items:
                if  items._category.startswith(query._value):
                    temporary_list.append(items)
        elif query._field == 'price':
            for items in self._list_of_items:
                if  items._name.startswith(query._value):
                    temporary_list.append(items)

        return Store(temporary_list)

    def ends_with_opreation(self, query):
        temporary_list = []
        if query._field == 'name':
            for items in self._list_of_items:
                if  items._name.endswith(query._value):
                    temporary_list.append(items)
        elif query._field == 'category':
            for items in self._list_of_items:
                if  items._category.endswith(query._value):
                    temporary_list.append(items)
        elif query._field == 'price':
            for items in self._list_of_items:
                if  items._name.endswith(query._value):
                    temporary_list.append(items)

        return Store(temporary_list)

    def contains_operation(self, query):
        temporary_list = []
        if query._field == 'name':
            for items in self._list_of_items:
                if query._value in items._name:
                    temporary_list.append(items)
        elif query._field == 'category':
            for items in self._list_of_items:
                if  query._value in items._category:
                    temporary_list.append(items)
        elif query._field == 'price':
             for items in self._list_of_items:
               if query._value in items._name:
                    temporary_list.append(items)

        return Store(temporary_list)

    def filter(self, query):
        if query._operation == 'EQ':
            self.equal_to_operations(query)
        elif query._operation == 'IN':
            self.in_operation(query)
        elif query._operation == 'STARTS_WITH':
            self.starts_with_operation(query)
        elif query._operation == 'ENDS_WITH':
            self.ends_with_opreation(query)
        elif query._operation == 'CONTAINS':
            self.contains_operation(query)
        elif query._operation in ['GTE', 'GT', 'LT', 'LTE']:
            self.lt_lte_gt_gte_operations(query)

    def exclude(self, query):
        filtered_list = self.filter(query)
        temporary_list = []
        for items in self._list_of_items:
            if items not in filtered_list._list_of_items:
                temporary_list.append(items)
        return Store(temporary_list)
    
