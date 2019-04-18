# vertices_selection_sets
>Blender addon to quickly create and use vertex sets for selection.<br>
Very often, when coloring weights, it is inconvenient to use to select vertices by **Vertex-Groups** due to their large number. Therefore, this small addon was written.

## setup:
console commands:
~~~
cd ~/.config/blender/2.79/scripts/addons
git clone https://github.com/volodya-renderberg/vertices_selection_sets.git
~~~
## use:
after the add-on is activated, the menu will be located in **3dView/Tools/Selection Sets/**
![image](https://user-images.githubusercontent.com/22092835/56391480-72304480-6237-11e9-8591-dda4dd2fec4e.png)

##### create set
Put the object into **Edit mode**, select the necessary vertices and click the **create** button, in the dialog box insert the **name** of the set being created.

##### buttons
- **add** - will add the selection of this set to the current selection.
- **replace** - only vertices of this set will be selected.
- **sub** - subtract from current selection.
- **del** - will remove this set

>Data sets are in the text data-block: "vertices_selection_sets_data"
