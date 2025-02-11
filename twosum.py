def twosum(inp_array,target):
    i = 0
    dict_map = {}
    for ele in inp_array:
        if ele in dict_map:
            return [i, dict_map[ele]]

        dict_map[target-ele] = i

        i = i + 1

    return


if __name__ == '__main__':

    twosum(inp_array=[3,5,7,13], target=10)