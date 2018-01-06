class Event:
    def __init__(self, t, ns, c, p):
        self.t = t
        self.namespace = ns
        self.command = c
        self.payload = p