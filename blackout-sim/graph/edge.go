package graph

type Edge struct {
	Weight   int64
	NextNode *Node
}

func NewEdge(weight int64, nextNode *Node) *Edge {
	return &Edge{
		Weight:   weight,
		NextNode: nextNode,
	}
}
