import torch


# Get GPUs, select 0 and ensure uses only as much memory as needed
assert torch.cuda.is_available()
gpus = torch.cuda.device_count()
current = torch.cuda.current_device()

# Test CUDA launched correctly
a = torch.zeros(1).cuda()
print(f"Using gpu {current} of {gpus} gpus")

