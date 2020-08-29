
class TVController():
    def test(self):
        pass
    
    def __init__(self):
        self.CHANNELS = ["BBC", "Discovery", "TV1000"]
        self.channel_number = 0

    def first_channel(self):
        return self.CHANNELS[0]

    def last_channel(self):
        return self.CHANNELS[-1]

    def turn_channel(self, channel_number):
        self.channel_number = channel_number
        try:
            if channel_number == 1:
                return self.CHANNELS[0]
            if channel_number == 2:
                return self.CHANNELS[1]
            if channel_number == 3:
                return self.CHANNELS[2]
        except:
            print('Введен неверный номер канала')

    def next_channel(self):
        self.channel_number += 1
        if self.channel_number >= len(self.CHANNELS):
            return self.CHANNELS[0]
        if self.channel_number == 2:
            return self.CHANNELS[1]

    def previous_channel(self):
        self.channel_number -= 1
        if self.channel_number <= 1:
            return self.CHANNELS[2]
        if self.channel_number == 2:
            return self.CHANNELS[1]
        if self.channel_number == 3:
            return self.CHANNELS[2]

    def current_channel(self):
        if self.channel_number == 1:
            return self.CHANNELS[0]
        if self.channel_number == 2:
            return self.CHANNELS[1]
        if self.channel_number == 3:
            return self.CHANNELS[2]

    def is_exist(self, num):
        try:
            if 1 <= num <= ((len(self.CHANNELS))):
                answer = 'Yes'
            else:
                answer = 'No'
        except:
            if (num in self.CHANNELS) == True:
                answer = 'Yes'
            else:
                answer = 'No'

        return answer



controller = TVController()

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(3))





