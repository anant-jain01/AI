from graphviz import Digraph

# Create a new directed graph
dot = Digraph(comment='AI-Powered Content Marketing Agent System')

# Nodes (Agents)
dot.node('A', '🧠 Content Strategist Agent\n(SEO & Topic Planning)')
dot.node('B', '✍️ Content Creator Agent\n(Generate Drafts & Scripts)')
dot.node('C', '🔍 SEO Optimizer Agent\n(Enhance for Search & Readability)')
dot.node('D', '🔄 Repurposer Agent\n(Format-Specific Adaptations)')
dot.node('E', '📤 Publisher Agent\n(CMS Integration & Scheduling)')
dot.node('F', '📊 Performance Feedback Agent\n(Analytics & ROI Loop)')

# Edges (Workflow)
dot.edge('A', 'B', label='Brief + Strategy')
dot.edge('B', 'C', label='Raw Content Draft')
dot.edge('C', 'D', label='SEO-Optimized Content')
dot.edge('D', 'E', label='Multi-Format Versions')
dot.edge('E', 'F', label='Published Content')
dot.edge('F', 'A', label='Performance Insights')

# Render the flowchart
dot.render('/mnt/data/ai_content_marketing_flowchart', format='png', cleanup=False)
dot.render('/mnt/data/ai_content_marketing_flowchart', format='pdf', cleanup=False)
dot.view()  # This will show the graph in supported environments
'/mnt/data/ai_content_marketing_flowchart.png'  # Return path to image file for display
