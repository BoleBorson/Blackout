package main

import (
	"fmt"

	"blackout.com/sim/graph"
)

func main() {
	g := graph.NewGraph()
	node := graph.NewNode("Cole")
	node2 := graph.NewNode("Shelley")

	g.AddNode(node)
	// Test adding same node twice to ensure set works
	g.AddNode(node)
	g.AddNode(node2)

	fmt.Println(g)
	coleNode, err := g.GetNode(node)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(coleNode)

	node3 := graph.NewNode("Joe")
	g.AddEdge(node, node3)

	fmt.Println(g)

}
