import sys
import json
from client import HalfEdgeMesh

mesh = HalfEdgeMesh()

def handle_call(name, arguments):
    if name == "triangle":
        v0 = tuple(arguments["v0"])
        v1 = tuple(arguments["v1"])
        v2 = tuple(arguments["v2"])
        he_count = mesh.build_triangle(v0, v1, v2)
        return {"half_edges": he_count, "vertices": len(mesh.vertices)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
