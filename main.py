import  os
import argparse

# function:     parse_commandline()
# description:  readin commandline parameters
# parameters:   none
# return value: 'argparse.ArgumentParser' object
def parse_commandline():
    current_work_dir = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(description='Routing Optimization Routine, zobinHuang @ 2021')

    parser.add_argument(
        '--topo', 
        type = str, 
        help = 'location of topology file', 
        default = os.path.join(current_work_dir, 'conf/topo/example.topo')
    )

    parser.add_argument(
        '--demand', 
        type=str,
        help='location of demand file', 
        default = os.path.join(current_work_dir, 'conf/demand/example.demand')
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
        topo_file = open(topo_path)
    except OSError as error:
        print('Error: topology file ' + topo_path + ' does not exist.')
    finally:
        pass
    
    # parse demand file
    try:
        demand_file = open(demand_path)
    except OSError as error:
        print('Error: demand file ' + demand_path + ' does not exist.')
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

    # parse topology and demand file
    parse_file(topo_path=args.topo, demand_path=args.demand)

if __name__ == "__main__":
    main()