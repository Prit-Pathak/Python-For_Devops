"""
Optimize Memory Usage Using a Custom Garbage Collector**
**Question**: Write a Python program with a custom garbage collector that minimizes memory usage by identifying and deleting unused objects based on certain criteria (e.g., inactive or out-of-scope objects).
**Task**: Create a custom memory management system that tracks and frees unused objects.
"""


class CustomGC:
    """Class to simulate garbage collector function"""

    def __init__(self):
        self.objects = []

    def create_object(self, name):
        """Create an object and add it to the objects list"""
        obj = MyClass(name)
        self.objects.append(obj)
        print(f"Object {name} created.")
        return obj

    def collect_garbage(self):
        """Simulate garbage collection by removing all objects that are no longer referenced."""
        print("Collecting unused objects...")
        before_count = len(self.objects)
        # Remove all objects that are not being referenced (simulating the garbage collector)
        self.objects = [obj for obj in self.objects if obj.is_referenced()]
        after_count = len(self.objects)
        print(f"Garbage collected: {before_count - after_count} objects.")


class MyClass:
    """Arbitrary class to assign memory to object"""

    def __init__(self, name):
        """An object is active by default"""
        self.name = name
        self.is_active = True

    def deactivate(self):
        """Mark the object as no longer active"""
        print(f"Deactivating {self.name}")
        self.is_active = False

    def is_referenced(self):
        """Check if the object is active (referenced)"""
        return self.is_active


# Simulate program execution
gc_simulator = CustomGC()

# Create objects
obj1 = gc_simulator.create_object("Object 1")
obj2 = gc_simulator.create_object("Object 2")
obj3 = gc_simulator.create_object("Object 3")

# Deactivate some objects to simulate unused objects
obj2.deactivate()

# Simulate garbage collection to free unused objects
gc_simulator.collect_garbage()

# At this point, only Object 1 and Object 3 should be retained, while Object 2 should be freed.
