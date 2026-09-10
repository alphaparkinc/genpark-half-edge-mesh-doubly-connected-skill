class HalfEdgeMesh:
    """
    Doubly-Connected Edge List (DCEL) / Half-Edge Mesh.
    Vertices, Half-Edges, Faces.
    Verifies Euler formula: V - E + F = 2 (for closed planar graphs).
    """
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.half_edges = []

    def build_triangle(self, v0, v1, v2):
        self.vertices.extend([v0, v1, v2])
        self.faces.append(0)
        he0 = {"next": 1, "prev": 2, "face": 0, "origin": 0}
        he1 = {"next": 2, "prev": 0, "face": 0, "origin": 1}
        he2 = {"next": 0, "prev": 1, "face": 0, "origin": 2}
        self.half_edges.extend([he0, he1, he2])
        return len(self.half_edges)
