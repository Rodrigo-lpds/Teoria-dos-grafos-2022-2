import graph_reader as gr

if __name__ == "__main__":
    graph_example = gr.read_graph_file('./graph_example.txt')
    print(graph_example)