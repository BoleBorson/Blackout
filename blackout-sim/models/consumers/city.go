package consumers

type City struct {
	ConsumptionFactor float64
	BaseConsumption   float64
}

func NewCity() *City {
	return &City{
		BaseConsumption:   100,
		ConsumptionFactor: 2,
	}
}

func (city City) GetConsumption() float64 {
	return city.BaseConsumption * city.ConsumptionFactor
}
