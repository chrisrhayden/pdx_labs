"""
# Test Data Below.  Leave this line alone.
>>> names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']

>>> people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward    ', 'Student'), ('Fin', 'Balnik', 'Student')]

>>> long_names(5)
['Kieran', 'Serada', 'Alfonzo']

>>> starts_with('S')
['Suki', 'Serada']

>>> last_names(people)
['Prasch', 'Ward', 'Balnik']

>>> smoosh(people)
['Kieran', 'Prasch', 'Instructor', 'Alfonzo', 'Ward', 'Student', 'Fin', 'Balnik', 'Student']

"""


def long_names(n_len):
    """ retu all names n cahrs long name """

    names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']
    n_names = [n_name for n_name in names if len(n_name) >= n_len]
    return n_names


def starts_with(st_l):
    """ get names with s at beginning """

    names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']
    s_name = [snam for snam in names if snam.startswith(st_l)]
    return s_name


def last_names(people):
    l_name = [lname[1].strip() for lname in people]
    return l_name


def smoosh(people):
#    new_list = []
#    for person in people:
#        for thing in person:
#            new_list.append(thing.strip())

    new_list = [nam.strip() for pers in people for nam in pers]
    return new_list


people = [('Kieran', 'Prasch', 'Instructor'),
          ('Alfonzo', 'Ward    ', 'Student'),
          ('Fin', 'Balnik', 'Student')]
names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Al    fonzo']
smoosh(people)
