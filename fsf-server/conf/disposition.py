#!/usr/bin/python
#
# This is the Python 'module' that contains the 
# disposition criteria for Yara signatures the scanner framework
# will archive/work on. Each member is the name of a  
# high fidelity Yara signature.
#
# Modules that are always run on a returned buffer value
default = ['META_BASIC_INFO',
           'EXTRACT_EMBEDDED',
           'SCAN_YARA']

# STRUCTURE: Array of tuples such that...
# Types:  [('string', 'array', boolean'), ...]
# Variables: [('rule name', ['module_1' , 'module_2'] , 'is archivable'), ...]

triggers = [('ft_zip', ['EXTRACT_ZIP'], False),
            ('ft_exe', ['META_PE'], False),
            ('ft_rar', ['EXTRACT_RAR'], False),
            ('ft_ole_cf', ['META_OLECF'], False),
            ('ft_pdf', ['META_PDF'], False),
            ('misc_ooxml_core_properties', ['META_OOXML'], False),
            ('ft_swf', ['EXTRACT_SWF'], False),
           ]
