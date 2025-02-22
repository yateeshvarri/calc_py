import importlib
import os

def load_plugins(invoker, plugin_folder="plugins"):
    """Dynamically loads plugins from the plugins directory."""
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{plugin_folder}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "register"):
                module.register(invoker)
