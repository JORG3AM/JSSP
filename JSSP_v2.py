import numpy as np
from pyhermes import Problem
from readJS import *
import random

def sequence_constrain(jobs):
    for job_id, job in enumerate(jobs):
        if (job[job_id][0]+job[job_id][1]<=job[job_id+1][0]):
            return True
        else:
            return False

def oneAtATime_constrain(jobs):
    for job_id, job in enumerate(jobs):
        if (job[job_id][0]+job[job_id][1]<=job[job_id+1][0]):
            return True
        else:
            return False

def next_operation_order_default(jobs_data):
    jobs_order = []
    for job_id, job in enumerate(jobs_data):
        jobs_order.append(random.sample(job, len(job)))
    jobs_order = random.sample(jobs_order, len(jobs_order))
    return jobs_order

def next_operation_order_LPT(opeations):
    pass

def next_operation_order_SPT(opeations):
    pass

def next_operation_order_MPA(opeations):
    pass

def next_operation_order_LPA(opeations):
    pass

def main():
    # #--------------------------Modifiable--------------------------#
    # data = "tai15_15.txt"
    # shape = (15, 15)
    # n_instance = 0
    # #--------------------------------------------------------------#
    # info_df, all_times, all_machines = get_instances(data, shape)

    # machines = all_machines[n_instance]
    # times = all_times[n_instance]

    # real_optimal = info_df['Lower bound'][n_instance]

    # job = []
    # jobs_data = []
    # for id_m, machine in enumerate(machines):
    #     for id_t, time in enumerate(times):
    #         job.append((machine[id_t], time[id_t]))
    #     jobs_data.append(job)

    jobs_data = [  # task = (machine_id, processing_time).
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3), (0, 5)]  # Job2
    ]
    print(jobs_data)

    machines_count = 1 + max(task[0] for job in jobs_data for task in job)
    all_machines = range(machines_count)
    horizon = sum(task[1] for job in jobs_data for task in job)

    # jobs_order = np.empty()
    # for job_id, job in enumerate(jobs_data):
    #     for task_id, task in enumerate(job):
    #         machine = task[0]
    #         duration = task[1]
            
    jobs_order = []
    for job_id, job in enumerate(jobs_data):
        jobs_order.append(random.sample(job, len(job)))
    jobs_order = random.sample(jobs_order, len(jobs_order))
   
    print(jobs_order)

    for job_id, job in enumerate(jobs_order):
        for task_id, task in enumerate(job):
            if (sequence_constrain(job) & oneAtATime_constrain(job)):
                print('Done!')
            else:
                print('No solution found!')
            
if __name__ == '__main__':
    main()
