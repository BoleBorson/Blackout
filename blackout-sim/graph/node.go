package graph

type Node struct {
	Name  string
	Edges map[int]*Edge
}

func NewNode(name string) Node {
	return Node{
		Name: name,
	}
}
