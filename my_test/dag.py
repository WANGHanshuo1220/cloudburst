import sys
from threading import local
sys.path.append('../')
from cloudburst.client.client import CloudburstConnection

HYDRO_CLUSTER_FUNC_ELB="18.176.37.179"

local_cloud = CloudburstConnection('127.0.0.1', 
                                   '127.0.0.1', 
                                   local=True)

def add(_, x):
    return x+1

def minus(_, x):
    return x-1

def square(_, x):
    list_x = list(x)
    return {list_x[0]*2, list_x[1]*3}

def algebra(_, x):
    list_x = list(x)
    return list_x[0] + list_x[1] 

def sum(_, x, y):
    return x + y*2

func1 = local_cloud.register(add, 'add')
func2 = local_cloud.register(minus, 'minus')
func3 = local_cloud.register(square, 'square')
func4 = local_cloud.register(algebra, 'algebra')
func5 = local_cloud.register(sum, 'sum')

edge1 = ('add', 'square')
edge2 = ('square', 'algebra')
edge3 = ('algebra', 'sum')
edge4 = ('minus', 'sum')

edge5 = ('add', 'sum')
edge6 = ('minus', 'sum')

# succ, err = local_cloud.register_dag('func_dag', 
#             ['add', 'square', 'algebra', 'minus', 'sum'],
#             [edge1, edge2, edge3, edge4])
# assert(succ)
succ, err = local_cloud.register_dag('func_list', 
                        ['add', 'minus', 'sum'],
                        [edge5, edge6])
assert(succ)
print(local_cloud.call_dag('func_list', 
                    {'add': [0], 'minus': [11]}, True))
