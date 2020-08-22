from matplotlib_venn import venn3
from matplotlib import pyplot as plt

set1 = set(['A', 'B', 'C', 'D'])
set2 = set(['B', 'C', 'D', 'E'])
set3 = set(['C', 'D',' E', 'F', 'G'])
set4 = set(['C', 'D'])

venn3([set1, set2, set3], ('Set1', 'Set2', 'Set3'))
plt.show()
