# InteractiveDependencyGraph

## Features
- Create dependency graph between classes, functions, and files starting from a root file, or everything in the chosen directory. Should take account of decorator. Function with decorator will have 2 modes of viewing. One mode is to see the decorated function as what it is written as(we need to be able to view the decorator code as well), and second is to view the wrapped version of it.
- Create interactive ways to hide and unhide each node's components
- Create interactive ways to choose which graph to look at, in case there are multiple of them
- Create interactive ways to view code in each node when hovered. Can be done by having another window showing the code, which is also ensuring that there can only be one source code opened at once.