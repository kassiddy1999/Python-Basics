# def ninjaIntro(dictionary):
#     for key,val in dictionary.items():
# #         print(f" i am {key} and i am a {val} belt")
# def beltCount(dictionary):
#     belts = list(dictionary.values())
#     for belt in set(belts):
#         num = belts.count(belt)
#         print(f'there are {num} {belt} belts')
# ninjaBelts = {}
# while True:
#     ninjaName = input('enter a ninja name:')
#     ninjaBelt = input('enter a ninja belt color:')
#     ninjaBelts[ninjaName]=ninjaBelt
#     another = input('add another?(y/n)')
#     if another == 'y':
#         continue
#     else:
#         break
def ninjaIntro(dictionary):
    for key,val in dictionary.items():
        print(f' i am {key} and i ama  {val} belt')
def beltCount(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'there are {num} {belt} belts')


ninjaBelts = {}
while True:
    ninjaName = input('please enter your name:')
    ninjaBelt = input('please enter your belt:')
    ninjaBelts[ninjaName] = ninjaBelt
    another = input('add another? y/n')
    if another == 'y':
        continue
    else:
        break
