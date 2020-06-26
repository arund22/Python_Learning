

def cal_tax(state,income):

    state_list = {'CA':10,"WA":5,"VA":4}

    net = income - (income * .10)

    print('after federal tax: '+str(net))

    if state in state_list:
        net = net - (income * state_list[state]/100)
        print(net)
    else:

        print("state is not in list")

    return net


print(cal_tax("WA",10000))