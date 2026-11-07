#!/usr/bin/env python3
"""
ASCII Network Visualizer - Fixed-grid visualization with circular node placement.
Simple and robust version for ASCII output.
"""

import networkx as nx


def visualize_graph_ascii(G, grid_size=25):
    """Create simple ASCII visualization on a fixed grid."""
    if len(G.nodes()) == 0:
        return "Empty graph"
    
    # Use circular layout - nodes evenly spaced in a circle
    pos = nx.circular_layout(G)
    
    # Scale positions to fit within grid_size
    scale = (grid_size - 2) / (len(G.nodes()) * 1.5) if len(G.nodes()) > 0 else 1
    
    chars = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
    
    # Place nodes at positions scaled to grid
    max_idx = min(grid_size, len(G.nodes()))
    angle_step = (2 * 3.14159) / len(G.nodes()) if G.nodes() else 0
    
    for i, node in enumerate(sorted(G.nodes(), key=str)):
        angle = i * angle_step
        x = int(grid_size/2 + scale * pos[node][0])
        y = int(grid_size/2 + scale * pos[node][1])
        
        # Clamp to grid bounds
        x = max(1, min(x, grid_size - 2))
        y = max(1, min(y, grid_size - 2))
        
        chars[y][x] = '●'
    
    return '\n'.join([''.join(row) for row in chars])


def print_graph_info(G):
    """Print basic graph information."""
    print(f"\nNetwork Information:")
    print(f"  Nodes: {len(G.nodes())}")
    print(f"  Edges: {len(G.edges())}")
    
    if G.nodes():
        node_labels = ', '.join(str(n) for n in list(G.nodes())[:5])
        print(f"  Sample nodes: {node_labels}...")
    else:
        print("  No nodes")


def demo_ascii_visualizer():
    """Main demonstration function."""
    print("=" * 60)
    print("ASCII NETWORK VISUALIZER")
    print("=" * 60)
    
    # Create a sample network with communities
    G = nx.Graph()
    
    for cluster_id in range(4):
        for offset in range(3):
            node_name = f"c{cluster_id}_{offset}"
            G.add_node(node_name)
            
            if cluster_id > 0:
                center = f"c{cluster_id-1}_0"
                for offset2 in range(3):
                    G.add_edge(center, f"c{cluster_id}_{offset2}")
    
    # Add random edges between clusters
    nodes = list(G.nodes())
    import random
    for _ in range(6):
        u, v = random.sample(nodes, 2)
        if random.random() < 0.4:
            G.add_edge(u, v)
    
    # Visualize
    print("\nGraph generated with circular layout:")
    ascii_art = visualize_graph_ascii(G, grid_size=25)
    
    lines = ascii_art.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    padded_lines = [line.ljust(max_len) for line in lines]
    
    print("\n" + '\n'.join(padded_lines))
    print("=" * 60)
    
    print_graph_info(G)


if __name__ == '__main__':
    demo_ascii_visualizer()
