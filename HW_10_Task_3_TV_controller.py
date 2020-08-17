CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController():

    def __init__(self, ch):
        self.CHANNELS = ch
        self.channel_number = 0

    def first_channel(self):
        # 1. представляет угрозу? 2. как использовать  В этом случае ошибка может произойти ТОЛЬКО если длинна массива нулевая. Просто отметь себе.
        return self.CHANNELS[0]

    def last_channel(self):
        return self.CHANNELS[-1]

    def turn_channel(self, channel_number):
#         хитрO конечно, ты же знаешь уже длинну но она динамическая потому нужно делать проверку.
        self.channel_number = channel_number
        if channel_number > len(self.CHANNELS) or channel_number <=0:
            print('Введен неверный номер канала')
        else:
            return self.CHANNELS[channel_number-1]

    def next_channel(self):
        # лучше с начала проверять а потом менять. Представь что будет если 10 раз вызвать next_channel? Чему станет равно self.channel_number ?
        if self.channel_number >= len(self.CHANNELS):
            self.channel_number = 0
        else:
            self.channel_number += 1

        return self.CHANNELS[self.channel_number]

    def previous_channel(self):
        # точно так же но зеркально с некст. 10 раз вызовем и текущий будет -10 а должно его зацикливать.
        self.channel_number -= 1
        if self.channel_number <= 1:
            return self.CHANNELS[2]
        if self.channel_number == 2:
            return self.CHANNELS[1]
        if self.channel_number == 3:
            return self.CHANNELS[2]

    def current_channel(self):
        '''не динамично. А если в массиве было бы 50 каналов ты же не писала бы 
        ....
        if self.channel_number == 49:
            return self.CHANNELS[48]
        if self.channel_number == 50:
            return self.CHANNELS[49]
        
        '''
        if self.channel_number == 1:
            return self.CHANNELS[0]
        if self.channel_number == 2:
            return self.CHANNELS[1]
        if self.channel_number == 3:
            return self.CHANNELS[2]

    def is_exist(self, num):
        try:
            if 1 <= num <= ((len(self.CHANNELS))):  # да, симпатичная проверка на вхождение в промежуток в синтаксисе есть.
                answer = 'Yes'
            else:
                answer = 'No'
        except:
            if num in self.CHANNELS:  # проверка и так возвращает тру. Нет смысла еще проверять что оно тру.
                answer = 'Yes'
            else:
                answer = 'No'

        return answer


# нам надо передавать каналы а не зашивать их намертво в пульте. Так более динамично получается.
controller = TVController(CHANNELS)

print(controller.first_channel())
print(controller.last_channel())
print(controller.turn_channel(1))
print(controller.next_channel())
print(controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist(3))





