# Sorting models based on accuracy
models = [("Model A", 0.85), ("Model B", 0.92), ("Model C", 0.88)]
sorted_models = sorted(models, key=lambda x: x[1], reverse=True)
print(sorted_models)
# Output: [('Model B', 0.92), ('Model C', 0.88), ('Model A', 0.85)]
