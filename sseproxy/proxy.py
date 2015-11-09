class ProxyInterface(object):
    """
    Interface for Proxy.
    """

    def get_floor(self, floor):
        raise NotImplementedError("Not implemented yet.")

    def get_room(self, room):
        raise NotImplementedError("Not implemented yet.")

    def get_workspace(self, workspace):
        raise NotImplementedError("Not implemented yet.")

    def get_employee(self, employee):
        raise NotImplementedError("Not implemented yet.")
