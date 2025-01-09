# Task 1
#
# A Person class
#
# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes.
# Make another method called talk() which makes prints a greeting from the person containing, for example like this:
#     "Hello, my name is Carl Johnson and I’m 26 years old".

print(
    '''
Task 1
A Person class
    '''
)


class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f'"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old".'


person_1 = Person('Carl', 'Johnson', 26)
person_2 = Person('Alexa', 'Zadik', 32)

print(
    person_1.talk()
)
print(
    person_2.talk()
)

# Task 2
#
# Doggy age
#
# Create a class Dog with class attribute 'age_factor' equals to 7.
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.
print(
    '''
Task 2
Doggy age
    '''
)


class Dog:

    def __init__(self, age_factor=7):
        self.age_factor = age_factor

    def human_age(self, age):
        human_age = self.age_factor * age
        return f'Yours dog is {age}y.o. that equivalent to {human_age}y.o. human age'


dog = Dog()
print(
    dog.human_age(5)
)

# Task 3
#
# TV controller
#
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
#
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

# The default channel turned on before all commands is №1.
#
# Your task is to create the TVController class and methods described above.
print(
    '''
Task 3
TV controller
    '''
)

CHANNELS = ["BBC", "Discovery", "TV1000"]

print(
    '______Channel List______\n'
)
for i in CHANNELS:
    print(
        f'Channel {CHANNELS.index(i) + 1}: {i}'
    )
print(
    '________________________\n'
)


class TVController:
    channel_index = 0

    def __init__(self, channels):
        self.channels = channels
        self.channel_index = 0
        # print(self.channel_index)

    def first_channel(self):
        self.channel_index = 0
        self.channel_index = 0
        #         print(self.channel_index)
        return f'First channel is: {self.channels[self.channel_index]}'

    def last_channel(self):
        self.channel_index = -1
        #         print(self.channel_index)
        return f'Last channel is: {self.channels[self.channel_index]}'

    def turn_channel(self, index=1):
        self.channel_index = 0 if index == 1 else index - 1
        return f'You are turned back to channel: {self.channels[self.channel_index]}'

    def next_channel(self):
        self.channel_index += 1
        return f'You are jumped to channel r: {self.channels[self.channel_index]}'

    def previous_channel(self):
        self.channel_index -= 1
        return f'Return to previous channel: {self.channels[self.channel_index]}'

    def current_channel(self):
        return f'Current channel is: {self.channels[self.channel_index]}'

    def exists(self, channel):
        # try:
        if isinstance(channel, int):
            return \
                f'Yes, {self.channels[channel]} channel in the channel list' \
                    if channel <= (len(self.channels) - 1) else \
                    f'No, current channel is not in the list'
        elif isinstance(channel, str):
            return \
                f'Yes, {channel} channel in the channel list' \
                    if channel in self.channels else \
                    f'No {channel} channel not in the list'
    # except Exception:
    #     return 'Some Error'


controller = TVController(CHANNELS)

print(controller.first_channel())  # BBC

print(controller.last_channel())  # TV1000

print(controller.turn_channel(1))  # BBC

print(controller.next_channel())  # Discovery

print(controller.previous_channel())  # "BBC"

print(controller.current_channel())  # "BBC"

print(controller.exists(0))  # "No"
print(controller.exists(1))  # "No"
print(controller.exists(2))  # "No"
print(controller.exists(3))  # "No"

print(controller.exists("BBC"))  # "Yes"
