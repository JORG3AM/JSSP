import numpy as np
import pandas as pd
import re

def read_txt(file):
    my_file = open(file, "r")
    data = my_file.read()
    data = re.split(r' |\n|, ', data)
    list = [x for x in data if x != '']
    my_file.close()
    return list

def get_ids(list, ch):
    ids = [i for i,x in enumerate(list) if x == ch]
    return ids

def list_to_listoflists(list):
    ids = get_ids(list, "number")
    n = ids[2] - ids[0]
    list_of_lists = [list[i:i + n] for i in range(0, len(list), n)]    
    return list_of_lists

def get_info_instances(instances):
    instances_info = []
    for i in range(len(instances)):
        ids1 = get_ids(instances[i], "number")
        ids2 = get_ids(instances[i], ":")
        instances_info.append(instances[i][ids1[0]:ids2[1]+1])

    col1 = [' '.join(instances_info[0][0:3]), 
            ' '.join(instances_info[0][3:6]),
            ' '.join(instances_info[0][6:8]),
            ' '.join(instances_info[0][8:10]),
            ' '.join(instances_info[0][11:13])]
    
    col2 = []
    for i in range(len(instances)):
            list = instances_info[i][14:19]
            list = [int(numeric_string) for numeric_string in list]
            col2.append(list)

    df = pd.DataFrame(col2, columns = col1)
    return df

def get_ptimes_instances(instances, shape):
    instances_times = []
    for i in range(len(instances)):
        ids1 = get_ids(instances[i], ":")
        list = instances[i][ids1[1]+1::]
        list = [int(numeric_string) for numeric_string in list]
        instance = np.array(list).reshape((shape[1],shape[0]))
        instances_times.append(instance)
    return instances_times

def get_instances(data, shape):
    data_list = read_txt(data)
    instances = list_to_listoflists(data_list)
    instances_info = get_info_instances(instances)
    instances_times = get_ptimes_instances(instances, shape)
    return instances_info, instances_times

# def main():
#     #--------------------------Modifiable--------------------------#
#     data = "tai20_5.txt"
#     shape = (20,5)
#     n_instance = 7
#     #--------------------------------------------------------------#
#     info, times = get_instances(data, shape)
#     print(info)
#     print(times[n_instance])

# if __name__ == '__main__':
#     main()