package graph

import "github.com/mitchellh/hashstructure"

type Graph struct {
	Nodes map[uint64]Node
}

func NewGraph() Graph {
	return Graph{
		Nodes: map[uint64]Node{},
	}
}

func (g Graph) AddNode(node *Node) error {
	// want to hash the actual struct
	nodeHash, err := hashstructure.Hash(*node, nil)
	if err != nil {
		return err
	}

	g.Nodes[nodeHash] = *node
	return nil
}

func (g Graph) GetNode(node *Node) (Node, error) {
	nodeHash, err := hashstructure.Hash(*node, nil)
	if err != nil {
		return Node{}, err
	}

	targetNode := g.Nodes[nodeHash]
	return targetNode, nil
}
