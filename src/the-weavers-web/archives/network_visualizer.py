#!/usr/bin/env python3
"""
Graph Tapestries - Network Graph Visualizer (NetworkX-free version)
Weaving node and edge connections into visual tapestries...
"""

import numpy as np
import matplotlib.pyplot as plt
import os

class GraphWeaver:
    """Main class for weaving graph tapestries (without networkx dependency)"""
    
    def __init__(self):
        self.nodes = {}
        self.edges = []
        
    def add_node(self, node_id, x=None, y=None, label=None, attributes=None):
        """Add a node with position and optional attributes"""
        if x is None or y is None:
            # Auto-generate circular layout positions
            import math
            angles = list(np.linspace(0, 2*np.pi, len(self.nodes)+1)) if self.nodes else [0]
            angle_index = (list(self.nodes.keys()).index(node_id) + 1) % len(angles) if self.nodes else 0
            angle = np.cos(angle_index * 2 * np.pi / max(len(self.nodes), 1))
            radius = 200
            x = 400 + radius * angle
            y = 300 + radius * np.sin(angle_index * 2 * np.pi / max(len(self.nodes), 1))
        
        node_dict = {
            'x': x,
            'y': y,
            'label': label or node_id,
        }
        if attributes:
            node_dict.update(attributes)
        self.nodes[node_id] = node_dict
    
    def add_edge(self, u, v, weight=1.0, attributes=None):
        """Add an edge between nodes"""
        self.edges.append((u, v, weight))
        
    def weave_layout_from_dict(self, graph_data):
        """Load a graph from a dictionary and compute positions"""
        
        # Calculate circular layout for nodes
        node_count = len(graph_data['nodes'])
        radius = 200
        center_x, center_y = 400, 300
        
        for i, (node_id, node_attrs) in enumerate(graph_data['nodes'].items()):
            angle = 2 * np.pi / node_count * (i + 1) if node_count > 0 else 0
            x = center_x + radius * np.cos(angle)
            y = center_y + radius * np.sin(angle)
            
            self.add_node(node_id, 
                         x=x, y=y, 
                         label=node_attrs.get('label', node_id),
                         attributes=node_attrs)
        
        # Add edges from the data - Handle both tuple and dict edge formats
        for edge in graph_data['edges']:
            if isinstance(edge, dict):
                u, v = edge['u'], edge['v']
                weight = edge.get('weight', 1.0)
            else:  # It's a tuple (u, v, weight=1) or similar
                u, v = edge[0], edge[1]
                weight = edge[2] if len(edge) > 2 else 1.0
            
            if u in self.nodes and v in self.nodes:
                self.add_edge(u, v, weight=weight)
    
    def weave_layout_from_dict_list(self, graph_data):
        """Load a graph from list-based format (more Pythonic)"""
        
        for node_id, node_attrs in graph_data['nodes'].items():
            x = 400 + 200 * np.cos(2 * np.pi / len(graph_data['nodes']) * (list(graph_data['nodes'].keys()).index(node_id) + 1))
            y = 300 + 200 * np.sin(2 * np.pi / len(graph_data['nodes']) * (list(graph_data['nodes'].keys()).index(node_id) + 1))
            
            self.add_node(node_id, 
                         x=x, y=y, 
                         label=node_attrs.get('label', node_id),
                         attributes=node_attrs)
        
        # Handle list of tuples or dicts for edges
        for edge in graph_data['edges']:
            if isinstance(edge, dict):
                u, v = edge['u'], edge['v']
                weight = edge.get('weight', 1.0)
            else:
                u, v = edge[0], edge[1]
                weight = edge[2] if len(edge) > 2 else 1.0
            
            if u in self.nodes and v in self.nodes:
                self.add_edge(u, v, weight=weight)
    
    def visualize(self, save_path=None):
        """Create a visual tapestry of the graph"""
        
        if len(self.nodes) == 0:
            print("Graph is empty - cannot weave visual tapestry")
            return None
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Draw edges first (so they appear behind nodes)
        for u, v, weight in self.edges:
            if u in self.nodes and v in self.nodes:
                x1, y1 = self.nodes[u]['x'], self.nodes[u]['y']
                x2, y2 = self.nodes[v]['x'], self.nodes[v]['y']
                
                # Create edge path
                nx1, ny1 = x1 + weight * (x2 - x1) / 50, y1 + weight * (y2 - y1) / 50
                ax.plot([nx1, x2], [ny1, y2], color='#4a4e69', linewidth=weight/2, alpha=0.6)
        
        # Draw nodes as circles
        for node_id, data in self.nodes.items():
            x, y = data['x'], data['y']
            
            # Determine node color based on attributes
            if 'type' in data:
                if data['type'] == 'center':
                    color = '#f4a261'  # Orange for center/hub
                else:
                    color = '#6b5b95'  # Purple for regular nodes
            else:
                color = '#6b5b95'
            
            ax.scatter(x, y, s=800, c=color, alpha=0.7)
        
        # Draw labels
        for node_id, data in self.nodes.items():
            label = data.get('label', str(node_id))
            if label.upper() != 'HUB':
                ax.text(data['x'], data['y'], label, 
                       color='white', ha='center', va='center', fontsize=10)
        
        # Draw center hub label separately
        for node_id, data in self.nodes.items():
            if data.get('label', '').upper() == 'HUB':
                ax.text(data['x'], data['y'], 'Hub', 
                       color='white', ha='center', va='center', fontsize=12, fontweight='bold')
        
        ax.set_title("Network Graph Tapestry", fontsize=14, color='white')
        ax.axis('off')
        ax.set_xlim(0, 800)
        ax.set_ylim(0, 600)
        
        if save_path:
            plt.tight_layout()
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            plt.close()
            print(f"Graph tapestry woven into {save_path}")
            return save_path
        
        else:
            plt.show()
            plt.close()
        
        return None
    
    def weave_statistics(self):
        """Calculate and return graph statistics"""
        
        if len(self.nodes) == 0:
            return {}
        
        from collections import defaultdict
        degree_count = defaultdict(int)
        
        for u, v, weight in self.edges:
            degree_count[u] += 1
            degree_count[v] += 1
        
        stats = {
            'num_nodes': len(self.nodes),
            'num_edges': len(self.edges),
            'density': len(self.edges) / (len(self.nodes) * (len(self.nodes) - 1)) if len(self.nodes) > 1 else 0,
            'average_degree': np.mean(list(degree_count.values())) if degree_count else 0,
        }
        
        return stats

