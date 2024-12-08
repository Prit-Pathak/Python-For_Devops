"""
**Simulate Reference Counting in Python**
- **Question**: Write a Python program that simulates reference counting to track the number of references to an object. Display when an object is collected (memory freed) based on reference counting.
- **Task**: Implement custom reference counting and track object lifecycle.
"""


class MyObject:
    """Myobject class that creates object reference"""

    def __init__(self, name):
        self.name = name
        self.ref_count = 1  # Start with a single reference to the object.
        print(f"Object {self.name} created with reference count {self.ref_count}.")

    def add_reference(self):
        """Simulate adding a reference to the object."""
        self.ref_count += 1
        print(
            f"Reference added to {self.name}. Current reference count: {self.ref_count}."
        )

    def remove_reference(self):
        """Simulate removing a reference to the object."""
        if self.ref_count > 0:
            self.ref_count -= 1
            print(
                f"Reference removed from {self.name}. Current reference count: {self.ref_count}."
            )

            if self.ref_count == 0:
                self.collect_garbage()

    def collect_garbage(self):
        """Simulate the garbage collection process."""
        print(f"Object {self.name} is collected (reference count is zero).")
        del self


def reference_count_simulation():
    """Simulator function"""
    # Create an object
    obj1 = MyObject("Object 1")

    # Multiple references to the same object (obj1 is shared across different variables)
    obj2 = obj1
    obj3 = obj1

    obj1.add_reference()  # obj1, obj2, and obj3 are all pointing to the same object

    # Add the object to a list (container) to simulate container references
    obj_list = [obj1]
    obj1.add_reference()  # Adding another reference (from list)

    # Add more references to obj1 from other variables
    obj4 = obj1
    obj4.add_reference()  # Adding another reference

    # Remove references from different places
    obj1.remove_reference()  # Remove one reference from obj1
    obj2.remove_reference()  # Remove one reference from obj2 (same object as obj1)

    # Remove reference from container
    obj_list.remove(obj1)
    obj1.remove_reference()  # obj1 was in obj_list, so remove this reference

    # Removing obj3, obj4
    obj3.remove_reference()  # Remove the reference from obj3
    obj4.remove_reference()  # Remove the reference from obj4


def main():
    """main funcion"""
    # Run the simulation
    reference_count_simulation()


if __name__ == "__main__":
    main()
