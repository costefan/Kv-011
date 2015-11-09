from sseproxy.type import ProxyType
from sseproxy.dummy import ProxyDummy
from sseproxy.sse import ProxySSE


class ProxyFactory(object):
    """
    Factory for Proxy implementation.
    """

    @staticmethod
    def get_proxy(proxy):
        if proxy == ProxyType.SSE:
            return ProxySSE()
        elif proxy == ProxyType.DUMMY:
            return ProxyDummy()
        else:
            raise IOError("Wrong proxy type.")


if __name__ == '__main__':
    ProxyFactory().get_proxy(ProxyType.SSE)
