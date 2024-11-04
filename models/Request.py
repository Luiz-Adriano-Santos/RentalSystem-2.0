class Request:
    def __init__(self, status, sport, timestamp, user, boots, helmet, ski_board):
        self.status = status
        self.sport = sport
        self.timestamp = timestamp
        self.user = user
        self.boots = boots
        self.din = self.calculate_din()
        self.employee = ''
        self.helmet = helmet
        self.ski_board = ski_board
    
    def calculate_din(self):
        if self.ski_board == 'Not Requested' or self.ski_board.type == 'Snowboard':
            return ''
        else:
            #implementar lógica de calculo do DIN
            return ''