def main():
    """Demonstrate graph weaving capabilities"""
    
    weaver = GraphWeaver()
    
    # Create a sample network
    nodes_data = {
        'H': {'label': 'Hub Node', 'type': 'center'},
        'A': {'label': 'Leaf A', 'type': 'peripheral'},
        'B': {'label': 'Leaf B', 'type': 'peripheral'},
        'C': {'label': 'Cluster 1', 'type': 'cluster'},
        'D': {'label': 'Cluster 2', 'type': 'cluster'},
        'E': {'label': 'Leaf C', 'type': 'peripheral'},
    }
    
    edges = [
        ('H', 'A'), ('H', 'B'), ('H', 'E'),      # Hub connections
        ('C', 'D'),                               # Cluster connection
        ('H', 'C'), ('H', 'D'),                   # Hub to clusters
        ('A', 'C'), ('B', 'D'),                   # Leaf-cluster bridges
    ]
    
    # Use list-based format instead of dict-based
    weaver.weave_layout_from_dict_list({'nodes': nodes_data, 'edges': edges})
    
    print("Graph Tapestry Weaver")
    print("=" * 50)
    
    stats = weaver.weave_statistics()
    
    print(f"\nGraph Statistics:")
    print(f"  Nodes: {stats.get('num_nodes', 0)}")
    print(f"  Edges: {stats.get('num_edges', 0)}")
    
    # Save visual tapestry
    output_dir = 'projects/network_threads/graph_tapestries/output'
    os.makedirs(output_dir, exist_ok=True)
    
    weaver.visualize(save_path=os.path.join(output_dir, 'network_graph_tapestry.png'))

if __name__ == '__main__':
    main()