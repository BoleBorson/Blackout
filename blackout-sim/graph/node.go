package graph

type Node struct {
	Name  string
	Edges map[uint64]*Edge
}

func NewNode(name string) *Node {
	return &Node{
		Name:  name,
		Edges: map[uint64]*Edge{},
	}
}
