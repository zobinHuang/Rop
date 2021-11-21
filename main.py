import os
import time
import argparse
import yaml
import logging
from src.topo import topo

# function:     parse_commandline()
# description:  readin commandline parameters
# parameters:   none
# return value: 'argparse.ArgumentParser' object
def parse_commandline():
    current_work_dir = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(description='Routing Optimization Routine, zobinHuang @ 2021')

    # parameter 'topo': location of topology file
    parser.add_argument(
        '--topo', 
        type = str, 
        help = 'location of topology file', 
        default = os.path.join(current_work_dir, 'conf/topo/example.yaml')
    )

    # parameter 'demand': location of demand file
    parser.add_argument(
        '--demand', 
        type=str,
        help='location of demand file', 
        default = os.path.join(current_work_dir, 'conf/demand/example.yaml')
    )
    
    # parameter 'log': location of log file
    parser.add_argument(
        '--log', 
        type=str,
        help='location of log file', 
        default = os.path.join(current_work_dir, 'log/' + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
    )

    return parser

# function:     parse_file()
# description:  parse topology file and demand file
# parameters:   topo_path:      location of topology file
#               demand_path:    location of demand file
# return value: none
def parse_file(topo_path:str, demand_path:str):
    # parse topology file
    try:
        logging.info('read topology file from ' + topo_path)
        topo_file = open(topo_path, 'r', encoding="utf-8")
    except OSError as error:
        logging.error('topology file ' + topo_path + ' does not exist.')
    finally:
        # readin and parse yaml data
        topo_data = topo_file.read()
        topo_yaml_data = yaml.load(topo_data, Loader=yaml.Loader)['topo']
        # print(topo_yaml_data)

        # check size of topology
        if topo_yaml_data['size'] != len(topo_yaml_data['nodes']):
            logging.warning('the specific size of topology (i.e. ' + str(topo_yaml_data['size']) +') does not macth the number of nodes, use the actual nodes amount (i.e. ' + str(len(topo_yaml_data['nodes'])) + ') instead')
        topo_size = len(topo_yaml_data['nodes'])       

        # build topo
        t = topo(topo_size=topo_size) 
        for node in topo_yaml_data['nodes']:
            if node['id'] > topo_size:
                logging.error('node index of ' + str(node['id']) + ' is out of range (i.e ' + str(topo_size) + ')')
                os._exit()
        
            # create node in topo
            t.add_node(node_index=node['id'])

            # fullfill the adjacency matrix in topo
            for neighbor in node['neighbor']:
                if neighbor['peer'] > topo_size:
                    logging.error('failed to create neighbor for node ' + str(node['id']) +', neighbor index of ' + str(neighbor['peer']) + ' is out of range (i.e ' + str(topo_size) + ')')
                    os._exit()
                
                if neighbor['weight'] <= 0:
                    logging.error('failed to create neighbor for node ' + str(node['id']) +', link weight of ' + str(neighbor['weight']) + ' is non-positive which is not allowed')
                    os._exit()
                t.add_link(src_node=node['id'], dest_node=neighbor['peer'], weight=neighbor['weight'])

        t.print_topo()

    # parse demand file
    try:
        logging.info('read demand file from ' + demand_path)
        demand_file = open(demand_path, 'r', encoding="utf-8")
    except OSError as error:
        logging.error('demand file ' + demand_path + ' does not exist.')
    finally:
        pass

# function:     main()
# description:  main routine
# parameters:   none
# return value: none
def main():
    # parse commandline parameters
    parser = parse_commandline()
    args = parser.parse_args()

    # config log file
    logging.basicConfig(level=logging.DEBUG, filename=args.log, filemode='w', format='%(name)s - %(levelname)s - %(message)s')

    # parse topology and demand file
    parse_file(topo_path=args.topo, demand_path=args.demand)

if __name__ == "__main__":
    main()