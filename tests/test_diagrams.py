# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 13:25:23 2020

@author: yrc2
"""
import pytest
import biosteam as bst
import os

folder = os.path.dirname(__file__)
folder = os.path.join(folder, 'Diagram Sources')
DISPLAY = False

def save_diagrams():
    import biorefineries.sugarcane as sc
    f = sc.C201.diagram(display=DISPLAY)
    file = os.path.join(folder, 'Clarifier.txt')
    expected_source = open(file, 'w')
    expected_source.write(f.source)
    for kind in ('thorough', 'cluster', 'surface', 'minimal'):
        f = sc.sugarcane_sys.diagram(kind, display=DISPLAY)
        file = os.path.join(folder, f'sugarcane {kind}.txt')
        expected_source = open(file, 'w')
        expected_source.write(f.source)
        expected_source.close()

def test_unit_diagram():
    import biorefineries.sugarcane as sc
    sc.load() # Reload system to make sure all is consistent
    f = sc.C201.diagram(display=DISPLAY)
    file = os.path.join(folder, 'Clarifier.txt')
    with open(file) as f_expected:
        expected_source = f_expected.read()
        assert set(f.source.split()) == set(expected_source.split())
    bst.process_tools.default()

def test_system_thorough_diagram():
    import biorefineries.sugarcane as sc
    f = sc.sugarcane_sys.diagram('thorough', display=DISPLAY)
    file = os.path.join(folder, 'sugarcane thorough.txt')
    with open(file) as f_expected:
        expected_source = f_expected.read()
        assert set(f.source.split()) == set(expected_source.split())
    bst.process_tools.default()

def test_system_cluster_diagram():
    import biorefineries.sugarcane as sc
    f = sc.sugarcane_sys.diagram('cluster', display=DISPLAY)
    file = os.path.join(folder, 'sugarcane cluster.txt')
    with open(file) as f_expected:
        expected_source = f_expected.read()
        assert set(f.source.split()) == set(expected_source.split())
    bst.process_tools.default()
    
# TODO: Find out why this test is not working
# def test_system_surface_diagram():
#     import biorefineries.sugarcane as sc
#     f = sc.sugarcane_sys.diagram('surface', display=DISPLAY)
#     file = os.path.join(folder, 'sugarcane surface.txt')
#     with open(file) as f_expected:
#         expected_source = f_expected.read()
#         assert set(f.source.split()) == set(expected_source.split())
#     bst.process_tools.default()
    
# def test_system_minimal_diagram():
#     import biorefineries.sugarcane as sc
#     f = sc.sugarcane_sys.diagram('minimal', display=DISPLAY)
#     file = os.path.join(folder, 'sugarcane minimal.txt')
#     with open(file) as f_expected:
#         expected_source = f_expected.read()
#         assert set(f.source.split()) == set(expected_source.split())
#     bst.process_tools.default()
    
if __name__ == '__main__':
    test_unit_diagram()
    # test_system_surface_diagram()
    test_system_thorough_diagram()
    test_system_cluster_diagram()
    # test_system_minimal_diagram()