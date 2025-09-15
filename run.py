from graphviz import Digraph

# Create a new Digraph
dot = Digraph(comment="Django Auth Tables")

# Nodes
dot.node("U", "auth_user\n(id, username, email, password, etc.)")
dot.node("UG", "auth_user_groups\n(user_id, group_id)")
dot.node("G", "auth_group\n(id, name)")
dot.node("GP", "auth_group_permissions\n(group_id, permission_id)")
dot.node("P", "auth_permission\n(id, name, codename, content_type_id)")
dot.node("UP", "auth_user_user_permissions\n(user_id, permission_id)")

# Edges
dot.edge("U", "UG", label="1..*")
dot.edge("UG", "G", label="*..1")
dot.edge("G", "GP", label="1..*")
dot.edge("GP", "P", label="*..1")
dot.edge("U", "UP", label="1..*")
dot.edge("UP", "P", label="*..1")

# Render in notebook
dot.format = "png"
file_path = "/mnt/data/django_auth_tables"
dot.render(file_path, cleanup=False)

file_path + ".png"