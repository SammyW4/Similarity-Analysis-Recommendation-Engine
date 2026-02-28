import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt
import time

BASE_URL = "https://en.wikipedia.org"
START_PAGE = "/wiki/Artificial_intelligence"
LEVEL1_LIMIT = 20
LEVEL2_LIMIT = 10

def get_links(page):
    url = BASE_URL + page

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    links = []
    
    for link in soup.find_all("a"):
        href = link.get("href")
        
        
        if href and href.startswith("/wiki/") and ":" not in href:
            links.append(href)
    
    return list(set(links))


edges = []

print("Collecting level 1 links...")
level1_links = get_links(START_PAGE)[:LEVEL1_LIMIT]
print("Level 1 links found:", len(level1_links))


for link in level1_links:
    edges.append((START_PAGE, link))
    
    print(f"Collecting level 2 links from {link}")
    
    try:
        level2_links = get_links(link)[:LEVEL2_LIMIT]
        
        for l2 in level2_links:
            edges.append((link, l2))
        
        time.sleep(1)
    
    except:
        continue

G = nx.DiGraph()
G.add_edges_from(edges)

print(f"\nTotal nodes: {len(G.nodes())}")
print(f"Total edges: {len(G.edges())}")

pagerank = nx.pagerank(G)

top_nodes = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 Important Nodes (PageRank):")
for node, score in top_nodes:
    print(node, score)

pagerank = nx.pagerank(G)

top_nodes = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 Important Nodes (PageRank):")
for node, score in top_nodes:
    print(node, score)

plt.figure(figsize=(10,8))
nx.draw(G, node_size=20, arrows=False)
plt.title("AI Wikipedia Network")
plt.show()

labels = [node.replace("/wiki/", "") for node, _ in top_nodes]
scores = [score for _, score in top_nodes]

plt.figure(figsize=(8,5))
plt.barh(labels, scores)
plt.xlabel("PageRank Score")
plt.title("Top 5 Important Articles")
plt.show()