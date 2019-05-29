import math
DEFAULT_BUCKET_SIZE =10
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j>=0 and key<arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
def sort(array, bucketSize=DEFAULT_BUCKET_SIZE):
	if len(array) == 0:
		return array
	minValue = array[0]
	maxValue = array[0]
	for i in range(1, len(array)):
		if array[i] < minValue:
			minValue = array[i]
		elif array[i] > maxValue:
			maxValue = array[i]
	bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
	buckets = []
	for i in range(0, bucketCount):
		buckets.append([])
	for i in range(0, len(array)):
		buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])
	array = []
	for i in range(0, len(buckets)):
		insertionSort(buckets[i])
		for j in range(0, len(buckets[i])):
			array.append(buckets[i][j])
	for i in range(0,len(array)):
		print(array[i])
sort([83, 45, 76, 1, 70, 34])
