#!/usr/bin/env python3
"""
Network Sculptor - Graph exploration and visualization
Uses networkx to create and analyze interesting network structures.
"""

import random
import networkx as nx


def create_community_graph(num_communities=4, nodes_per_community=6):
    """Create a graph with multiple communities (clusters)."""
    G = nx.Graph()
    
    # Create communities
    for community in range(num_communities):
        for node_idx in range(nodes_per_community):
            node_name = f"n{community}_{node_idx}"
            G.add_node(node_name)
    
    # Add edges within communities (high probability)
    for i in range(num_communities):
        nodes_in_community = [f"n{i}_{j}" for j in range(nodes_per_community)]
        for n1, n2 in nx.generators.random_graphs.complete_graph(nodes_per_community, 0.3).edges():
            G.add_edge(f"n{i}_[{n1}]_[", f"n{i}_[{n2}]_")
    
    # Add random edges between communities (lower probability)
    nodes = list(G.nodes())
    for _ in range(5):
            u, v = random.sample(nodes, 2)
            G.add_edge(u, v)
    
    return G


def create_random_network(num_nodes=30, edge_prob=0.1):
    """Create a random Erdos-Renyi graph."""
    nodes = [f"node_{i}" for i in range(num_nodes)]
    G = nx.erdos_renyi_graph(len(nodes), edge_prob, seed=random.randint(0, 100))
    
    # Add labels to nodes
    for node in G.nodes():
        G.nodes[node]['label'] = f"{node[3:]}({random.randint(0,9)})"
    
    return G


def analyze_network(G):
    """Basic network analysis."""
    print(f"\nGraph Statistics:")
    print(f"  Nodes: {G.number_of_nodes()}")
    print(f"  Edges: {G.number_of_edges()}")
    print(f"  Density: {nx.density(G):.3f}")
    
    if nx.is_connected(G):
        print(f"  Connected: Yes")
    else:
        print(f"  Connected: No (components: {nx.number_connected_components(G)})")
    
    return G


def visualize_graph_ascii(G, size=40):
    """Try to create a simple ASCII layout of the graph."""
    # This is simplified - just shows node count and edges
    lines = []
    lines.append("=" * 30)
    lines.append(f"NETWORK VISUALIZATION (ASCII)")
    lines.append("=" * 30)
    lines.append(f"Nodes: {G.number_of_nodes()}")
    lines.append(f"Edges: {G.number_of_edges()}")
    
    # Show a simple representation
    node_positions = {node: random.random() for node in G.nodes()}
    sorted_nodes = sorted(G.nodes(), key=lambda n: node_positions[n])
    
    display_width = min(len(sorted_nodes), size)
    display_nodes = sorted_nodes[:display_width]
    
    for pos, node in enumerate(display_nodes):
        lines.append(f"  {node}  [degree={G.degree(node)}]")
    
    return "\n".join(lines)


def run_graph_sculptor_demo():
    """Main demonstration."""
    print("=" * 50)
    print("NETWORK SCULPTOR - Graph Exploration Tool")
    print("=" * 50)
    
    # Create and analyze a random network
    G = create_random_network(num_nodes=20, edge_prob=0.15)
    G = analyze_network(G)
    
    ascii_vis = visualize_graph_ascii(G, size=20)
    print("\n" + ascii_vis)


if __name__ == '__main__':
    run_graph_sculptor_demo()
