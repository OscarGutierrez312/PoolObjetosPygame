from tiposFiguras.triangulo import Triangulo


class ObjectPool:
    __instance = None
    __resources = list()

    def __init__(self):
        if ObjectPool.__instance is not None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def getInstance():
        if ObjectPool.__instance is None:
            ObjectPool.__instance = ObjectPool()

        return ObjectPool.__instance

    def getResource(self):
        if len(self.__resources) > 0:
            print("Using existing resource.")
            return self.__resources.pop(0)
        else:
            print("Creating new resource.")
            return Triangulo()

    def returnResource(self, resource):
        resource.reset()
        self.__resources.append(resource)
