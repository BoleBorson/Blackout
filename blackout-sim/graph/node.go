package graph

import (
	"errors"

	"github.com/mitchellh/hashstructure"
)

type Node struct {
	Payload any
	Edges   map[uint64]*Edge
}

func NewNode(payload any) *Node {
	return &Node{
		Payload: payload,
		Edges:   map[uint64]*Edge{},
	}
}

func (node *Node) GetEdge(destNode *Node) (*Edge, error) {
	destNodeHash, err := hashstructure.Hash(*destNode, nil)
	if err != nil {
		return nil, err
	}
	if edge, ok := node.Edges[destNodeHash]; ok {
		return edge, nil
	}
	return nil, errors.New("no edge between nodes")
}

func (node *Node) Compare(compareTo *Node) (bool, error) {
	nodeHash, err := hashstructure.Hash(*node, nil)
	if err != nil {
		return false, err
	}

	compareHash, err := hashstructure.Hash(*compareTo, nil)
	if err != nil {
		return false, err
	}

	if nodeHash == compareHash {
		return true, nil
	}
	return false, nil
}
