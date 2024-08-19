package producers

type CoalPlant struct {
	ProductionFactor float64
	BaseProduction   float64
}

func NewCoalPlant() *CoalPlant {
	return &CoalPlant{
		BaseProduction:   100,
		ProductionFactor: 2,
	}
}

func (cp CoalPlant) GetProduction() float64 {
	return cp.BaseProduction * cp.ProductionFactor
}
