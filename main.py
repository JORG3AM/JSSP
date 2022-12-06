from readJS import *
from JSSP_v1 import *

def main():

    data = "tai20_15.txt"
    ids1 = get_ids(data,"i")
    ids2 = get_ids(data,"_")
    ids3 = get_ids(data,".txt")
    #shape = (data[ids1[0]+1:ids2[0]], data[ids2[0]+1:ids3[0]])
    shape = (20,15)
    n_instance = 1
 
    info, all_times, all_machines = get_instances(data, shape)
    real_optimal = info['lower bound'][n_instance]

    times = all_times[n_instance]
    machines = all_machines[n_instance]

if __name__ == '__main__':
    main()