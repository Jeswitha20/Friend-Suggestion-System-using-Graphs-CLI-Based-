import networkx as nx
import matplotlib.pyplot as plt

# Graph Object
G = nx.Graph()

# Add User
def add_user(user):
    if user not in G.nodes:
        G.add_node(user)
        print(f"User '{user}' added.")
    else:
        print(f"User '{user}' already exists.")

# Add Friendship
def add_friend(user1, user2):
    if user1 in G.nodes and user2 in G.nodes:
        if not G.has_edge(user1, user2):
            G.add_edge(user1, user2)
            print(f"Friendship between '{user1}' and '{user2}' added.")
        else:
            print("They are already friends.")
    else:
        print("One or both users do not exist.")

# Show Friends
def show_friends(user):
    if user in G.nodes:
        friends = list(G.neighbors(user))
        if friends:
            print(f"Friends of {user}: {', '.join(friends)}")
        else:
            print(f"{user} has no friends.")
    else:
        print("User does not exist.")

# Suggest Friends
def suggest_friends(user):
    if user not in G.nodes:
        print("User does not exist.")
        return
    
    friends = set(G.neighbors(user))
    suggestions = {}

    for friend in friends:
        for fof in G.neighbors(friend):
            if fof != user and fof not in friends:
                suggestions[fof] = suggestions.get(fof, 0) + 1
    
    if suggestions:
        print(f"Friend suggestions for {user}:")
        for s, count in sorted(suggestions.items(), key=lambda x: -x[1]):
            print(f"{s} (Mutual Friends: {count})")
    else:
        print("No friend suggestions.")

# Visualize Graph
def visualize_graph():
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold', edge_color='gray')
    plt.title("Friendship Graph", fontsize=15)
    plt.show()

# CLI Loop
while True:
    print("\nFriend Suggestion System (with Graph Visualization)")
    print("1. Add User")
    print("2. Add Friend")
    print("3. Show Friends")
    print("4. Suggest Friends")
    print("5. Show Graph")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        user = input("Enter user name: ")
        add_user(user)
    elif choice == '2':
        u1 = input("Enter first user: ")
        u2 = input("Enter second user: ")
        add_friend(u1, u2)
    elif choice == '3':
        user = input("Enter user name to show friends: ")
        show_friends(user)
    elif choice == '4':
        user = input("Enter user name to suggest friends: ")
        suggest_friends(user)
    elif choice == '5':
        visualize_graph()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")

# The following code is an alternative implementation of a Friend Suggestion System using a graph structure.
# graph={}

# # Adding a person (node)
# def add_user(user):
#     if user not in graph:
#         graph[user] = []
#         print(f"User '{user}' added successfully.")
#     else:
#         print(f"User '{user}' already exists.")

# # Adding a friendship (edge)
# def add_friend(user1, user2):
#     if user1 in graph and user2 in graph:
#         if user2 not in graph[user1]:
#             graph[user1].append(user2)
#             graph[user2].append(user1)
#             print(f"Friendship between '{user1}' and '{user2}' added successfully.")
#     else:
#         print(f" '{user1}' or '{user2}' persons do not exist.")

# # Showing friends of a person
# def show_friends(user):
#     if user in graph:
#         friends = graph[user]
#         if friends:
#             print(f"Friends of '{user}': {', '.join(friends)}")
#         else:
#             print(f"'{user}' has no friends.")
#     else:
#         print(f"User '{user}' does not exist.")

# # Suggesting friends based on mutual friends
# def suggest_friends(user):
#     if user not in graph:
#         print(f"User '{user}' does not exist.")
#         return
    
#     friends = graph[user]
#     suggestions = set()
    
#     for friend in friends:
#         for mutual_friend in graph[friend]:
#             if mutual_friend != user and mutual_friend not in friends:
#                 suggestions.add(mutual_friend)
    
#     if suggestions:
#         print(f"Friend suggestions for '{user}': {', '.join(suggestions)}")
#     else:
#         print(f"No friend suggestions available for '{user}'.")
    
# def show_graph():
#     for user in graph:
#         print(f"{user}: {', '.join(graph[user])}")
# # Main CLI loop 
# while True:
#     print("\nFriend Suggestion System")
#     print("1. Add User")    
#     print("2. Add Friend")
#     print("3. Show Friends")
#     print("4. Suggest Friends")
#     print("5. Show Graph")
#     print("6. Exit")
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         user = input("Enter user name: ")
#         add_user(user)
#     elif choice == '2':
#         user1 = input("Enter first user name: ")
#         user2 = input("Enter second user name: ")
#         add_friend(user1, user2)
#     elif choice == '3':
#         user = input("Enter user name to show friends: ")
#         show_friends(user)
#     elif choice == '4':
#         user = input("Enter user name to suggest friends: ")
#         suggest_friends(user)
#     elif choice == '5':
#         show_graph()
#     elif choice == '6':
#         print("Exiting the system.")
#         break
#     else:
#         print("Invalid choice. Please try again.")