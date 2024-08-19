package models

import (
	"math/rand/v2"

	"blackout.com/sim/models/consumers"
	"blackout.com/sim/models/producers"
)

type Entity struct {
	Id       int64
	Consumer Consumer
	Producer Producer
}

// dummy constructor to ensure I know how interfaces work
func NewEntity() *Entity {
	return &Entity{
		// ID needed to randomize hash of entity in the graph
		Id:       rand.Int64N(10000000),
		Consumer: consumers.NewCity(),
		Producer: producers.NewCoalPlant(),
	}
}
