# use hhtp requests to get json and priuntrtes
import requests


def make_upper(person_n: dict):
    t = person_n['title'][0].upper() + person_n['title'][1:]
    f = person_n['first'][0].upper() + person_n['first'][1:]
    l = person_n['last'][0].upper() + person_n['last'][1:]
    return t + ' ' + f + ' ' + l


def get_json(weburl: str):
    r = requests.get(weburl)
    data = r.json()
    # name = data['results'][0]['name'].values()
    people = data['results']
    for person in people:
        person_name = person['name']
        p_name = make_upper(person_name)
        print(p_name)




#        name = data['results'][i]['name'].values()
#        print(' '.join(list(name)))
#        print(data['results'][0].keys())
#        li_name = list(name)
#        new_li_name.append(li_name[0][0].upper() + li_name[0][1:])
#        new_li_name.append(li_name[1][0].upper() + li_name[1][1:])
#        #new_str_name.append(li_name[1][0].upper() + li_name[1][1:])
#        #new_str_name = li_name[2][0].upper() + li_name[2][1:]
#        print(new_li_name)




get_json('http://api.randomuser.me/?results=5')
