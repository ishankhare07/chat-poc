class ModifiedDict(dict):
    def __init__(self):
        self.__dict = {}

    def __setitem__(self, key, value):
        if self.__dict.get(key):
            # key exists
            self.__dict[key].append(value)
        else:
            # key doesn't exists
            self.__dict[key] = [value]

    def __getitem__(self, key):
        return self.__dict.get(key)

    def pop(self, key, value):
        return self.__dict[key]

    def get(self, key, default=None):
        result = self.__dict.get(key)
        return result if result else default

    def __repr__(self):
        return dict.__repr__(self.__dict)


class GlobalStore:
    __connected = ModifiedDict()
    __verified = ModifiedDict()

    @property
    def connected(self):
        return GlobalStore.__connected

    @property
    def verified(self):
        return GlobalStore.__verified

    def move_to_verified(self, key, value):
        """
            move the websocket object from connected
            to verified
        """
        self.remove_connected(key, value)
        GlobalStore.__verified[key] = value

    def remove_connected(self, key, value):
        GlobalStore.__connected[key].remove(value)
