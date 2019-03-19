

def new_fun(var1, var2):
    pass

diction = {
    'name':'oye',
    'class':''
}
def another_fun(**kwargs):
    if kwargs.get('class'):
        print('works')
    else:
        print('not works')

another_fun(**diction)