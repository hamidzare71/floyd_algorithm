import networkx as nx
import matplotlib.pyplot as plt  # plotting and show the graph
import math  # call infinite number from math lib

G = nx.DiGraph()  # create a Direct Graph from networkx as G


def floyd_initial_diagraph_create():
    # initial nodes and directed edges for testing

    G.add_nodes_from([0, 1, 2, 3, 4])
    G.add_weighted_edges_from([(0, 1, 1),
                               (0, 4, 2),
                               (1, 2, 3),
                               (1, 3, 2),
                               (2, 4, -4),
                               (3, 0, 2),
                               (3, 2, 5),
                               (4, 1, 4)])


def floyd_digraph_create_from_user():
    # input nodes and edges weight from user

    print("Enter nodes as int and weight as float")

    try:
        node = int(input('How many Nodes?'))
    except:
        print("\nI've mentioned U :(")
        node = int(input('again, How many f.. Nodes?'))

    # add node 0 to 'node'
    for i in range(node):
        G.add_node(i)
    print('nodes: ', G.nodes, 'created')

    input_text = "Enter source: "
    while True:
        try:
            # input src-->des and it's weight
            edge_src = int(input(input_text))
            edge_des = int(input("Enter destination: "))
            edge_weight = float(input("Add weight: "))
            G.add_edges_from([(edge_src, edge_des)], weight=edge_weight)

            input_text = "Enter c to finish or enter another source: "
            inpt = input("wanna finish? press 'c'\n"
                         "             else press any: ")
            if inpt == 'c':
                # print("\nPressed 'c' , end...\n ")
                print("nodes: ", G.nodes)
                print("edges: ", G.edges)
                break
            else:
                pass
        except:
            # print("except handling test")
            continue


def floyd_plotting_graph():
    # plotting Directed graph and its weight

    # test the prepared shortest path method from networkx lib
    print("networkx.shortest_path(G, src=0): ", nx.shortest_path(G, 0))
    print("networkx.shortest_path_length(G, src=0): ", nx.shortest_path_length(G, 0))
    pos = nx.spring_layout(G)  # positions for all nodes random
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


def floyd_cost_list_maker():
    # make weight list n*n as First cost matrices

    g_num_nodes = G.number_of_nodes()
    rows_count = g_num_nodes
    cols_count = g_num_nodes
    cost_list = [[0 for j in range(cols_count)] for i in range(rows_count)]  # initialize with 0
    for i in range(g_num_nodes):
        for j in range(g_num_nodes):
            if i == j:  # main diameter(Ghotr)=0
                cost_list[i][j] = 0.0
            elif G.get_edge_data(i, j) == None:  # no direct path so [hamidzare@IEEE.org]make it [Infinite]
                cost_list[i][j] = math.inf  # infinite number import from math lib
            else:
                G_attr = G.get_edge_data(i, j).get('weight')
                cost_list[i][j] = G_attr
    floyd_cost_list_printer(g_num_nodes, cost_list)  # after make the matrice(list)-->print it
    floyd_algorithm(cost_list)  # call the main floyd algorithm


def floyd_cost_list_printer(g_num_nodes, cost_list):
    # print the first cost matrices

    print('\nFirst Cost Matrices:')  # print name of [hamidzare@IEEE.org]dimention matrice
    print("\t {} \t\t{} \t\t{} \t\t{} \t\t{}".format(0, 1, 2, 3, 4))
    print('--------------------------------------')

    for i in range(g_num_nodes):
        print("{0}|".format(i), ' ', end='')

        for j in range(G.number_of_nodes()):
            print(cost_list[i][j], str.ljust('  ', 3, ' '), sep='\t', end='')
        print('')


def floyd_algorithm(cost_list):
    # main algorithm define the [hamidzare@IEEE.org]shortest path and make Path matrices

    g_num_nodes = G.number_of_nodes()
    rows_count = g_num_nodes
    cols_count = g_num_nodes
    path_list = [[-1 for j in range(cols_count)] for i in range(rows_count)]  # initialize with 0
    g_num_nodes = G.number_of_nodes()
    k = 1
    for k in range(g_num_nodes):
        for i in range(g_num_nodes):
            for j in range(g_num_nodes):
                if cost_list[i][j] == math.inf or cost_list[i][j] > cost_list[i][k] + cost_list[k][j]:
                    cost_list[i][j] = cost_list[i][k] + cost_list[k][j]
                    path_list[i][j] = k

    print('\nShortest path matrices(Final costs: ')
    print("\t {} \t\t{} \t\t{} \t\t{} \t\t{}".format(0, 1, 2, 3, 4))
    print('--------------------------------------')

    for i in range(g_num_nodes):
        print("{0}|".format(i), ' ', end=' ')
        for j in range(G.number_of_nodes()):
            print(cost_list[i][j], str.ljust('  ', 3, ' '), sep='\t', end='')
        print('')

    # print Path matrices
    print('\nPath matrices(interface nodes): ')
    print("\t {} \t\t{} \t\t{} \t\t{} \t\t{}".format(0, 1, 2, 3, 4))
    print('--------------------------------------')

    for i in range(g_num_nodes):
        print("{0}|".format(i), ' ', end=' ')
        for j in range(G.number_of_nodes()):
            print(path_list[i][j], ' ', sep='  ', end='\t')
        print('')

    # interface weigt between 2 nodes
    qst = input('\nwanna show shortest path between 2 node?'
                'y/n?')
    if qst == 'y':
        src_node = int(input("enter source node: "))
        des_node = int(input("enter destination node: "))
        shortest_path_two_node(path_list, src_node, des_node)
        print('shortest length between [', src_node, '] --> [', des_node, '] is: ', cost_list[src_node][des_node])
    else:
        pass


def shortest_path_two_node(path_list, src_node, des_node):
    # show interface nodes between 2 nodes

    if path_list[src_node][des_node] != -1:
        shortest_path_two_node(path_list, src_node, path_list[src_node][des_node])
        print("Interface node: ", path_list[src_node][des_node])
        shortest_path_two_node(path_list, path_list[src_node][des_node], des_node)


def floyd_directed_path_weight():
    # find the Directed[hamidzare@IEEE.org]path for every nodes to other
    # and append it to an axis list
    print("\ndirect path Node [i]-->[j]")
    my_list = []
    for i in range(G.number_of_nodes()):
        for j in range(G.number_of_nodes()):
            if G.get_edge_data(i, j) != None:  # determine there is direct edge between i,j
                # cast weight Values to float( was so boring :) thanks JADI
                G_attr = G.get_edge_data(i, j).get('weight')
                print('Node [', i, ']-->[', j, ']: ', G_attr, "\t")
                my_list.append(G_attr)
    print('list of weight: ', my_list)


# floyd_initial_diagraph_create()
floyd_digraph_create_from_user()
floyd_plotting_graph()  # plot and show Digraph
floyd_cost_list_maker()  # make cost matrices
