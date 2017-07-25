# writ a thing to use dict

import pickle
from twilio.rest import TwilioRestClient

# old fincs
# def pickel_this_shit(to_pic: dict, path: str):
#     """ old pickler """
#
#     phone_pickle = path + 'phone_1'
#     with open(phone_pickle, 'wb') as pkf:
#         pickler = pickle.Pickler(pkf)
#         print(to_pic)
#         user_input = input('would you like to save this ')
#         if user_input == 'y':
#             pickler.dump(to_pic)
# def open_pic():
#     with open('/home/chris/proj/pickeldphone_1', 'rb') as f:
#         unpik = pickle.Unpickler(f)
#         print(unpik.load())


class Phonebook():
    def __init__(self, pick_path: str):
        with open(pick_path, 'rb') as f:
            unpik = pickle.load(f)
        self.phone_book = unpik

    def add_to_book(self, name: str, number: str, phrase: str):
        """ add new person to phon book """
        phone_b = dict()
        phone_b['name'] = name
        phone_b['number'] = number
        phone_b['phrase'] = phrase
        self.phone_book.append(phone_b)

    def pickle_dict(self, file_path: str):
        """ make dict pickled """
        with open(file_path, 'wb') as pkf:
            pickler = pickle.Pickler(pkf)
            pickler.dump(self.phone_book)

    def unpickle_dict(self, pick_path: str) -> list:
        """ open dict """
        with open(pick_path, 'rb') as f:
            unpik = pickle.load(f)
        return unpik


pb = Phonebook


def new_add_to():
    """ get the thiigs to add """

    bname = input('what is the name ')
    bnumber = input('what is the number ')
    bphrase = input('what is the phrase ')
    return bname, bnumber, bphrase


def up_date_p(the_dict: dict):
    """ update the dict """

    lol_thigs = 'idk'
    print('what would you like to change')
    p_keys = list(the_dict.keys())
    user_input = input(f'{p_keys} or q ')
    if user_input == 'q':
        pass
    else:
        to_change = the_dict.phone_book[user_input]
        canged = input(f'change {to_change} to ')


def show_people(b_ins: pb):
    list_of = b_ins.phone_book
    for per in list_of:
        print(per['name'])


def pick_people(b_ins: pb):
    list_peps = b_ins.phone_book
    # men_d = {i: nper for i, nper in enumerate(list_peps, start=1)}
    men_d = dict(enumerate(list_peps, start=1))
    for n, pers in men_d.items():
        print(n, pers['name'])
    user_input = int(input('who do you chose '))
    return men_d[user_input]['number']





def text_func(number, payload):
    account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to='+1' + dest,
                                     from_="+14243512633",
                                     body=payload)
    print(f'sent to {dest}')
    print(message)


def start_men(instance: pb):
    """ show stat menu and let people choos thigs """

    print('welcom to the fantstic dictinary')

    while True:
        print('what would you like to do,\n\
        [a]dd person, [c]hange person, [l]ist person or [s]ave')
        user_input = input('> ')

        if user_input == 'a':
            instance.add_to_book(*new_add_to())
        elif user_input == 'c':
            print('lol i hvent made this')
        elif user_input == 'l':
            show_people(instance)
        elif user_input == 's':
            save_input = input('would you like to save to defalt [y|n] ')
            if save_input == 'y':
                pickle_path = '/home/chris/proj/pickeld/phone_2'
                instance.pickle_dict(pickle_path)
        elif user_input == 't':
            pick_people(instance)
            text_func()
        elif user_input == 'q':
            break






def lord_func():
    """ the start func """

    #pickle_path = '/home/chris/proj/pickeld/phone_2'
    #start_men()
    #first_book = Phonebook(p_book=list())    # Makes new phonebok
    # first_book.add_to_book(*new_add_to())    # Updates phone book with entry
    # first_book.pickle_l_dict(pickle_path)
    # up_date_p(first_book.phone_book)
    # pickel_this_shit(first_book.phone_book, pickle_path)
    # open_pic()

    pickle_path = '/home/chris/proj/pickeld/phone_2'
    # sunstantat dict
    cl_pbook = Phonebook(pickle_path)
    print(cl_pbook.phone_book)
    start_men(cl_pbook)



if __name__ == '__main__':
    lord_func()
