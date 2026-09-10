from client import HalfEdgeMesh

def main():
    print("=== Testing Half-Edge Doubly Connected Mesh ===")
    mesh = HalfEdgeMesh()

    edges_count = mesh.build_triangle((0, 0), (1, 0), (0, 1))
    print(f"Created triangle with {edges_count} half-edges.")

    assert len(mesh.vertices) == 3
    assert len(mesh.faces) == 1
    assert mesh.half_edges[0]["next"] == 1
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
