package graph

import (
	"errors"
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
	// if src and dest node are the same, throw error
	ok, err := srcNode.Compare(destNode)
	if err != nil || ok {
		return errors.New("Edge cannot connect a node to itself")
	}

	// if node is not in graph then add it
	ok, err = g.inGraph(srcNode)
	if err != nil {
		return err
	}
	if !ok {
		g.AddNode(srcNode)
	}
	ok, err = g.inGraph(destNode)
	if err != nil {
		return err
	}
	if !ok {
		g.AddNode(destNode)
	}

	destNodeHash, err := hashstructure.Hash(destNode, nil)
	if err != nil {
		return err
	}
	srcNode.Edges[destNodeHash] = NewEdge(10, destNode)

	fmt.Println("========Edge Addition=======")
	fmt.Println("Src Node:", srcNode)
	fmt.Println("Dest Node:", destNode)

	return nil
}

func (g Graph) inGraph(node *Node) (bool, error) {
	nodeHash, err := hashstructure.Hash(*node, nil)
	if err != nil {
		return false, err
	}

	if _, ok := g.Nodes[nodeHash]; !ok {
		return false, nil
	}
	return true, nil
}
