class VM:
    def __init__(self, vm_id):
        self.vm_id = vm_id
        self.is_busy = False

class Cloudlet:
    def __init__(self, cloudlet_id):
        self.cloudlet_id = cloudlet_id
        self.status = 'Pending'

def allocate_resources(vms, cloudlets):
    for cloudlet in cloudlets:
        for vm in vms:
            if not vm.is_busy:
                vm.is_busy = True
                cloudlet.status = 'Executed on VM ' + str(vm.vm_id)
                print(f'Cloudlet {cloudlet.cloudlet_id} is executed on VM {vm.vm_id}')
                break

# Create VMs and Cloudlets
vms = [VM(i) for i in range(3)]  # 3 VMs
cloudlets = [Cloudlet(i) for i in range(5)]  # 5 Cloudlets

# Allocate resources
allocate_resources(vms, cloudlets)
