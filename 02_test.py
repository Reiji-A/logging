import logging

logging.basicConfig()
module_levels = {"my_pac.mod01":logging.DEBUG,
                 "my_pac.mod02":logging.INFO}
for module,level in module_levels.items():
    logging.getLogger(module).setLevel(level=level)

"""
複数のモジュールに対して、別々のlogを出す
"""
