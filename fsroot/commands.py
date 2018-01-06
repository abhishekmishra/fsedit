class StartCommand:
    def handle(self, e):
        print('Start command executed')


class StopCommand:
    def handle(self, e):
        print('Stop command executed')


class KillCommand:
    def handle(self, e):
        print('Kill command executed')


default_command_config = {
    'start': StartCommand(),
    'stop': StopCommand(),
    'kill': KillCommand()
}
