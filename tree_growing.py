
from aether.diagnostics import set_diagnostics_on
from aether.indices import define_problem_type
from aether.geometry import define_node_geometry_2d, define_elem_geometry_2d, make_data_grid, evaluate_ordering, \
    define_data_geometry, define_node_geometry, define_1d_elements, group_elem_parent_term
from aether.exports import export_node_geometry_2d, export_elem_geometry_2d, export_data_geometry, export_node_geometry, \
    export_1d_elem_geometry
from aether.growtree import grow_tree
import os


set_diagnostics_on(False)
define_problem_type('grow_tree')

define_node_geometry('P2BRP228-H10777_UpperAirway.ipnode')
define_1d_elements('P2BRP228-H10777_UpperAirway.ipelem')

# Growing into RLL
define_node_geometry_2d('Right_fitted.ipnode')
define_elem_geometry_2d('RLL_surface.ipelem', 'unit')
make_data_grid(0, 5.35, False, 'test', 'test')
evaluate_ordering()
group_elem_parent_term(23)
grow_tree(23, 1, 60.0, 20.0, 0.4, 1.5, 1.5, 180.0,  False, 'test')


# Growing into RUL
define_node_geometry_2d('Right_fitted.ipnode')
define_elem_geometry_2d('RUL_surface.ipelem', 'unit')
make_data_grid(0, 5.35, False, 'test', 'test')
evaluate_ordering()
group_elem_parent_term(15)
grow_tree(15, 1, 60.0, 20.0, 0.4, 1.5, 1.5, 180.0,  False, 'test')

# Growing into RML
define_node_geometry_2d('Right_fitted.ipnode')
define_elem_geometry_2d('RML_surface.ipelem', 'unit')
make_data_grid(0, 5.35, False, 'test', 'test')
evaluate_ordering()
group_elem_parent_term(24)
grow_tree(24, 1, 60.0, 20.0, 0.4, 1.5, 1.5, 180.0,  False, 'test')


# Growing into LUL
define_node_geometry_2d('Left_fitted.ipnode')
define_elem_geometry_2d('LUL_surface.ipelem', 'unit')
make_data_grid(0, 5.35, False, 'test', 'test')
evaluate_ordering()
group_elem_parent_term(11)
grow_tree(11, 1, 60.0, 20.0, 0.4, 1.5, 1.5, 180.0,  False, 'test')

# Growing into LLL
define_node_geometry_2d('Left_fitted.ipnode')
define_elem_geometry_2d('LLL_surface.ipelem', 'unit')
make_data_grid(0, 5.35, False, 'test', 'test')
evaluate_ordering()
group_elem_parent_term(12)
grow_tree(12, 1, 60.0, 20.0, 0.4, 1.5, 1.5, 180.0,  False, 'test')

export_node_geometry('Airway/Grown_Full.exnode', 'MAC')
export_1d_elem_geometry('Airway/Grown_Full.exelem', 'MAC')

os.system("perl ex2ipelem.pl  Airway/Grown_Full")
os.system("perl ex2ipnodeVert.pl  Airway/Grown_Full")
