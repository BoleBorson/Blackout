package graph

import (
	"fmt"

	"github.com/mitchellh/hashstructure"
)

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

func (g Graph) AddEdge(srcNode, destNode *Node) error {
	// check for nodes existence
	srcNodeHash, err := hashstructure.Hash(*srcNode, nil)
	if err != nil {
		return err
	}

	destNodeHash, err := hashstructure.Hash(*destNode, nil)
	if err != nil {
		return err
	}

	// if node is not in graph then add it
	if _, ok := g.Nodes[srcNodeHash]; !ok {
		g.AddNode(srcNode)
	}
	if _, ok := g.Nodes[destNodeHash]; !ok {
		g.AddNode(destNode)
	}

	srcNode.Edges[destNodeHash] = NewEdge(10, destNode)

	fmt.Println("========Edge Addition=======")
	fmt.Println("Src Node:", srcNode)
	fmt.Println("Dest Node:", destNode)

	return nil
}
