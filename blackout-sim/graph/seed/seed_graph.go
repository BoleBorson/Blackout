package seed

import (
	"encoding/json"
	"io"
	"log"
	"os"

	"blackout.com/sim/graph"
)

// dummy record as I am not sure what fields I actually want in Node
type SeedNode struct {
	Id      int64   `json:"id"`
	Payload string  `json:"payload"`
	Edges   []int64 `json:"edges"`
}

func SeedFromJSON(filePath string) graph.Graph {
	idTracker := make(map[int64]*graph.Node)
	g := graph.NewGraph()
	seed := loadJsonFile(filePath)

	// Need every node created before an edge can be made
	for _, seedNode := range seed {
		node := graph.NewNode(seedNode.Payload)
		idTracker[seedNode.Id] = node
		g.AddNode(node)
	}

	for _, seedNode := range seed {
		for _, id := range seedNode.Edges {
			nextNode := idTracker[id]
			currentNode := idTracker[seedNode.Id]
			g.AddEdge(currentNode, nextNode)
		}
	}

	return g
}

func loadJsonFile(filePath string) []SeedNode {
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Error opening file: %v", err)
	}
	defer file.Close()

	data, err := io.ReadAll(file)
	if err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	var seed []SeedNode
	err = json.Unmarshal(data, &seed)
	if err != nil {
		log.Fatalf("Error unmarshaling JSON: %v", err)
	}

	// for _, node := range seed {
	// 	fmt.Println("Id:", node.Id)
	// 	fmt.Println("Payload:", node.Payload)
	// 	fmt.Println("Edges:", node.Edges)
	// 	fmt.Println()
	// }

	return seed
}
