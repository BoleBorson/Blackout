package main

import (
	"fmt"

	"blackout.com/sim/graph/seed"
)

func main() {

	g := seed.SeedFromJSON("/home/cole/code-projects/Blackout/blackout-sim/graph/seed/test_graph.json")
	fmt.Println(g)

	// g := graph.NewGraph()
	// node := graph.NewNode("Cole")
	// node2 := graph.NewNode("Shelley")
	// node3 := graph.NewNode("Joe")

	// g.AddNode(node)
	// // Test adding same node twice to ensure set works
	// g.AddNode(node)
	// g.AddNode(node2)
	// err := g.AddEdge(node, node2)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }

	// err = g.AddEdge(node2, node3)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }

	// fmt.Println(g)
	// coleNode, err := g.GetNode(node)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }

	// fmt.Println(coleNode)

	// fmt.Println(g)
	// edge, err := node.GetEdge(node3)
	// if err != nil {
	// 	fmt.Println(err)
	// 	return
	// }
	// fmt.Println(*edge)

}
