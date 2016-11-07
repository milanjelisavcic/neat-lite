import yaml
from neat import NumericParamSpec, NominalParamSpec, NeuronSpec, NetworkSpec, NeuronGene, ConnectionGene, Mutator


linear_spec = NeuronSpec('linear',
	[NumericParamSpec('bias', -1., 1.),
	 NumericParamSpec('gain', 0., 1.)],
	[NominalParamSpec('some_thing', ['surprise', 'motherfucker'])]
)


sigmoid_spec = NeuronSpec('sigmoid',
	[NumericParamSpec('bias', -1., 1.),
	 NumericParamSpec('gain', 0., 1.)]
)


diff_spec = NeuronSpec('differential',
	[NumericParamSpec('bias', -1., 1.)]
)


# test NeuronSpec's param_names() and get_random_parameters()
print(linear_spec.param_names())
print(linear_spec.get_random_parameters())





ng = NeuronGene('my neuron is linear', gain=0.44, bias=99.5, somethingelse='hello')

print(ng['gain'])
print(ng['bias'])
print(ng['somethingelse'])


net_spec = NetworkSpec([linear_spec, sigmoid_spec, diff_spec])

# check NetworkSpec's __getitem__()
print(net_spec['linear'])

# check NetworkSpec's __iter__()
print(list(neutype for neutype in net_spec))
expect = set(['linear', 'sigmoid', 'differential'])
print(expect == set(list(neutype for neutype in net_spec))) 


# check Mutator object construction
mutator = Mutator(net_spec)
print(mutator)


# check Mutator's _get_probabilities()
items = [('a', 0.1), ('b', 0.2), ('c', 0.05), 'd', 'e', 'f', 'g']
expect = set([('a', 0.1), ('b', 0.2), ('c', 0.05), ('d', 0.1625), ('e', 0.1625) , ('f', 0.1625), ('g', 0.1625)])
result = set(  (elem[0], round(elem[1], 5))  for elem in mutator._get_probabilities(items))
print(result)
print(expect == result)

items = [('a', 0.5), ('b', 0.5), ('c', 0.2), 'd', 'e', 'f', 'g']
expect = set([('a', 0.5), ('b', 0.5), ('c', 0.2), ('d', 0.), ('e', 0.) , ('f', 0.), ('g', 0.)])
result = set(  (elem[0], round(elem[1], 5))  for elem in mutator._get_probabilities(items))
print(result)
print(expect == result) 

