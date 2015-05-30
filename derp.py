
def run(self, machineNumber, port_number):
	block_size = int(/machineNumber)
	block_count = int(array_size/block_size)
	numpy.set_printoptions(threshold=numpy.nan)
	# Pyro4.config.SERIALIZER = "pickle"
	machine_count = 0
	for x in range(0, block_count):
	    temp_array = []
	    for y in range(0, block_count):
	        url = servers[machine_count % len(servers)] + str(port_number)
	        matrix = Pyro4.Proxy(url)
	        matrix.clear_c_matrix()
	        matrix.set_matrix_a(matrixA[x][y])
	        matrix.set_matrix_b(matrixB[x][y])
	        temp_array.append(matrix)
	        machine_count += 1
	        if machine_count % 2 == 0:
	            port_number += 1
	    self.array.append(temp_array)
	for i in range(0, machineNumber):
	    for element in self.array:
	        for value in element:
	            value.multiply()
	    self.shift_a_matrix_left()
	    self.shift_b_matrix_up(block_size, block_count)
	self.get_result_matrix(block_size)
	print("--- %s seconds ---" % (time.time() - start_time))
