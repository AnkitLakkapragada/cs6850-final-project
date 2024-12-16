import random
from networkx.algorithms import community
from networkx.algorithms.community.quality import modularity

sampled_nodes = random.sample(list(G.nodes), min(500, len(G.nodes)))  
G_sampled = G.subgraph(sampled_nodes)

def detect_communities_and_calculate_modularity(graph):
    """
    Detects communities in the graph using the Louvain method and calculate modularity
    """
    communities = community.greedy_modularity_communities(graph)
    community_map = {}
    for idx, comm in enumerate(communities):
        for node in comm:
            community_map[node] = idx

    nx.set_node_attributes(graph, community_map, "community")

    modularity_score = modularity(graph, [set(comm) for comm in communities])

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)  
    for comm_idx, comm in enumerate(communities):
        nx.draw_networkx_nodes(graph, pos, nodelist=list(comm), label=f"Community {comm_idx}")
    
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, font_size=8)
    plt.title(f"Community Detection in the Network (Modularity Score: {modularity_score:.2f})")
    # plt.legend()
    plt.show()

    return modularity_score

modularity_score = detect_communities_and_calculate_modularity(G_sampled)
print(f"Modularity Score: {modularity_score:.2f}")