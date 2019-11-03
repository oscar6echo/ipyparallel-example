
## ipyparallel Example

This example illustrate how to use [**ipyparallel**](https://ipyparallel.readthedocs.io/en/latest/index.html) to split a parallel algo over several cores, in one or several machines, sharing a disk folder.

The example is contrived but simple so as to focus on the **ipyparallel** setup and operations.

The notebook is used as a cockpit and as such does not contain any code.  
It just calls on the 2 companion packages below:
+ `my_package`:  
    The demo parallel algo articially slowed down but `sleep()` calls.  
    It is interesting mostly in the opiniated interface it provides
+ `setup_ipyparallel`:  
    The package to create the **ipyparallel** scripts to launch the controller / engines.  
    It also to move local packages so that they are visible by the engines.


