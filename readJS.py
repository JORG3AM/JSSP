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
    ids = get_ids(list, "Nb")
    n = ids[2] - ids[0]
    list_of_lists = [list[i:i + n] for i in range(0, len(list), n)]    
    return list_of_lists

def get_info_instances(instances):
    instances_info = []
    for i in range(len(instances)):
        ids1 = get_ids(instances[i], "Nb")
        ids2 = get_ids(instances[i], "Times")
        instances_info.append(instances[i][ids1[0]:ids2[0]+1])

    col1 = [' '.join(instances_info[0][0:3]), 
            ' '.join(instances_info[0][3:6]),
            ' '.join(instances_info[0][6:8]),
            ' '.join(instances_info[0][8:10]),
            ' '.join(instances_info[0][10:12]),
            ' '.join(instances_info[0][12:14])]
    
    col2 = []
    for i in range(len(instances)):
            list = instances_info[i][14:20]
            list = [int(numeric_string) for numeric_string in list]
            col2.append(list)

    df = pd.DataFrame(col2, columns = col1)
    return df

def get_times_from_instances(instances, shape):
    instances_times = []
    for i in range(len(instances)):
        ids1 = get_ids(instances[i], "Times")
        ids2 = get_ids(instances[i], "Machines")
        list = instances[i][ids1[0]+1:ids2[1]]
        list = [int(numeric_string) for numeric_string in list]
        instance = np.array(list).reshape((shape[0],shape[1]))
        instances_times.append(instance)
    return instances_times

def get_machines_from_instances(instances, shape):
    instances_machines = []
    for i in range(len(instances)):
        ids1 = get_ids(instances[i], "Machines")
        list = instances[i][ids1[1]+1::]
        list = [int(numeric_string) for numeric_string in list]
        instance = np.array(list).reshape((shape[0],shape[1]))
        instances_machines.append(instance)
    return instances_machines

def get_instances(data, shape):
    data_list = read_txt(data)
    instances = list_to_listoflists(data_list)
    instances_info = get_info_instances(instances)
    instances_times = get_times_from_instances(instances, shape)
    instances_machines = get_machines_from_instances(instances, shape)
    return instances_info, instances_times, instances_machines

def main():
    #--------------------------Modifiable--------------------------#
    data = "tai20_15.txt"
    shape = (20,15)
    n_instance = 0
    #--------------------------------------------------------------#
    info_df, all_times, all_machines = get_instances(data, shape)
    
    machines = all_machines[n_instance]
    times = all_times[n_instance]
    
    jobs_data = []
    for id_m, machine in enumerate(machines):
        for id_t, time in enumerate(times):
            jobs_data.append(zip(machine, time))
    print(jobs_data[0])

if __name__ == '__main__':
    main()