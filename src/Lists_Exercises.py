
heros=['spider man','thor','hulk','iron man','captain america']

def length_of_list():
    print(len(heros))

def add_black_panther():
    heros.append('black panther')
    print(heros)

def remove_add_blackpanther():

    heros.remove('black panther')
    print(heros)
    leng = len(heros)
    print(leng)
    for i in range(0,leng):
        #print(heros[i])
        if heros[i]=='hulk':
            #print(heros[i])
            heros.insert(i+1,'black panther')
    #        heros.insert(i,'black panther')
    print(heros)

def replace_thor_add_strange():
    heros[1:3]=['doctor strange']
    print(heros)

def sort_alpha():
    print(sorted(heros))

def odd_number():
    list = int(input('Enter the Max number : '))
    oddnumber = []
    for i in range(0,list):
        if (i % 2 !=0):
            oddnumber.append(i)
    print(oddnumber)
    print(len(oddnumber))


if __name__ == '__main__':

    length_of_list()
    add_black_panther()
    remove_add_blackpanther()
    replace_thor_add_strange()
    sort_alpha()
    odd_number()
