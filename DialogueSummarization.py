from datasets import load_dataset

hf_dataset_name = "knkarthick/dialogsum"
dataset = load_dataset(hf_dataset_name, split=None)

# Dataset Inspection
for split in dataset.keys():
    print(f"{split}: {len(dataset[split])} rows")

# print two examples of dataset
indices = [20,400]

dashLine = ''.join(['-' for j in range(100)])

for num, index in enumerate(indices):
    print(dashLine)
    print(f"Example {num+1}")
    print(dashLine)
    print("dialogue:")
    print(dataset['test'][index]['dialogue'])
    print(dashLine)
    print("summary:")
    print(dataset['test'][index]['summary'])
    print(dashLine)


